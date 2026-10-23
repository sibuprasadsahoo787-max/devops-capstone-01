#!/usr/bin/env bash

set -euo pipefail

IMAGE_NAME="devops-capstone-01:1.0"

echo "================================"
echo " DevOps Capstone - Local CI"
echo "================================"

echo
echo "Step 1: Checking Python"
python3 --version

echo
echo "Step 2: Running automated tests"
python3 -m unittest discover -s tests -v

echo
echo "Step 3: Building Docker image"
docker build -t "$IMAGE_NAME" .

echo
echo "CI PASSED: Tests and Docker build succeeded."
