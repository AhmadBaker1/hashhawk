import re 

# Map of algorithm names to their regex patterns
HASH_PATTERNS = {
    'md5': re.compile(r'^[a-f0-9]{32}$'), # 32 hex characters 
    'sha1': re.compile(r'^[a-f0-9]{40}$'), # 40 hex characters
}

def detect_hash_type(hash_str: str) -> str:
    """
    Examine the input string and match it against known hash patterns.
    Returns the name of the hash algorithm if a match is found like  (e.g., 'md5', 'sha1'), 
    otherwise raise ValueError.
    """
    for name, pattern in HASH_PATTERNS.items():
        if pattern.match(hash_str.lower()):
            return name
        
    # If no match is found, raise an error
    raise ValueError(f"Unknown hash type for hash: {hash_str}")