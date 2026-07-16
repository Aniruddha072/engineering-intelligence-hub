import pytest
from eih.main import health_check


@pytest.mark.asyncio
async def test_health_check() -> None:
    result = await health_check()

    assert result == {
        "status": "healthy",
        "service": "Engineering Intelligence Hub",
    }