"""Tests for authentication module."""
import pytest
from src.auth.auth_core import hash_password, verify_password, login, logout, get_session

class TestPasswordHashing:
    def test_hash_password_returns_string(self):
        result = hash_password("mypassword")
        assert isinstance(result, str)
        assert ":" in result
    
    def test_verify_password_success(self):
        password = "secure_password"
        hashed = hash_password(password)
        assert verify_password(hashed, password) is True
    
    def test_verify_password_failure(self):
        password = "secure_password"
        hashed = hash_password(password)
        assert verify_password(hashed, "wrong_password") is False

class TestLoginFunction:
    def test_login_success_admin(self):
        session = login("admin", "admin123")
        assert session['username'] == "admin"
        assert session['role'] == "admin"
        assert 'session_id' in session
    
    def test_login_failure_wrong_password(self):
        with pytest.raises(ValueError) as excinfo:
            login("admin", "wrong")
        assert "Invalid username or password" in str(excinfo.value)

class TestSessionManagement:
    def test_logout_removes_session(self):
        session = login("admin", "admin123")
        session_id = session['session_id']
        assert get_session(session_id) is not None
        result = logout(session_id)
        assert result is True
        assert get_session(session_id) is None
    
    def test_logout_nonexistent_session(self):
        result = logout("nonexistent")
        assert result is False
