# Zero Trust Architecture Assessor

<p align="center">
  ![Stars](https://img.shields.io/github/stars/ridhinva/zero-trust-assessor?style=for-the-badge)
  ![Forks](https://img.shields.io/github/forks/ridhinva/zero-trust-assessor?style=for-the-badge)
  ![Issues](https://img.shields.io/github/issues/ridhinva/zero-trust-assessor?style=for-the-badge)
  ![License](https://img.shields.io/github/license/ridhinva/zero-trust-assessor?style=for-the-badge)
  ![Last Commit](https://img.shields.io/github/last-commit/ridhinva/zero-trust-assessor?style=for-the-badge)
  ![Build Status](https://img.shields.io/github/actions/workflow/status/ridhinva/zero-trust-assessor/ci.yml?style=for-the-badge)
  ![Zero Trust](https://img.shields.io/badge/Zero%20Trust-Architecture%20Assessment-critical?style=for-the-badge)
  ![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
</p>

---

## 🎯 Overview

**Zero Trust architecture assessment tool** validating ZTNA config, device posture, microsegmentation, continuous verification, and identity-aware proxy deployment.

| Check | Severity | Description |
|-------|----------|-------------|
| ZTNA Configuration | 🔴 CRITICAL | Tailscale, Twingate, Cloudflare Access, Zscaler ZPA |
| Device Posture Assessment | 🟠 HIGH | CrowdStrike, SentinelOne, Kolide integration |
| Identity-Aware Proxy | 🟠 HIGH | Google IAP, AWS Verified Access, Azure App Proxy |
| Microsegmentation | 🟠 HIGH | Illumio, Guardicore, Calico, Cilium |
| Continuous Verification | 🟡 MEDIUM | Behavioral biometrics, risk-based MFA |
| mTLS Everywhere | 🟡 MEDIUM | Service mesh, WireGuard, IPsec |
| Software-Defined Perimeter | 🟡 MEDIUM | SDP controller/gateway validation |
| Legacy App Compatibility | 🟡 MEDIUM | VPN fallback, app modernization gaps |


---

## 🚀 Quick Start

```bash
git clone https://github.com/ridhinva/zero-trust-assessor.git
cd zero-trust-assessor
pip install requests pyyaml
python3 zero_trust_assessor.py --config zt-config.yaml --mode assess
```

---

## ⚖️ Disclaimer

For authorized security assessment only.
