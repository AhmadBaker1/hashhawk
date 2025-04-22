# hashhawk/cracker.py

import hashlib
from passlib.hash import bcrypt

def crack_md5(hash_to_crack: str, wordlist_path: str) -> str | None:
    """
    Dictionary attack via a file path.
    """
    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
        for pw in (line.strip() for line in f):
            if hashlib.md5(pw.encode()).hexdigest() == hash_to_crack:
                return pw
    return None

def crack_md5_list(hash_to_crack: str, wordlist: list[str]) -> str | None:
    """
    Dictionary attack via an in-memory list of passwords.
    """
    for pw in wordlist:
        if hashlib.md5(pw.encode()).hexdigest() == hash_to_crack:
            return pw
    return None

def crack_bcrypt_list(hash_to_crack: str, wordlist: list[str]) -> str | None:
    """
    List-based bcrypt cracking using passlib.
    """
    for pw in wordlist:
        if bcrypt.verify(pw, hash_to_crack):
            return pw
    return None
