import requests
from typing import Dict

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-XSS-Protection",
    "X-Content-Type-Options",
]


def check_security_headers(url: str) -> Dict:
    result = {"url": url, "checked": [], "missing": []}

    try:
        r = requests.get(url, timeout=8)
        headers = {k.title(): v for k, v in r.headers.items()}

        for h in SECURITY_HEADERS:
            present = h in headers
            result["checked"].append({
                "header": h,
                "present": present,
                "value": headers.get(h)
            })
            if not present:
                result["missing"].append(h)

        result["status_code"] = r.status_code

    except Exception as e:
        result["error"] = str(e)

    return result
