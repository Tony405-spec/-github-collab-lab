"""Authentication module for GitHub Learning Lab."""
from .auth_core import login, logout, hash_password, verify_password
__all__ = ['login', 'logout', 'hash_password', 'verify_password']
