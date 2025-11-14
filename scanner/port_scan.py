from typing import Dict, List
from .utils import extract_host

COMMON_PORTS = [80, 443, 22, 21, 3306, 8080]


def scan_ports(url: str, ports: List[int] = None) -> Dict:
    host = extract_host(url)
    ports = ports or COMMON_PORTS

    result = {"host": host, "ports": []}

    try:
        import nmap
        nm = nmap.PortScanner()

        port_list = ",".join(str(p) for p in ports)
        scan = nm.scan(hosts=host, ports=port_list, arguments='-sS -Pn')

        if host in scan.get("scan", {}):
            tcp = scan["scan"][host].get("tcp", {})
            for p in ports:
                state = tcp.get(p, {}).get("state", "closed/filtered")
                result["ports"].append({"port": p, "state": state})
        else:
            for p in ports:
                result["ports"].append({"port": p, "state": "closed/filtered"})

    except Exception as e:
        for p in ports:
            result["ports"].append({"port": p, "state": f"error: {str(e)}"})

    return result
