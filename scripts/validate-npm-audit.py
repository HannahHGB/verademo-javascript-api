#!/usr/bin/env python3
"""
Validates npm audit results against Critical/High vulnerability threshold.

Usage:
  python3 scripts/validate-npm-audit.py <audit-report.json>

Exit codes:
  0 - No critical/high vulnerabilities found
  1 - Critical/high vulnerabilities found
"""

import json
import sys


def validate_npm_audit(report_path):
    """Parse npm audit JSON report and check for critical/high vulnerabilities."""
    try:
        with open(report_path, 'r') as f:
            audit_data = json.load(f)
    except FileNotFoundError:
        print(f"❌ Could not find audit report at {report_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"❌ Could not parse {report_path} as JSON")
        sys.exit(1)

    # Extract vulnerability counts from metadata
    metadata = audit_data.get('metadata', {})
    vulnerabilities = metadata.get('vulnerabilities', {})

    critical = vulnerabilities.get('critical', 0)
    high = vulnerabilities.get('high', 0)
    moderate = vulnerabilities.get('moderate', 0)
    low = vulnerabilities.get('low', 0)

    print("\n🔍 npm audit Vulnerability Summary:")
    print(f"  🔴 Critical: {critical}")
    print(f"  🟠 High:     {high}")
    print(f"  🟡 Moderate: {moderate}")
    print(f"  🔵 Low:      {low}")

    total_critical_high = critical + high

    if total_critical_high > 0:
        print(f"\n❌ Found {total_critical_high} critical/high vulnerabilities that need fixing.")
        print("Check SCAN-RESULTS.md for the recommended fixes.")
        return False
    else:
        print(f"\n✅ No critical or high vulnerabilities detected!")
        return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/validate-npm-audit.py <audit-report.json>")
        sys.exit(1)

    report_path = sys.argv[1]
    success = validate_npm_audit(report_path)
    sys.exit(0 if success else 1)
