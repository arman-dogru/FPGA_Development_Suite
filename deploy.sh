#!/bin/bash

# Upgrade pip and setuptools
pip install --upgrade pip setuptools

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Install Netlify CLI
npm install -g netlify-cli

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
