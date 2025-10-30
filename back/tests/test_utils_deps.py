import pytest
from fastapi import HTTPException
from app.utils.deps import get_bearer

def test_get_bearer_ok():
    token = get_bearer("Bearer abc.def.ghi")
    assert token == "abc.def.ghi"

@pytest.mark.parametrize("hdr", ["", "Bearer", "Token abc", "bearer", None])
def test_get_bearer_missing(hdr):
    with pytest.raises(HTTPException) as ei:
        get_bearer(hdr)  # type: ignore[arg-type]
    assert ei.value.status_code == 401
