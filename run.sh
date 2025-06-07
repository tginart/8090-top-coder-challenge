#!/bin/bash

# This script is a simple wrapper that calls the hard-coded depth-9 decision tree.
# It takes three parameters and passes them directly to the Python script.

set -euo pipefail

if [ "$#" -ne 3 ]; then
    echo "Usage: ./run.sh <trip_duration_days> <miles_traveled> <total_receipts_amount>"
    exit 1
fi

python3 calculate.py "$1" "$2" "$3" 