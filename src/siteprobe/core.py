from urllib.parse import urlparse

def host(url: str) -> str:
    return urlparse(url).hostname or ""

def status_family(status: int) -> str:
    return f"{int(status) // 100}xx" if 100 <= int(status) < 600 else "unknown"
