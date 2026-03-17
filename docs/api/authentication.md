# Authentication API Documentation

## Functions
- `hash_password(password)`: Hashes a password
- `verify_password(stored_hash, password)`: Verifies a password
- `login(username, password)`: Authenticates a user
- `logout(session_id)`: Ends a session
- `get_session(session_id)`: Gets session info

## Example
```python
from src.auth import login, logout

try:
    session = login("admin", "admin123")
    print(f"Logged in as {session['role']}")
    logout(session['session_id'])
except ValueError as e:
    print(f"Login failed: {e}")

