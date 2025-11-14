import argparse
from .utils import normalize_url, save_report
from .https_check import check_https
from .headers_check import check_security_headers
from .dir_enum import enumerate_paths
from .port_scan import scan_ports


def run_scan(target: str, out: bool = True) -> dict:
    target = normalize_url(target)
    report = {"target": target}

    report["https"] = check_https(target)
    report["headers"] = check_security_headers(target)
    report["dirs"] = enumerate_paths(target)
    report["ports"] = scan_ports(target)

    if out:
        path = save_report(report)
        report["report_file"] = path

    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Web Security Scanner")
    parser.add_argument("--url", "-u", required=True,
                        help="Target URL (example.com or https://example.com)")
    parser.add_argument("--no-report", action="store_true",
                        help="Do not save JSON report")
    args = parser.parse_args()

    result = run_scan(args.url, out=not args.no_report)

    print("--- Scan Summary ---")
    print("Target:", result["target"])

    https_info = result.get("https", {})
    if https_info.get("https"):
        print("HTTPS: enabled", https_info.get("cert", {}).get("issuer"))
    else:
        print("HTTPS: disabled or error -", https_info.get("error"))

    missing = result.get("headers", {}).get("missing", [])
    print("Missing security headers:", missing)

    dirs = result.get("dirs", {}).get("findings", [])
    print("Found directories:", [d.get("url") for d in dirs])

    ports = result.get("ports", {}).get("ports", [])
    print("Ports:", [(p.get("port"), p.get("state")) for p in ports])

    if result.get("report_file"):
        print("Report saved to:", result["report_file"])
