import os
import json
import logging
import hashlib
from groq import Groq
import redis

logger = logging.getLogger(__name__)

# Initialize Clients
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "mock_key_for_testing")
client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY != "mock_key_for_testing" else None

# Redis setup for caching
redis_host = os.environ.get("REDIS_HOST", "localhost")
cache = redis.Redis(host=redis_host, port=6379, db=0, decode_responses=True)

def cached_llm_call(prompt: str, system_prompt: str, model="llama-3.1-8b-instant") -> str:
    """Calls Groq API with aggressive Redis caching to prevent rate limits."""
    if not client:
        logger.warning("No GROQ_API_KEY. Returning mock response.")
        return "MOCK_RESPONSE: " + prompt[:50] + "..."

    # Hash the prompts for the cache key
    cache_key_raw = f"{model}:{system_prompt}:{prompt}"
    cache_key = hashlib.md5(cache_key_raw.encode()).hexdigest()
    
    cached_response = cache.get(cache_key)
    if cached_response:
        logger.info(f"Cache hit for key {cache_key}")
        return cached_response
        
    logger.info(f"Cache miss for key {cache_key}. Calling Groq API...")
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        response_text = completion.choices[0].message.content
        
        # Cache for 24 hours
        cache.setex(cache_key, 86400, response_text)
        return response_text
    except Exception as e:
        logger.error(f"Groq API call failed: {e}")
        raise e

# --- Agent Prompts ---

PROMPT_GEOPOLITICAL = """
You are a senior Geopolitical Risk Analyst specializing in global energy security.

Analyze the supplied economy and import dependency data.

Focus on:
- Geopolitical conflicts
- Middle East tensions
- Strait of Hormuz closure risk
- Regional instability
- International sanctions
- Energy security
- Countries highly dependent on oil imports

Return a concise professional assessment with:
- Risk Level
- Key Geopolitical Risks
- Expected Impact
"""

PROMPT_LOGISTICS = """
You are a Maritime Logistics Analyst.

Analyze the supply chain resilience of the selected economy.

Focus on:
- Maritime chokepoints
- Strait of Hormuz
- Shipping delays
- Port congestion
- Alternative shipping routes
- Supply disruption
- Transport resilience

Return:
- Logistics Risk
- Major Bottlenecks
- Suggested Alternate Routes
"""

PROMPT_MARKET = """
You are an Energy Market Analyst.

Analyze how the current scenario affects:

- Oil prices
- LNG prices
- Inflation
- Supply chain cost
- Industrial production
- Import dependency
- Market volatility

Return:
- Economic Impact
- Price Trend
- Market Outlook
"""

PROMPT_SYNTHESIS = """
You are the Chief Risk Officer preparing an executive briefing.

Combine all analyst reports into a concise report.

Return the response in this format:

Executive Summary

Overall Risk Level

Import Dependency Score

Key Findings

Recommendations

Keep the response under 300 words.
"""

def run_agent_pipeline(economy_data: dict, ids_score: float) -> str:
    """
    Orchestrates the multi-agent pipeline sequentially.
    Includes a fallback to a single degraded agent call if the chain fails.
    """
    base_input = f"Economy Data: {json.dumps(economy_data)}\nImport Dependency Score (IDS): {ids_score}/100"
    
    try:
        logger.info("Starting Agent Pipeline...")
        geo_report = cached_llm_call(base_input, PROMPT_GEOPOLITICAL)
        logistics_report = cached_llm_call(base_input, PROMPT_LOGISTICS)
        market_report = cached_llm_call(base_input, PROMPT_MARKET)
        
        synthesis_input = f"Geopolitical Report:\n{geo_report}\n\nLogistics Report:\n{logistics_report}\n\nMarket Report:\n{market_report}"
        final_brief = cached_llm_call(synthesis_input, PROMPT_SYNTHESIS, model="llama-3.1-70b-versatile")
        
        return final_brief
        
    except Exception as e:
        logger.error(f"Pipeline failed: {e}. Falling back to degraded single-agent mode.")
        # Fallback Mode: Ask the synthesis agent to do its best with raw data alone
        fallback_prompt = "You are a crisis analyst. Provide a brief assessment based on this raw data."
        try:
            return cached_llm_call(base_input, fallback_prompt, model="llama-3.1-8b-instant")
        except Exception as fallback_e:
            return f"Error: Unable to generate brief. System degraded. ({fallback_e})"

if __name__ == "__main__":
    # Test script
    mock_data = {"imports": [{"volume": 1200000, "source": "Saudi Arabia"}], "chokepoint_exposure": 0.85, "reserve_days": 120}
    print(run_agent_pipeline(mock_data, 49.5))
