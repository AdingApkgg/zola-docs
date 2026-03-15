#!/bin/bash

# Check if zola is installed
if ! command -v zola &> /dev/null; then
    echo "Zola not found. Installing..."
    ZOLA_VERSION="v0.22.1"
    
    # Detect OS for download
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "Detected Linux. Downloading Zola ${ZOLA_VERSION}..."
        curl -L "https://github.com/getzola/zola/releases/download/${ZOLA_VERSION}/zola-${ZOLA_VERSION}-x86_64-unknown-linux-gnu.tar.gz" | tar xz
        echo "Zola installed successfully."
        ./zola build
    else
        echo "Zola is not installed. Please install it manually."
        echo "For macOS: brew install zola"
        exit 1
    fi
else
    echo "Zola found. Building..."
    zola build
fi
