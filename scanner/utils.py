import re
import json
import os
import datetime
from typing import Dict


def normalize_url(url: str) -> str:
    url = url.strip()
    if not url:
        raise ValueError("Empty URL")

    if not re.match(r"^https?://", url, re.I):
        url = "https://" + url

    return url


def extract_host(url: str) -> str:
    host = re.sub(r"^https?://", "", url, flags=re.I)
    host = host.split("/")[0]
    return host


def save_report(report: Dict, out_dir: str = "reports") -> str:
    os.makedirs(out_dir, exist_ok=True)

    timestamp = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    filename = f"scan_report_{timestamp}.json"
    path = os.path.join(out_dir, filename)

    with open(path, "w") as f:
        json.dump(report, f, indent=2)

    return path
