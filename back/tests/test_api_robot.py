import pytest
from httpx import AsyncClient, ASGITransport
from datetime import datetime
from main import app

@pytest.mark.asyncio
async def test_robot_data_ingest(client):
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        payload = {
            "robot_id": "RB-668",
            "timestamp": datetime.now().isoformat()+"Z",
            "location": {"zone":"A","row":1,"shelf":2},
            "scan_results": [
                {"product_id":"SKU1","quantity":5,"status":"OK"},
                {"product_id":"SKU2","quantity":0,"status":"CRITICAL"}
            ],
            "battery_level": 88.5,
            "next_checkpoint": "Z9"
        }
        r = await ac.post("/api/robots/data", json=payload, headers={"Authorization: Bearer token RB-668"})
        assert r.status_code in (200, 201, 202)
        data = r.json()
        assert "detail" in data
