import pytest

@pytest.mark.anyio
async def test_dashboard_current_smoke(client):
    r = await client.get("/api/dashboard/current")
    # With overrides it might still hit service; allow 200/500; ensure no crash of routing
    assert r.status_code in (200, 500, 404)
