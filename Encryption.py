import secrets
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Encrypt:
    _backend = default_backend()
    _iterations = 100_000

    def __init__(self, master_password:str) -> None:
        self._password: bytes = master_password.encode()        
        self._salt = secrets.token_bytes(16)
        self._key = self._derive_key(self._salt)


    def _derive_key(self, salt: bytes) -> bytes:
        """Derive a secret key from a given password and salt"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(), length=32, salt=salt,
            iterations=self._iterations, backend=self._backend)
        return b64e(kdf.derive(self._password))

    def encrypt(self, data: bytes) -> bytes:
        return b64e(b'%b%b%b' % (self._salt, self._iterations.to_bytes(4, 'big'), b64d(Fernet(self._key).encrypt(data))))

    def decrypt(self, encrypted_message: bytes) -> str:
        decoded = b64d(encrypted_message)
        salt, iter, encrypted_message = decoded[:16], decoded[16:20], b64e(decoded[20:])
        iterations = int.from_bytes(iter, 'big')
        key = self._derive_key(salt)
        try:
            Buffer =  Fernet(key).decrypt(encrypted_message)
            return Buffer
        except InvalidToken:
            return ""
        