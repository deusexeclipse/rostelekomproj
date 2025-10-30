import pytest

@pytest.mark.anyio
async def test_health(client):
    r = await client.get("/ping/")
    assert r.status_code == 200
    assert r.json() == {"status":"ok"}
