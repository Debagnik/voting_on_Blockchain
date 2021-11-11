import hashlib
import os
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def get_key_pair(key_size=512):
    """
    Returns (public key, private key) pair with default key size of 512 bytes.
    """
    private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )
    public_key = private_key.public_key()
    return public_key, private_key


def sign(message, private_key):
    
    if type(message) == str:
        message = message.encode()

    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature


def verify_signature(message, signature, public_key):
    
    if type(message) == str:
        message = message.encode()
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
    except InvalidSignature as e:
        raise e
    except Exception as e:
        raise Exception('Unexpected error: {}'.format(e))


def get_str_hash(s):
    m = hashlib.sha256()
    m.update(s.encode())
    return m.hexdigest()


def get_formatted_time_str(date_obj):
    
    return date_obj.strftime("%Y-%m-%d %H:%M")


def get_input_of_type(message, expected_type, allowed_inputs=None):
    
    while True:
        try:
            user_input = expected_type(input(message))
            if allowed_inputs:
                if user_input in allowed_inputs:
                    break   # correct input type and part of allowed inputs
                print('Unexpected input')
                continue
            break
        except (ValueError, TypeError):
            print("Wrong type of input")
    return user_input


def clear_screen():
    """Clears terminal screen"""
    os.system('cls||clear')