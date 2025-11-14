import requests
from typing import Dict, List
from .utils import normalize_url

COMMON_PATHS = [
    "admin", "login", "uploads", "config.php", "phpinfo.php",
    "robots.txt", "backup", "backup.zip", "test", "server-status",
]


def enumerate_paths(url: str, paths: List[str] = None) -> Dict:
    url = normalize_url(url)

    if not url.endswith("/"):
        url += "/"

    paths = paths or COMMON_PATHS
    findings = []

    for p in paths:
        test_url = url + p

        try:
            r = requests.get(test_url, timeout=5)
            if r.status_code == 200:
                findings.append({"path": p, "url": test_url, "code": 200})
            elif r.status_code == 403:
                findings.append({"path": p, "url": test_url, "code": 403})
        except:
            pass

    return {"base": url, "findings": findings}
