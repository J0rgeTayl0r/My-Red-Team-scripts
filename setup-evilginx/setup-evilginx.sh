#!/usr/bin/env bash
#
# setup-evilginx.sh
# Automates Evilginx installation & basic configuration
# Usage: ./setup-evilginx.sh <domain> <public-ip>
# Example: ./setup-evilginx.sh hacksmarter-manufacturing.cam 147.182.215.174
#  Made by Jorge Taylor AKA L0rdV0ld3m0rt

set -e  # Exit on error
set -u  # Error on unset variables

# --- CONFIG ---
DOMAIN=${1:-}
IP=${2:-}
WORKDIR="$HOME/evilginx"
EVILGINX_URL="https://github.com/kgretzky/evilginx3/releases/download/v3.3.0/evilginx-v3.3.0-linux-64bit.zip"

if [[ -z "$DOMAIN" || -z "$IP" ]]; then
    echo "Usage: $0 <domain> <public-ip>"
    exit 1
fi

echo "[*] Preparing system..."
sudo apt update
sudo apt install -y unzip wget curl

echo "[*] Creating working directory: $WORKDIR"
mkdir -p "$WORKDIR"
cd "$WORKDIR"

echo "[*] Downloading Evilginx..."
wget -q --show-progress "$EVILGINX_URL" -O evilginx.zip

echo "[*] Unzipping Evilginx..."
unzip -o evilginx.zip
chmod +x evilginx

echo "[*] Setting up initial configuration..."
# Launch Evilginx in background to configure it
sudo ./evilginx -p &  # Start in background with persistence enabled
EVILGINX_PID=$!
sleep 3  # Wait for Evilginx to start

echo "[*] Configuring domain and IP..."
{
    echo "config domain $DOMAIN"
    echo "config ipv4 external $IP"
    echo "config autocert on"
} | sudo ./evilginx

echo "[*] Done!"
echo "--------------------------------------------------"
echo "Next steps:"
echo "1. Point an A record for $DOMAIN to $IP"
echo "2. Allow inbound TCP 80/443 in your firewall"
echo "3. Start Evilginx: cd $WORKDIR && sudo ./evilginx"
echo "--------------------------------------------------"
