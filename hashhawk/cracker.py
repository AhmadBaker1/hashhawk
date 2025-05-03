import re

HASH_PATTERNS = {
    'md5': re.compile(r'^[a-f0-9]{32}$'),
    'sha1': re.compile(r'^[a-f0-9]{40}$'),
    'sha256': re.compile(r'^[a-f0-9]{64}$'),
}

def detect_hash_type(hash_str: str) -> str:
    for name, pattern in HASH_PATTERNS.items():
        if pattern.match(hash_str.lower()):
            return name
    raise ValueError(f"Unknown hash format: {hash_str}")

# === hashhawk/cracker.py ===
import hashlib
from passlib.hash import bcrypt


def crack_md5_list(hash_to_crack: str, wordlist: list[str]) -> str | None:
    for pw in wordlist:
        if hashlib.md5(pw.encode()).hexdigest() == hash_to_crack:
            return pw
    return None


def crack_sha1_list(hash_to_crack: str, wordlist: list[str]) -> str | None:
    for pw in wordlist:
        if hashlib.sha1(pw.encode()).hexdigest() == hash_to_crack:
            return pw
    return None


def crack_sha256_list(hash_to_crack: str, wordlist: list[str]) -> str | None:
    for pw in wordlist:
        if hashlib.sha256(pw.encode()).hexdigest() == hash_to_crack:
            return pw
    return None


def crack_bcrypt_list(hash_to_crack: str, wordlist: list[str]) -> str | None:
    for pw in wordlist:
        if bcrypt.verify(pw, hash_to_crack):
            return pw
    return None