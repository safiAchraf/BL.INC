import hashlib
import base64

def Hasher(data):
    # Create a new SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Convert the data to bytes if it's not already
    if isinstance(data, str):
        data = data.encode()

    # Update the hash object with the data
    sha256_hash.update(data)

    # Get the hash digest as bytes
    hash_digest = sha256_hash.digest()

    # Encode the hash digest using base64
    encoded_hash = base64.b64encode(hash_digest)

    # Convert the bytes to a string
    hash_string = encoded_hash.decode()

    return hash_string[:6].lower()