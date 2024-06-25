#!/bin/bash

# Ensure we're using a compatible Python version
pyenv install 3.8.12
pyenv global 3.8.12

# Upgrade pip and setuptools
pip install --upgrade pip setuptools

# Install SIP manually
pip install sip==6.6.2

# Install the other dependencies
pip install -r requirements.txt

# Package the application
echo "Packaging FPGA Development Suite..."
mkdir -p dist/FPGA_Development_Suite
cp -r src dist/FPGA_Development_Suite/
cp -r docs dist/FPGA_Development_Suite/
cp README.md dist/FPGA_Development_Suite/
cp setup.py dist/FPGA_Development_Suite/

# Deploy to Netlify
echo "Deploying FPGA Development Suite..."
netlify deploy --dir=dist/FPGA_Development_Suite --prod
