# 🛡️ Hormuz Maritime Intelligence Platform (Hormuz-SentinelX)

An AI-powered, real-time energy security and macroeconomic risk intelligence platform monitoring the **Strait of Hormuz** chokepoint. Built for India's Ministry of Petroleum & Natural Gas and the Petroleum Planning & Analysis Cell (PPAC) to analyze crude oil supply resilience, freight premiums, and macroeconomic shocks during chokepoint disruptions.

## 🚀 One-Click Deployment

Deploy the platform instantly to your preferred cloud provider:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://hormuz-sentinelx.onrender.com/)

---

## 🌟 Key Features

* **Interactive Live Map**: Real-time tracking of maritime traffic around the Strait of Hormuz, Fujairah, and Dubai approach routes using Leaflet.
* **Resilience Scenarios**: Toggle between different levels of Hormuz closure (30% Partial, 60% Severe, 100% Full Blockade) to see real-time updates.
* **National Resilience Gauges**: Dynamic visualization of India's Strategic Petroleum Reserve (SPR) cover, Economic Shock Index (ESI), and supply gaps.
* **Macroeconomic Simulation**: Predicts Brent crude spikes, India petrol/diesel price impacts, GDP contraction risk, and CPI inflation spikes.
* **AI Situation Brief**: Provides an automated executive briefing analyzing current conditions, resilience metrics, and recommended actions.
* **Stand-alone Architecture**: Runs completely out-of-the-box in simulated/mock mode if external data streams are not connected.

---

## 🛠️ Tech Stack

* **Backend**: Python 3.11/3.12, FastAPI, Uvicorn, Asyncio, aiosqlite
* **Frontend**: HTML5, Vanilla CSS, JS/ES6, Leaflet.js for interactive mapping, Chart.js/Canvas for resilience radars
* **Data & Analytics**: Shapely (polygon-based land masking), Pandas, Matplotlib, Numpy (reporting engine)

---

## ⚙️ Environment Variables

Configure these environment variables in your deployment dashboard to unlock full functionality:

| Environment Variable | Description | Default | Required |
| --- | --- | --- | --- |
| `PORT` | The port the web server listens on. | `8002` | No (Cloud platforms set this automatically) |
| `AISSTREAM_API_KEY` | API Key from [aisstream.io](https://aisstream.io) for live AIS tracking. | *None* | No (Falls back to Mock/Simulation mode if not provided) |
| `GROQ_API_KEY` | API Key from Groq for running the AI Agent analysis. | *None* | No |
| `REDIS_HOST` | Hostname for Redis cache. | `localhost` | No |
| `REDIS_PORT` | Port for Redis cache. | `6379` | No |

---

## 💻 Local Development

### 1. Clone the repository
```bash
git clone https://github.com/mandira15/Hormuz-SentinelX.git
cd Hormuz-SentinelX
```

### 2. Set up virtual environment & install dependencies
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Run the application
```bash
python src/main.py
```
Open `http://localhost:8002` in your browser.

---

## 📦 Docker Deployment

You can build and run the platform locally using Docker:

```bash
# Build the Docker image
docker build -t hormuz-sentinelx .

# Run the container
docker run -p 8002:8002 --env-file .env hormuz-sentinelx
```

Or run the full stack (including Database & Redis) with Docker Compose:
```bash
docker-compose up --build
```
