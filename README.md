# JWT Token Generator

A simple Python utility for generating JSON Web Tokens (JWT) using RS256 algorithm.

## Features

- Generate JWT tokens with customizable claims
- Support for RS256 signing algorithm
- Configurable subject, name, and API key claims
- Includes timestamp (iat) in token payload

## Requirements

- Python 3.x
- PyJWT (2.8.0)
- cryptography (41.0.4)

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `config.template.py` to `config.py` and fill in your configuration:
   ```bash
   cp config.template.py config.py
   ```

## Usage

The main script `generate_jwt.py` provides a function to generate JWT tokens. You can either import the function in your code or run the script directly:

```python
from generate_jwt import generate_jwt

token = generate_jwt(
    subject="your-subject",
    name="your-name",
    x_api_key="your-api-key",
    private_key="your-private-key"
)
```

Or run directly from command line:
```bash
python generate_jwt.py
```

## Configuration

Edit `config.py` to set your default values for:
- `SUBJECT`: The subject claim for the token
- `NAME`: The name claim for the token
- `X_API_KEY`: Your API key
- `PRIVATE_KEY`: Your RSA private key for signing
- `ALGORITHM`: The signing algorithm (defaults to RS256)
