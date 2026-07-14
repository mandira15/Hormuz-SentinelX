"""
Mock Maritime Analytics Engine
Hackathon Demo Version

This module simulates maritime traffic around the Strait of Hormuz.
No SQLite, AIS Stream, or external APIs are required.
"""

import asyncio
import random
from datetime import datetime, timezone

# ==========================================================
# GATE DEFINITIONS
# ==========================================================

GATE_A = (26.05, 56.50)
GATE_B = (26.65, 56.10)

GATES = {
    "Strait of Hormuz": {
        "a": GATE_A,
        "b": GATE_B,
        "description": "Primary global oil shipping chokepoint",
    },
    "Fujairah Approach": {
        "a": (25.00, 56.50),
        "b": (25.30, 56.50),
        "description": "Fujairah Port",
    },
    "Dubai Approach": {
        "a": (25.00, 55.20),
        "b": (25.35, 55.20),
        "description": "Dubai / Jebel Ali",
    },
}

# ==========================================================
# ANCHORAGE ZONES
# ==========================================================

ANCHORAGE_ZONES = {
    "Fujairah Anchorage": {
        "lat": 25.15,
        "lon": 56.40,
    },
    "Dubai / Jebel Ali": {
        "lat": 25.05,
        "lon": 55.05,
    },
    "Bandar Abbas": {
        "lat": 27.15,
        "lon": 56.30,
    },
}

# ==========================================================
# CRISIS TIMELINE
# ==========================================================

CRISIS_TIMELINE = [
    {
        "date": "2026-03-01",
        "event": "Regional military escalation",
        "severity": "high",
    },
    {
        "date": "2026-03-03",
        "event": "Shipping advisory issued",
        "severity": "medium",
    },
    {
        "date": "2026-03-06",
        "event": "Commercial vessels rerouted",
        "severity": "critical",
    },
]

# ==========================================================
# STRAIT POLYGON
# ==========================================================

STRAIT_DANGER_ZONE = [
    (26.85, 55.80),
    (26.85, 56.70),
    (26.10, 56.70),
    (26.10, 56.15),
]

# ==========================================================
# SCENARIO DATA
# ==========================================================

SCENARIOS = {
    "normal": {
        "risk": "LOW",
        "inbound": 188,
        "outbound": 181,
        "anchored": 28,
        "waiting": 9,
        "active": 352,
    },

    "limited": {
        "risk": "MEDIUM",
        "inbound": 118,
        "outbound": 112,
        "anchored": 54,
        "waiting": 31,
        "active": 301,
    },

    "conflict": {
        "risk": "HIGH",
        "inbound": 54,
        "outbound": 47,
        "anchored": 103,
        "waiting": 76,
        "active": 228,
    },

    "closed": {
        "risk": "CRITICAL",
        "inbound": 0,
        "outbound": 0,
        "anchored": 171,
        "waiting": 138,
        "active": 191,
    },
}

# ==========================================================
# CURRENT DEMO STATE
# ==========================================================

CURRENT_SCENARIO = "normal"

# ==========================================================
# SHIP TYPES
# ==========================================================

SHIP_TYPES = [
    "Tanker",
    "Cargo",
    "Container",
    "LNG Carrier",
    "Bulk Carrier",
]

FLAGS = [
    "Panama",
    "Liberia",
    "India",
    "Singapore",
    "Marshall Islands",
]

DESTINATIONS = [
    "Dubai",
    "Jebel Ali",
    "Fujairah",
    "Bandar Abbas",
    "Doha",
    "Mumbai",
]

# ==========================================================
# HELPERS
# ==========================================================

def set_demo_scenario(name: str):
    """
    Change the active demo scenario.
    """

    global CURRENT_SCENARIO

    if name in SCENARIOS:
        CURRENT_SCENARIO = name


def current():
    return SCENARIOS[CURRENT_SCENARIO]


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def random_ship():
    return {
        "mmsi": random.randint(100000000, 999999999),
        "ship_name": random.choice([
            "MT Horizon",
            "MV Ocean Star",
            "Pacific Trader",
            "Sea Falcon",
            "Arabian Pearl",
            "Blue Neptune",
            "Eastern Spirit",
        ]),
        "flag": random.choice(FLAGS),
        "destination": random.choice(DESTINATIONS),
        "ship_type": random.choice(SHIP_TYPES),
        "speed": round(random.uniform(8, 18), 1),
        "crossed_at": utc_now(),
    }


def get_ship_type_label(ship_type):
    """
    Compatibility function used by api.py.
    """

    return str(ship_type)

# ==========================================================
# MOCK ANALYTICS FUNCTIONS
# ==========================================================

async def get_transit_summary(hours: int = 24, gate: str | None = None):
    """
    Mock transit summary.
    """

    data = current()

    recent = []

    for _ in range(10):
        ship = random_ship()

        ship["direction"] = random.choice([
            "INBOUND",
            "OUTBOUND",
        ])

        ship["gate"] = "Strait of Hormuz"

        recent.append(ship)

    return {
        "hours": hours,
        "gate_filter": gate,
        "inbound": data["inbound"],
        "outbound": data["outbound"],
        "by_gate": {
            "Strait of Hormuz": {
                "inbound": data["inbound"],
                "outbound": data["outbound"],
            }
        },
        "recent_events": recent,
    }


async def get_hourly_transits(hours=48, gate=None):
    """
    Mock hourly chart.
    """

    base = current()

    chart = []

    for h in range(hours):
        chart.append(
            {
                "hour": f"{h:02d}:00",
                "inbound": max(
                    0,
                    int(base["inbound"] / hours)
                    + random.randint(-3, 3),
                ),
                "outbound": max(
                    0,
                    int(base["outbound"] / hours)
                    + random.randint(-3, 3),
                ),
            }
        )

    return chart


async def get_vessel_states():
    """
    Mock vessel state distribution.
    """

    data = current()

    anchored = data["anchored"]

    transiting = max(0, data["active"] - anchored - 42)

    return {
        "states": {
            "transiting": transiting,
            "anchored": anchored,
            "maneuvering": 26,
            "slow": 16,
            "unknown": 0,
        },
        "total": data["active"],
        "zone_counts": {
            "Fujairah Anchorage": anchored // 2,
            "Dubai / Jebel Ali": anchored // 3,
            "Bandar Abbas": anchored // 4,
        },
        "vessels_by_state": {},
    }


async def get_flag_distribution(hours: int = 24):
    """
    Mock vessel flags.
    """

    return [
        {"flag": "Panama", "vessels": 63},
        {"flag": "Liberia", "vessels": 51},
        {"flag": "India", "vessels": 39},
        {"flag": "Singapore", "vessels": 27},
        {"flag": "Marshall Islands", "vessels": 21},
    ]


async def get_destination_distribution(hours: int = 24):
    """
    Mock destinations.
    """

    return [
        {"destination": "Dubai", "vessels": 48},
        {"destination": "Jebel Ali", "vessels": 41},
        {"destination": "Fujairah", "vessels": 29},
        {"destination": "Bandar Abbas", "vessels": 19},
        {"destination": "Mumbai", "vessels": 14},
    ]


async def get_daily_summary():
    """
    Mock daily dashboard summary.
    """

    data = current()

    return {
        "generated_at": utc_now(),
        "total_records": 18420,
        "records_24h": 3418,
        "unique_vessels_24h": data["active"],
        "transits_24h": {
            "inbound": data["inbound"],
            "outbound": data["outbound"],
            "total": data["inbound"] + data["outbound"],
        },
        "vessel_states": {
            "transiting": data["active"] - data["anchored"],
            "anchored": data["anchored"],
            "maneuvering": 26,
            "slow": 16,
        },
        "anchorage_zones": {
            "Fujairah Anchorage": data["anchored"] // 2,
            "Dubai / Jebel Ali": data["anchored"] // 3,
            "Bandar Abbas": data["anchored"] // 4,
        },
    }

# ==========================================================
# DEMO UTILITIES
# ==========================================================

def randomize_demo():
    """
    Slightly randomize the current scenario values
    to make the dashboard look live.
    """

    data = SCENARIOS[CURRENT_SCENARIO]

    data["inbound"] = max(0, data["inbound"] + random.randint(-5, 5))
    data["outbound"] = max(0, data["outbound"] + random.randint(-5, 5))
    data["anchored"] = max(0, data["anchored"] + random.randint(-2, 2))
    data["waiting"] = max(0, data["waiting"] + random.randint(-2, 2))


async def heartbeat():
    """
    Background task that keeps changing the demo values.
    """

    while True:
        randomize_demo()
        await asyncio.sleep(30)


# ==========================================================
# MODULE TEST
# ==========================================================

if __name__ == "__main__":

    async def run_demo():

        print("\n========== MOCK MARITIME ANALYTICS ==========\n")

        print(await get_transit_summary())

        print(await get_hourly_transits())

        print(await get_vessel_states())

        print(await get_flag_distribution())

        print(await get_destination_distribution())

        print(await get_daily_summary())

        print(await get_blockade_indicators())

        print("\n=============================================\n")

    asyncio.run(run_demo())

async def get_blockade_indicators():
    data = current()

    ratio = round((data["anchored"] / data["active"]) * 100, 1)

    return {
        "active_vessels": data["active"],
        "anchored_vessels": data["anchored"],
        "anchored_ratio_pct": ratio,
        "waiting_fleet_6h": data["waiting"],
        "waiting_fleet_24h": max(0, data["waiting"] - 10),
        "strait_transits_24h": data["inbound"] + data["outbound"],
        "strait_status": CURRENT_SCENARIO.upper(),
        "situation": {
            "level": data["risk"],
            "title": f"{data['risk']} Risk",
            "text": "Demo maritime analytics generated from simulated data."
        },
        "fleet_by_type": [
            {"type": "Tanker", "count": 84},
            {"type": "Cargo", "count": 102},
            {"type": "Container", "count": 61},
        ],
        "fleet_by_flag": [
            {"flag": "Panama", "count": 58},
            {"flag": "Liberia", "count": 41},
            {"flag": "India", "count": 36},
        ],
    }

# ==========================================================
# SCENARIO HELPERS
# ==========================================================

def available_scenarios():
    """Return all available demo scenarios."""
    return list(SCENARIOS.keys())


def get_current_scenario():
    """Return the active demo scenario."""
    return CURRENT_SCENARIO


def set_demo_scenario(name: str):
    """Change the active demo scenario."""
    global CURRENT_SCENARIO

    if name in SCENARIOS:
        CURRENT_SCENARIO = name


# ==========================================================
# INDIA — HORMUZ DEPENDENCY PRESET
# Sources: IEA India 2023, Ministry of Petroleum & Natural Gas,
#          PPAC, Petroleum Planning & Analysis Cell
# ==========================================================

INDIA_HORMUZ_PRESET = {
    "title": "India Crude Oil Imports via Strait of Hormuz",
    "subtitle": "What a Hormuz Crisis Means for India's Fuel Prices",
    "baseline": {
        # India total crude oil imports: ~4.8 mb/d (IEA 2023)
        "total_crude_imports_mbd": 4.8,
        # Share transiting Hormuz: ~64% of India's crude comes from Gulf producers
        # (Iraq, Saudi Arabia, UAE, Kuwait, Iran proxy) that must use Hormuz
        "hormuz_dependent_mbd": 3.1,
        "hormuz_dependency_pct": 64.5,
        # Strategic Petroleum Reserve capacity: ~5.33 million tonnes (~39 mb)
        "spr_days_cover": 9.5,
        # India's domestic crude production: ~0.75 mb/d
        "domestic_production_mbd": 0.75,
        # Non-Hormuz alternate supply available (Russia, Nigeria, US, Angola etc.)
        "non_hormuz_flex_mbd": 1.4,
        # India's refining capacity: 5.0 mb/d
        "refining_capacity_mbd": 5.0,
        # Brent reference price baseline (USD/barrel)
        "brent_baseline_usd": 82,
        # Petrol retail price baseline in India (₹/litre)
        "petrol_baseline_inr": 94.72,
        # Diesel retail price baseline (₹/litre)
        "diesel_baseline_inr": 87.62,
        # Top Gulf suppliers through Hormuz
        "top_suppliers": [
            {"country": "Iraq",         "mbd": 1.04, "pct": 21.7},
            {"country": "Saudi Arabia", "mbd": 0.68, "pct": 14.2},
            {"country": "UAE",          "mbd": 0.49, "pct": 10.2},
            {"country": "Kuwait",       "mbd": 0.35, "pct":  7.3},
            {"country": "Oman",         "mbd": 0.28, "pct":  5.8},
            {"country": "Qatar (LNG)",  "mbd": 0.26, "pct":  5.4},
        ],
    },
}

# Closure scenario definitions (30 / 60 / 100 %)
INDIA_CLOSURE_SCENARIOS = {
    30: {
        "label": "30% Closure",
        "tag": "Partial Disruption",
        "color": "#fdd835",
        "description": (
            "Conflict threatens navigation; 30% of Hormuz-dependent tankers rerouted "
            "or delayed. Insurance surcharges spike. India activates partial SPR release."
        ),
    },
    60: {
        "label": "60% Closure",
        "tag": "Severe Crisis",
        "color": "#ff9800",
        "description": (
            "Active hostilities; Iranian mine threats. Most Gulf tankers halt. India invokes "
            "Emergency Petroleum Act. Alternative routing via Cape of Good Hope adds 20 days. "
            "Panic buying begins at pumps."
        ),
    },
    100: {
        "label": "100% Closure",
        "tag": "Full Blockade",
        "color": "#ff5252",
        "description": (
            "Complete chokepoint closure. All 3.1 mb/d of India's Hormuz-linked crude "
            "stops flowing. SPR exhausted in ~9 days. Fuel rationing introduced. "
            "Industrial output falls sharply."
        ),
    },
}


def compute_india_hormuz_impact(closure_pct: int) -> dict:
    """
    Compute India's supply gap, resilience score, and fuel price impact
    for a given Hormuz closure percentage (30, 60, or 100).

    Real-world assumptions:
    - Rerouting via Cape Good Hope adds ~20 days and ~$3/bbl freight premium per 10% closure
    - Brent premium scales roughly +$8/bbl per 30% closure tier
    - India petrol/diesel price: 35-40% crude cost pass-through after taxes/duties buffer
    - Alternative diversification from Russia/US/Nigeria can offset ~45% of lost Gulf supply
    - SPR cover: 9.5 days at full demand
    """
    base = INDIA_HORMUZ_PRESET["baseline"]
    hormuz_dep = base["hormuz_dependent_mbd"]
    domestic = base["domestic_production_mbd"]
    flex = base["non_hormuz_flex_mbd"]
    spr_days = base["spr_days_cover"]
    brent_base = base["brent_baseline_usd"]
    petrol_base = base["petrol_baseline_inr"]
    diesel_base = base["diesel_baseline_inr"]

    # Volume disrupted
    disrupted_mbd = round(hormuz_dep * closure_pct / 100, 2)

    # India can flex ~45% of disruption from non-Hormuz sources
    flex_offset = min(flex, disrupted_mbd * 0.45)
    net_supply_gap_mbd = round(max(0, disrupted_mbd - flex_offset), 2)

    # Effective supply (domestic + non-Gulf imports + flex)
    effective_supply = round(domestic + (hormuz_dep - disrupted_mbd) + flex_offset, 2)

    # SPR additional buffer in days at net gap rate
    spr_buffer_days = round(spr_days * (hormuz_dep / (net_supply_gap_mbd + 0.01)), 1) \
        if net_supply_gap_mbd > 0 else 999

    # Brent price spike ($8 per 30% closure tier, exponential above 60%)
    brent_premium = {30: 8, 60: 22, 100: 48}.get(closure_pct, closure_pct * 0.48)
    brent_crisis = brent_base + brent_premium

    # India pass-through: ~35% cost pass-through after excise buffer
    usd_inr = 83.5
    bbl_to_litre = 6.29   # 1 barrel ≈ 158.99 litres, but accounting for refinery yield
    cost_increase_per_litre = round(
        (brent_premium / bbl_to_litre) * usd_inr * 0.35, 2
    )
    petrol_crisis = round(petrol_base + cost_increase_per_litre, 2)
    diesel_crisis = round(diesel_base + cost_increase_per_litre * 0.9, 2)

    # Freight surcharge (Cape rerouting)
    freight_premium_per_bbl = round(closure_pct / 10 * 0.3, 1)

    # Resilience score (0–100): starts at 72 (India's baseline — diversified but Gulf-heavy)
    # Deductions: supply gap severity, SPR cover, price shock magnitude
    resilience = 72
    resilience -= min(35, net_supply_gap_mbd * 15)   # supply gap penalty
    resilience -= min(15, brent_premium * 0.3)         # price shock penalty
    resilience += min(10, spr_buffer_days * 0.4)       # SPR bonus (capped)
    resilience = max(0, min(100, round(resilience)))

    # Macro impact
    gdp_impact_pct = round(net_supply_gap_mbd * 0.6, 1)  # ~0.6% GDP per mb/d gap
    inflation_bps = int(net_supply_gap_mbd * 120)         # ~120 bps CPI per mb/d gap

    scenario_meta = INDIA_CLOSURE_SCENARIOS.get(closure_pct, {})

    return {
        "closure_pct": closure_pct,
        "label": scenario_meta.get("label", f"{closure_pct}% Closure"),
        "tag": scenario_meta.get("tag", "Disruption"),
        "color": scenario_meta.get("color", "#ff9800"),
        "description": scenario_meta.get("description", ""),
        "supply": {
            "hormuz_dependent_mbd": hormuz_dep,
            "disrupted_mbd": disrupted_mbd,
            "flex_offset_mbd": round(flex_offset, 2),
            "net_supply_gap_mbd": net_supply_gap_mbd,
            "effective_supply_mbd": effective_supply,
            "spr_cover_days": spr_days,
            "spr_buffer_days_at_gap": min(999, spr_buffer_days),
        },
        "price": {
            "brent_baseline_usd": brent_base,
            "brent_crisis_usd": brent_crisis,
            "brent_premium_usd": brent_premium,
            "freight_premium_per_bbl": freight_premium_per_bbl,
            "petrol_inr_baseline": petrol_base,
            "petrol_inr_crisis": petrol_crisis,
            "diesel_inr_baseline": diesel_base,
            "diesel_inr_crisis": diesel_crisis,
            "cost_increase_per_litre_inr": cost_increase_per_litre,
        },
        "macro": {
            "gdp_impact_pct": gdp_impact_pct,
            "cpi_inflation_bps": inflation_bps,
        },
        "resilience_score": resilience,
    }


def get_india_hormuz_all_scenarios() -> dict:
    """Return India resilience data for all three closure scenarios."""
    return {
        "preset": INDIA_HORMUZ_PRESET,
        "scenarios": {
            pct: compute_india_hormuz_impact(pct)
            for pct in [30, 60, 100]
        },
        "metadata": {
            "last_updated": "2024-Q4",
            "sources": [
                "IEA India Energy Review 2023",
                "Ministry of Petroleum & Natural Gas, India",
                "PPAC (Petroleum Planning & Analysis Cell)",
                "Indian Strategic Petroleum Reserves Ltd (ISPRL)",
                "IMF World Economic Outlook 2024",
            ],
        },
    }


async def transit_detection_loop(interval_sec: int = 300):
    """
    Dummy loop for hackathon demo to run heartbeat and randomize demo values.
    """
    await heartbeat()
