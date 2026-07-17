<div align="center">

<img src="https://img.shields.io/badge/🛡️%20HORMUZ%20SENTINELX-AI%20Energy%20Security%20Intelligence-0a1628?style=for-the-badge&labelColor=0d1b2a&color=1a3a5c" alt="Hormuz SentinelX" />

# 🛡️ Hormuz-SentinelX
### *AI-Powered Energy Security Intelligence Command*

**India's geopolitical crisis simulation platform for the Strait of Hormuz**

[![Live Demo](https://img.shields.io/badge/🌐%20Live%20Demo-hormuz--sentinelx.onrender.com-4a8fe8?style=for-the-badge&logo=render&logoColor=white)](https://hormuz-sentinelx.onrender.com/)
[![Deploy to Render](https://img.shields.io/badge/Deploy%20to-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/deploy?repo=https://github.com/mandira15/Hormuz-SentinelX)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.103%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-d8a73c?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Live%20%26%20Deployed-4fd299?style=for-the-badge)](https://hormuz-sentinelx.onrender.com/)

---

> **An AI-powered Energy Security Intelligence platform that simulates geopolitical disruptions in the Strait of Hormuz and analyzes their cascading impact on India's energy security, fuel prices, supply chains, and economy through interactive scenario-based decision support.**

</div>

---

## 🎬 Walkthrough Demo

<!-- WALKTHROUGH_VIDEO_PLACEHOLDER: Replace this comment with your video embed once uploaded -->
> 📹 **Walkthrough video** — *upload your demo video to this repo and replace this section with:*
> ```md
> https://user-images.githubusercontent.com/YOUR_USER_ID/YOUR_VIDEO_ID.mp4
> ```

---

## 🌐 Live Application

**🚀 [https://hormuz-sentinelx.onrender.com/](https://hormuz-sentinelx.onrender.com/)**

The platform is fully deployed and accessible. No login required — open and explore all scenarios immediately.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Workflow Architecture](#-workflow-architecture)
- [Dashboard Panels](#-dashboard-panels)
- [Scenario Engine](#-scenario-engine)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Docker Deployment](#-docker-deployment)
- [Data Sources](#-data-sources--references)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)

---

## 🔍 Overview

The **Strait of Hormuz** is the world's most critical energy chokepoint — ~21 million barrels of oil pass through it daily, representing 20–21% of global petroleum liquids. **India sources ~64.5% of its crude oil imports** (≈3.1 mb/d) through this narrow 33 km passage.

**Hormuz-SentinelX** is a strategic intelligence command platform designed for India's Ministry of Petroleum & Natural Gas (MoPNG) and PPAC analysts to:

- 🎯 **Simulate** 3 levels of Hormuz closure (30% Partial / 60% Severe / 100% Full Blockade)
- 📊 **Quantify** cascading economic shocks: Brent spike, petrol/diesel prices, GDP contraction, CPI inflation
- 🗺️ **Visualize** real maritime trade routes on an interactive geospatial map
- 🤖 **Generate** AI executive situation reports with confidence scores and recommended policy actions
- ⏱️ **Track** supply chain cascade timelines from closure day to economic impact

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🗺️ **Interactive Strategic Map** | Leaflet.js map showing Strait of Hormuz, Gulf shipping lanes, and India's exposure routes |
| 🎭 **3-Scenario Simulator** | Toggle between 30% Partial / 60% Severe / 100% Full Blockade — all KPIs update live |
| 📊 **Economic Shock Index (ESI)** | Animated arc gauge (0–100) measuring real-time economic stress |
| 🤖 **AI Executive Brief** | Typewriter-animated situation report with confidence score from IEA, MoPNG, PPAC & IMF |
| 🎯 **National Resilience Radar** | Spider/radar chart showing India's resilience across 6 dimensions vs. baseline |
| ⚡ **AI Recommended Actions** | Priority-tagged policy actions (IMMEDIATE / URGENT / HIGH / MONITOR) per scenario |
| 🛢️ **SPR Buffer Dashboard** | Strategic Petroleum Reserve status across Padur, Vizag & Mangalore facilities |
| ⛽ **Fuel Price Simulation** | Real-time petrol, diesel, LPG, aviation turbine fuel price impact with freight overlays |
| 📉 **Macroeconomic Gauges** | Live GDP contraction risk and CPI inflation arc gauges with numeric overlays |
| ⏱️ **Supply Chain Cascade Timeline** | Day-by-day cascade from closure event to petrol pump shortages and industrial disruptions |
| 🔄 **Import Dependency Sankey** | Sankey flow diagram: Gulf Suppliers → India Refinery → Economic Sectors |
| 🚨 **Emergency Protocol Mode** | Toggleable FUEL-RED emergency mode with animated alert banners |
| 📡 **Intel Ticker** | Live-scrolling news-style ticker with scenario-aware intelligence updates |
| 🌙 **Dark Command UI** | Military-grade dark dashboard with glassmorphism panels and animated grid |

---

## 🏗️ Workflow Architecture

The following diagram shows the full system architecture of Hormuz-SentinelX:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    HORMUZ SENTINELX — SYSTEM ARCHITECTURE           │
└─────────────────────────────────────────────────────────────────────┘

┌──────────────────┐
│  Future Live     │──future feed──►┌──────────────────┐
│  Data Sources    │                │    API Layer     │──triggers──►┐
└──────────────────┘                │  (FastAPI/REST)  │            │
                                    └──────────────────┘            │
                                                                     ▼
                                                         ┌──────────────────┐
                                                         │ Analytics Engine │──feeds──►┐
                                                         │ (Python/Pandas)  │          │
                                                         └──────────────────┘          │
                                                                                       │
                    ┌──────────────────────────────────────────────────────────────────┘
                    │                    generates
                    ▼
     ┌──────────────────────┐   future enhance   ┌─────────────────────┐
     │  AI Intelligence     │◄──────────────────│  Future AI Layer    │
     │  Engine              │                    │  (LLM Integration)  │
     │  (Scenario Logic)    │                    └─────────────────────┘
     └──────────────────────┘
              │                    │                    │
         generates            generates               runs
              │                    │                    │
              ▼                    ▼                    ▼
     ┌──────────────┐  ┌──────────────────┐  ┌──────────────────┐
     │   Outputs    │  │  Scenario Engine │  │  Mock Data Layer │
     │  (Reports,   │  │  (30/60/100%)    │◄─│  (Simulated      │
     │   KPIs,      │  │                  │  │   Scenario Data) │
     │   Alerts)    │  └──────────────────┘  └──────────────────┘
     └──────────────┘

                    ┌──────────────────────────────────┐
  User accesses ───►│        Web Dashboard             │
                    │   (HTML5 / Vanilla JS / CSS)     │
                    └──────────────────────────────────┘
                         │   renders panels:
          ┌──────────────┴─────────────────────────────────────────────────┐
          │              │              │              │                    │
          ▼              ▼              ▼              ▼                    ▼
  ┌────────────┐ ┌──────────────┐ ┌──────────┐ ┌──────────────┐ ┌──────────────────┐
  │Interactive │ │  Scenario    │ │Executive │ │  Economic    │ │National          │
  │Map (Leaflet│ │  Simulator   │ │Sit. Rpt. │ │  Shock Dash  │ │Resilience Radar  │
  └────────────┘ └──────────────┘ └──────────┘ └──────────────┘ └──────────────────┘
          │              │
          ▼              ▼
  ┌──────────────┐ ┌──────────────────────┐
  │  SPR Buffer  │ │ Supply Chain Cascade │
  │  Timeline    │ │ Timeline & Sankey    │
  └──────────────┘ └──────────────────────┘
```

### Data Flow

```
User selects scenario (30% / 60% / 100%)
          │
          ▼
Scenario Engine calculates:
  ├── Supply gap (mb/d)
  ├── Brent crude spike ($)
  ├── Fuel price deltas (₹/L)
  ├── ESI score (0-100)
  ├── GDP contraction (%)
  ├── CPI inflation (bps)
  └── SPR drawdown days
          │
          ▼
Analytics Engine feeds → AI Intelligence Engine
          │
          ├── Updates all dashboard KPI cards
          ├── Regenerates AI Executive Brief
          ├── Re-renders Radar & Sankey charts
          ├── Updates Cascade Timeline
          └── Updates Map overlays & badges
```

---

## 🎛️ Dashboard Panels

The platform renders a **3-column military command dashboard**:

### Left Column

| Panel | Description |
|---|---|
| 🤖 AI Executive Situation Report | Typewriter-animated briefing with live confidence score |
| 🎯 National Resilience Radar | 6-axis spider chart vs. baseline |
| ⚡ AI Recommended Actions | Priority-tagged policy action list |

### Center Column

| Panel | Description |
|---|---|
| 🗺️ Strategic Map Strip | Interactive Leaflet map of Hormuz region (expandable) |
| 📊 Economic Shock Index | Arc gauge 0–100 with animated needle |
| 🔢 KPI Cards | Supply Gap (mb/d), Brent Price, SPR Days, GDP Risk |
| 📈 Scenario Comparison Matrix | Side-by-side 30/60/100% scenario data |
| ⏱️ Supply Chain Cascade | Day-by-day cascade timeline |
| 🔄 Import Dependency Flow | Sankey: Gulf → India Refinery → Economic Sectors |

### Right Column

| Panel | Description |
|---|---|
| 📉 Macroeconomic Impact Gauges | GDP & CPI arc gauges |
| ⛽ Fuel Price Impact | Petrol, Diesel, LPG, ATF price cards with freight bar |
| 🛢️ SPR Status | Reserve meter across Padur, Vizag & Mangalore |

---

## 🎭 Scenario Engine

| Scenario | Closure | Supply Gap | Brent Spike | Petrol Price | ESI | GDP Impact | CPI Spike |
|---|---|---|---|---|---|---|---|
| **30% Partial** | 30% | 0.51 mb/d | +$8 → $90/bbl | ₹131.89/L | 28 — *Elevated* | -0.3% | +61 bps |
| **60% Severe** | 60% | 1.24 mb/d | +$35 → $117/bbl | ₹157.42/L | 57 — *High* | -0.8% | +152 bps |
| **100% Blockade** | 100% | 3.1 mb/d | +$75 → $157/bbl | ₹215.07/L | 89 — *Catastrophic* | -2.1% | +380 bps |

> **Baseline**: Petrol ₹94.72/L · Diesel ₹87.62/L · Brent $82/bbl · SPR 64 days cover
> India total crude imports: **4.8 mb/d** | Gulf dependency: **64.5%** | Hormuz exposure: **3.1 mb/d**

---

## 🛠️ Tech Stack

### Backend

| Technology | Version | Purpose |
|---|---|---|
| **Python** | 3.11+ | Core runtime |
| **FastAPI** | ≥0.103.1 | REST API framework with async support |
| **Uvicorn** | ≥0.23.2 | ASGI server |
| **Pydantic** | v2 ≥2.3.0 | Data validation & settings management |
| **aiosqlite** | latest | Async SQLite for state persistence |
| **Pandas / NumPy** | latest | Data processing & scenario mathematics |
| **Jinja2** | latest | HTML templating engine |
| **aiofiles** | latest | Async file I/O |
| **WebSockets** | latest | Real-time data push (planned) |

### Frontend

| Technology | Purpose |
|---|---|
| **HTML5 / Vanilla JS (ES6+)** | Core dashboard logic — zero framework dependencies |
| **Vanilla CSS** | Military-grade dark UI with glassmorphism panels |
| **Leaflet.js 1.9.4** | Interactive geospatial map (Hormuz region + shipping lanes) |
| **Canvas API** | Radar chart, Sankey diagram, arc gauges |
| **Inter + JetBrains Mono** | Typography (Google Fonts) |
| **CSS Animations** | Grid drift, scanlines, pulse, ticker scroll, shimmer |

### Infrastructure

| Technology | Purpose |
|---|---|
| **Docker** | Containerization |
| **Docker Compose** | Local multi-service orchestration |
| **Render.com** | Cloud deployment (live production) |
| **Netlify** | Static frontend hosting option |

---

## 📦 Project Structure

```
Hormuz-SentinelX/
│
├── 📁 src/                     # Core Python backend
│   ├── api/                    # FastAPI routers & endpoints
│   ├── engines/                # Analytics + Scenario + AI engines
│   └── models/                 # Pydantic schemas
│
├── 📁 templates/               # Jinja2 HTML dashboard templates
├── 📁 static/                  # Static CSS, JS, images
├── 📁 frontend/                # Frontend component modules
│
├── 📁 data/                    # Scenario data & mock datasets
│   ├── scenarios/              # JSON scenario definitions (30/60/100%)
│   └── mock/                   # Simulated feed data
│
├── 📁 scripts/                 # Utility scripts (setup, seed)
├── 📁 tests/                   # Test suite
├── 📁 docs/                    # Architecture diagrams & documentation
│
├── 🐳 Dockerfile               # Container image definition
├── 🐳 docker-compose.yml       # Multi-service orchestration
├── ☁️  render.yaml             # Render.com deployment config
├── ☁️  netlify.toml            # Netlify deployment config
├── 📋 requirements.txt         # Python dependencies
├── 🔐 .env.example             # Environment variables template
└── 📖 README.md                # This file
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip / venv

### 1. Clone the Repository

```bash
git clone https://github.com/mandira15/Hormuz-SentinelX.git
cd Hormuz-SentinelX
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
# Edit .env with your settings (optional — works in mock mode by default)
```

### 5. Run the Server

```bash
uvicorn src.main:app --reload --port 8000
```

### 6. Open the Dashboard

```
http://localhost:8000
```

> **💡 Note**: The platform runs in **mock/simulated mode** out-of-the-box with no external data connections required. All scenario data is generated internally.

---

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)

```bash
git clone https://github.com/mandira15/Hormuz-SentinelX.git
cd Hormuz-SentinelX
docker-compose up --build
# Access at http://localhost:8000
```

### Using Docker directly

```bash
docker build -t hormuz-sentinelx .
docker run -p 8000:8000 hormuz-sentinelx
```

### One-Click Deploy to Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/mandira15/Hormuz-SentinelX)

---

## 📡 Data Sources & References

| Source | Data Used |
|---|---|
| **IEA (International Energy Agency)** | Global oil flow statistics, Hormuz throughput volumes |
| **MoPNG (Ministry of Petroleum & Natural Gas)** | India's petroleum policy & SPR facility data |
| **PPAC (Petroleum Planning & Analysis Cell)** | Fuel price baselines, import dependency ratios |
| **IMF World Economic Outlook 2024** | GDP impact coefficients, CPI elasticity factors |
| **EIA (U.S. Energy Information Administration)** | Brent crude price scenarios & forecasts |
| **Leaflet / OpenStreetMap** | Geospatial map tiles for Hormuz region |

> ⚠️ **Disclaimer**: All economic impact figures are simulation estimates based on published models and research. This is a decision-support tool, not a financial or policy directive.

---

## 🗺️ Roadmap

- [x] Core 3-column military command dashboard
- [x] 3-scenario engine (30% Partial / 60% Severe / 100% Full Blockade)
- [x] Interactive Leaflet.js strategic map with shipping lane overlays
- [x] Economic Shock Index arc gauge (0–100)
- [x] AI Executive Situation Brief (typewriter animation)
- [x] National Resilience Radar chart (6-axis)
- [x] Supply Chain Cascade Timeline
- [x] Import Dependency Sankey diagram
- [x] Emergency Protocol Mode (FUEL-RED)
- [x] Docker & Render cloud deployment
- [ ] 🔜 Live AIS ship tracking integration
- [ ] 🔜 Real-time Brent crude price API feed
- [ ] 🔜 LLM integration for dynamic AI briefs (GPT-4o / Gemini)
- [ ] 🔜 Multi-country impact analysis (Pakistan, China, EU)
- [ ] 🔜 PDF export of executive situation reports
- [ ] 🔜 WebSocket-based live data push
- [ ] 🔜 Historical scenario playback

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'feat: add your feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a **Pull Request**

Please ensure your PR:
- Follows existing code style
- Includes appropriate tests in `/tests`
- Updates this README if needed

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Mandira** — [@mandira15](https://github.com/mandira15)

---

<div align="center">

**⭐ Star this repo if you find it useful!**

[![GitHub stars](https://img.shields.io/github/stars/mandira15/Hormuz-SentinelX?style=social)](https://github.com/mandira15/Hormuz-SentinelX/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/mandira15/Hormuz-SentinelX?style=social)](https://github.com/mandira15/Hormuz-SentinelX/network/members)

*Built with 🛡️ for India's energy security*

</div>
