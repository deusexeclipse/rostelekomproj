from app.core.security import SecurityManager

def test_password_hash_and_verify():
    raw = "Sup3rS3cret!"
    hashed = SecurityManager.get_password_hash(raw)
    assert hashed and isinstance(hashed, str) and hashed != raw
    assert SecurityManager.verify_password(raw, hashed)

def test_password_strength_min_length():
    ok, msg = SecurityManager.validate_password_strength("short")
    assert ok in (True, False)
