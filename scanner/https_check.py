import socket
import ssl
from typing import Dict
from .utils import extract_host


def check_https(url: str) -> Dict:
    host = extract_host(url)
    result = {
        "host": host,
        "https": False,
        "cert": None,
        "error": None
    }

    try:
        ctx = ssl.create_default_context()

        with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
            s.settimeout(5)
            s.connect((host, 443))
            cert = s.getpeercert()

        result["https"] = True
        result["cert"] = {
            "subject": cert.get("subject"),
            "issuer": cert.get("issuer"),
            "notBefore": cert.get("notBefore"),
            "notAfter": cert.get("notAfter"),
        }

    except Exception as e:
        result["error"] = str(e)

    return result
