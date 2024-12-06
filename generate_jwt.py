import time
from jwt import encode
from config import SUBJECT, NAME, X_API_KEY, ALGORITHM, PRIVATE_KEY

def generate_jwt(subject, name, x_api_key, private_key, algorithm="RS256"):
    """
    Generate a JWT token with the specified parameters
    
    Args:
        subject (str): Subject of the token
        name (str): Name in the token
        x_api_key (str): API key to include in token
        private_key (str): Private key for signing
        algorithm (str, optional): Algorithm to use. Defaults to "RS256"
    
    Returns:
        str: Generated JWT token
    """
    # Create payload
    payload = {
        "sub": subject,
        "name": name,
        "iat": int(time.time()),  # Current time
        "x-api-key": x_api_key
    }

    # Generate JWT token using specified algorithm
    token = encode(
        payload,
        private_key,
        algorithm=algorithm
    )

    return token

if __name__ == "__main__":
    # Use values from config
    token = generate_jwt(
        subject=SUBJECT,
        name=NAME,
        x_api_key=X_API_KEY,
        private_key=PRIVATE_KEY,
        algorithm=ALGORITHM
    )
    print("\nGenerated JWT Token:")
    print(token)
