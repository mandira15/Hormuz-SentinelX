"""Entry point: run AIS collector, analytics engine, and web server concurrently."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import logging

import uvicorn

from src.analytics import transit_detection_loop
from src.collector import collect

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)


async def run_server():
    """Run FastAPI server."""
    port = int(os.environ.get("PORT", 8002))
    config = uvicorn.Config("src.api:app", host="0.0.0.0", port=port, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


async def main():
    """Run collector, analytics, and web server in parallel."""
    await asyncio.gather(
        collect(),
        run_server(),
        transit_detection_loop(interval_sec=300),
    )


if __name__ == "__main__":
    asyncio.run(main())

