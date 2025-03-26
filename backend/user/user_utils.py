from passlib.context import CryptContext

# Create a password context for bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    """Verify a plain password against a hashed password."""
    try:
        return pwd_context.verify(plain, hashed)
    except Exception as e:
        # Log the error in a production environment
        print(f"Error verifying password: {e}")
        return False
