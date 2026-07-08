import logging

logger = logging.getLogger(__name__)

def calculate_ids(economy_data: dict) -> float:
    """
    Calculate the Import Dependency Score (IDS) out of 100.
    A higher score implies higher risk / greater dependency.
    
    economy_data expected structure:
    {
        "imports": [{"volume": 1000, "source": "A"}, {"volume": 500, "source": "B"}],
        "chokepoint_exposure": 0.45,  # 45% of imports pass through a chokepoint
        "reserve_days": 60
    }
    """
    try:
        imports = economy_data.get("imports", [])
        chokepoint_exposure = economy_data.get("chokepoint_exposure", 0.0)
        reserve_days = economy_data.get("reserve_days", 0)

        if not imports:
            return 0.0

        # 1. Source Diversification (HHI - Herfindahl-Hirschman Index approach)
        total_volume = sum(item["volume"] for item in imports)
        if total_volume == 0:
            return 0.0
            
        hhi = sum((item["volume"] / total_volume) ** 2 for item in imports)
        # HHI is between ~0 and 1. We scale this to a 0-40 point penalty.
        diversification_penalty = hhi * 40

        # 2. Chokepoint Exposure Penalty (0-40 points)
        chokepoint_penalty = chokepoint_exposure * 40

        # 3. Reserve Buffer Mitigation (0-20 points reduction)
        # Assuming 90 days is a 'safe' buffer.
        safe_buffer = 90.0
        reserve_mitigation = min(reserve_days / safe_buffer, 1.0) * 20

        # Base risk is 20 (inherent dependency on imports)
        base_risk = 20
        
        ids_score = base_risk + diversification_penalty + chokepoint_penalty - reserve_mitigation
        
        return max(0.0, min(100.0, ids_score))
        
    except Exception as e:
        logger.error(f"Error calculating IDS: {e}")
        return -1.0
