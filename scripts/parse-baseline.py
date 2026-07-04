#!/usr/bin/env python3
"""
Parses SCAN-RESULTS.md to extract baseline vulnerability count (critical + high).

For npm audit format.

Usage:
  python3 scripts/parse-baseline.py ../SCAN-RESULTS.md

Returns: integer count of critical + high vulnerabilities
"""

import sys
import re


def parse_npm_baseline(file_path):
    """Parse npm audit SCAN-RESULTS.md and count critical + high vulnerabilities."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Could not find {file_path}", file=sys.stderr)
        sys.exit(1)

    critical_count = 0
    high_count = 0

    # Count "Severity: critical" and "Severity: high" lines
    lines = content.split('\n')
    for line in lines:
        line_lower = line.lower()
        if 'severity: critical' in line_lower:
            critical_count += 1
        elif 'severity: high' in line_lower:
            high_count += 1

    total = critical_count + high_count
    return total


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/parse-baseline.py <SCAN-RESULTS.md>", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    baseline = parse_npm_baseline(file_path)
    print(baseline)
