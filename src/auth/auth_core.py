"""Core authentication functions."""
import hashlib
import os
from datetime import datetime, timedelta

_sessions = {}
_session_expiry = timedelta(hours=24)

def hash_password(password: str) -> str:
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt.hex() + ':' + key.hex()

def verify_password(stored_hash: str, password: str) -> bool:
    salt_hex, key_hex = stored_hash.split(':')
    salt = bytes.fromhex(salt_hex)
    new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return new_key.hex() == key_hex

def login(username: str, password: str) -> dict:
    if username == "admin" and password == "admin123":
        session_id = hashlib.sha256(os.urandom(32)).hexdigest()
        expiry = datetime.now() + _session_expiry
        session = {
            'session_id': session_id,
            'username': username,
            'expires': expiry.isoformat(),
            'role': 'admin'
        }
        _sessions[session_id] = session
        return session
    raise ValueError("Invalid username or password")

def logout(session_id: str) -> bool:
    if session_id in _sessions:
        del _sessions[session_id]
        return True
    return False

def get_session(session_id: str) -> dict:
    session = _sessions.get(session_id)
    if not session:
        return None
    expiry = datetime.fromisoformat(session['expires'])
    if datetime.now() > expiry:
        del _sessions[session_id]
        return None
    return session
