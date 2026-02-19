#!/bin/bash

echo "Setting up The Singularity Framework..."

# Create necessary directories
mkdir -p data reports temp engines protocols

# Install Python dependencies
pip3 install -r requirements.txt

# Compile Go components (if Go is available)
if command -v go &> /dev/null; then
    echo "Compiling Go scraper..."
    cd engines
    go build -o scraper scraper.go
    cd ..
else
    echo "Go not found - using Python fallback for scraping"
fi

# Compile Rust components (if Rust is available)
if command -v cargo &> /dev/null; then
    echo "Compiling Rust correlator..."
    cd engines/correlator
    cargo build --release
    cd ../..
else
    echo "Rust not found - using Python fallback for correlation"
fi

# Set executable permissions
chmod +x main.py
chmod +x setup.sh

echo "Setup complete! Run with: python3 main.py"