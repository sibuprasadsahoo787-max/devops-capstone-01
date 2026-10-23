#!/usr/bin/env bash

set -euo pipefail

echo "================================"
echo " DevOps Capstone - Local CI"
echo "================================"

echo
echo "Step 1: Checking Python version"
python3 --version

echo
echo "Step 2: Running automated tests"
python3 -m unittest discover -s tests -v

echo
echo "CI PASSED: All checks completed successfully."
