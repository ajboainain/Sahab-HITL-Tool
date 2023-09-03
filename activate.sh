#!/bin/bash

VENV_PATH="venv/Scripts/activate"

if [ -f "$VENV_PATH" ]; then
    source "$VENV_PATH"
    echo "Virtual environment activated."
else
    echo "Virtual environment not found at '$VENV_PATH'. Please check the path"
fi