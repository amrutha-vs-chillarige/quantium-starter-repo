#!/bin/bash

# Activate virtual environment
source .venv/Scripts/activate

# Run tests
pytest

# Capture exit code
EXIT_CODE=$?

# Exit with same code
if [ $EXIT_CODE -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Tests failed."
    exit 1
fi