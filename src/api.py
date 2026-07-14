"""
FastAPI Backend (Hackathon Demo)

Uses simulated analytics instead of SQLite/AIS.
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.analytics import (
    GATES,
    GATE_A,
    GATE_B,
    ANCHORAGE_ZONES,
    STRAIT_DANGER_ZONE,
    CRISIS_TIMELINE,
    INDIA_HORMUZ_PRESET,
    available_scenarios,
    get_current_scenario,
    set_demo_scenario,
    get_transit_summary,
    get_hourly_transits,
    get_vessel_states,
    get_flag_distribution,
    get_destination_distribution,
    get_daily_summary,
    get_blockade_indicators,
    get_india_hormuz_all_scenarios,
    compute_india_hormuz_impact,
)


app = FastAPI(
    title="Hormuz Maritime Intelligence",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# ==========================================================
# HOME
# ==========================================================

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "map.html",
        {
            "request": request
        },
    )


# ==========================================================
# SCENARIO
# ==========================================================

@app.get("/api/scenario")
async def current_scenario():
    return {
        "current": get_current_scenario(),
        "available": available_scenarios(),
    }


@app.post("/api/scenario/{scenario}")
async def change_scenario(scenario: str):

    set_demo_scenario(scenario)

    return {
        "success": True,
        "current": get_current_scenario(),
    }


# ==========================================================
# ANALYTICS
# ==========================================================

@app.get("/api/analytics/transits")
async def api_transits(
    hours: int = 24,
    gate: str | None = None,
):

    return await get_transit_summary(hours, gate)


@app.get("/api/analytics/hourly")
async def api_hourly(
    hours: int = 48,
    gate: str | None = None,
):

    return {
        "hours": hours,
        "data": await get_hourly_transits(hours, gate),
    }


@app.get("/api/analytics/states")
async def api_states():

    return await get_vessel_states()


@app.get("/api/analytics/flags")
async def api_flags(hours: int = 24):

    return {
        "hours": hours,
        "data": await get_flag_distribution(hours),
    }


@app.get("/api/analytics/destinations")
async def api_destinations(hours: int = 24):

    return {
        "hours": hours,
        "data": await get_destination_distribution(hours),
    }

# ==========================================================
# GATE INFORMATION
# ==========================================================

@app.get("/api/analytics/gate")
async def api_gate():

    return {
        "gates": {
            name: {
                "a": {
                    "lat": gate["a"][0],
                    "lon": gate["a"][1],
                },
                "b": {
                    "lat": gate["b"][0],
                    "lon": gate["b"][1],
                },
                "description": gate.get("description", ""),
            }
            for name, gate in GATES.items()
        },
        "anchorage_zones": ANCHORAGE_ZONES,
        "danger_zone": [
            {
                "lat": p[0],
                "lon": p[1],
            }
            for p in STRAIT_DANGER_ZONE
        ],
        "crisis_timeline": CRISIS_TIMELINE,
    }


# ==========================================================
# BLOCKADE
# ==========================================================

@app.get("/api/analytics/blockade")
async def api_blockade():

    return await get_blockade_indicators()


# ==========================================================
# DAILY SUMMARY
# ==========================================================

@app.get("/api/analytics/summary")
async def api_summary():

    return await get_daily_summary()


# ==========================================================
# INDIA — HORMUZ IMPACT (INDIA-SPECIFIC PRESET)
# ==========================================================

@app.get("/api/india-hormuz")
async def api_india_hormuz():
    """
    Return India crude oil import baseline + resilience scores
    for 30%, 60%, and 100% Hormuz closure scenarios.
    Real data from IEA, MoPNG, PPAC.
    """
    return get_india_hormuz_all_scenarios()


@app.get("/api/india-hormuz/{closure_pct}")
async def api_india_hormuz_scenario(closure_pct: int):
    """
    Return India impact for a specific closure percentage.
    Accepts: 30, 60, or 100
    """
    if closure_pct not in (30, 60, 100):
        return {"error": "closure_pct must be 30, 60, or 100"}
    return compute_india_hormuz_impact(closure_pct)


# ==========================================================
# HEALTH CHECK
# ==========================================================

@app.get("/health")
async def health():

    return {
        "status": "ok",
        "backend": "running",
        "mode": "demo",
        "scenario": get_current_scenario(),
    }


# ==========================================================
# DEMO API
# ==========================================================

@app.get("/api/demo")
async def demo():

    return {
        "project": "Hormuz Maritime Intelligence Platform",
        "version": "1.0",
        "mode": "Hackathon Demo",
        "database": False,
        "live_data": False,
        "analytics": "Simulated",
        "scenario": get_current_scenario(),
    }


# ==========================================================
# STARTUP
# ==========================================================

@app.on_event("startup")
async def startup():

    print("=" * 60)
    print("Hormuz Maritime Intelligence")
    print("Hackathon Demo Backend Started")
    print("=" * 60)

    print(f"Scenario : {get_current_scenario()}")
    print("Database : Disabled")
    print("Analytics : Mock Simulation")
    print("=" * 60)