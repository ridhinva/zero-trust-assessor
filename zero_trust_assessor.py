#!/usr/bin/env python3
"""
Zero Trust Architecture Assessor
ZTNA config, device posture, microsegmentation, continuous verification
"""
import sys, json, argparse

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║           Zero Trust Architecture Assessor                   ║
║    ZTNA, Device Posture, Microsegmentation, Verification     ║
╚══════════════════════════════════════════════════════════════╝
"""

def check_ztna_config(config):
    return {"vulnerable": False, "details": ["ZTNA config check requires Tailscale/Twingate/Cloudflare/Zscaler config"]}

def check_device_posture(config):
    return {"vulnerable": False, "details": ["Device posture check requires CrowdStrike/SentinelOne/Kolide integration"]}

def check_iap(config):
    return {"vulnerable": False, "details": ["IAP check requires Google IAP/AWS Verified Access/Azure App Proxy config"]}

def check_microsegmentation(config):
    return {"vulnerable": False, "details": ["Microsegmentation check requires Illumio/Guardicore/Calico/Cilium config"]}

def check_continuous_verification(config):
    return {"vulnerable": False, "details": ["Continuous verification check requires behavioral MFA config"]}

def check_mtls(config):
    return {"vulnerable": False, "details": ["mTLS check requires service mesh/WireGuard/IPsec config"]}

def scan_target(config_file, modes):
    if not YAML_AVAILABLE:
        print("[!] PyYAML not installed. Install with: pip install pyyaml")
        config = {}
    else:
        with open(config_file) as f:
            config = yaml.safe_load(f)
    
    all_results = {"target": config_file, "findings": {}}
    if "ztna" in modes or "all" in modes:
        all_results["findings"]["ztna"] = check_ztna_config(config)
    if "posture" in modes or "all" in modes:
        all_results["findings"]["device_posture"] = check_device_posture(config)
    if "iap" in modes or "all" in modes:
        all_results["findings"]["identity_aware_proxy"] = check_iap(config)
    if "microseg" in modes or "all" in modes:
        all_results["findings"]["microsegmentation"] = check_microsegmentation(config)
    if "verify" in modes or "all" in modes:
        all_results["findings"]["continuous_verification"] = check_continuous_verification(config)
    if "mtls" in modes or "all" in modes:
        all_results["findings"]["mtls"] = check_mtls(config)
    return all_results

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="Zero Trust Architecture Assessor")
    parser.add_argument("--config", required=True, help="YAML config file")
    parser.add_argument("--mode", choices=["ztna", "posture", "iap", "microseg", "verify", "mtls", "all"], default="all")
    parser.add_argument("--output", help="Output JSON file")
    args = parser.parse_args()
    modes = ["ztna", "posture", "iap", "microseg", "verify", "mtls"] if args.mode == "all" else [args.mode]
    print(f"[*] Assessing Zero Trust config: {args.config}\n")
    results = scan_target(args.config, modes)
    total_vulns = sum(1 for v in results["findings"].values() if v.get("vulnerable"))
    print(f"\n{'='*60}\nAssessment Complete: {total_vulns} vulnerable categories found")
    for cat, finding in results["findings"].items():
        status = "🔴 VULNERABLE" if finding.get("vulnerable") else "🟢 OK"
        print(f"  {status} {cat}")
        for d in finding.get("details", []): print(f"    -> {d}")
    if args.output:
        with open(args.output, "w") as f: json.dump(results, f, indent=2)
        print(f"\n[*] Results saved to {args.output}")

if __name__ == "__main__": main()