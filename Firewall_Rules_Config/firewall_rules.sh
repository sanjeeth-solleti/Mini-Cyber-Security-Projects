#!/bin/bash

echo "[*] Enabling UFW Firewall..."
sudo ufw enable

echo "[*] Setting default policies..."
sudo ufw default deny incoming
sudo ufw default allow outgoing

echo "[*] Allowing essential ports..."
sudo ufw allow 22     # SSH
sudo ufw allow 80     # HTTP
sudo ufw allow 443    # HTTPS

echo "[*] Blocking vulnerable ports..."
sudo ufw deny 23      # Telnet
sudo ufw deny 445     # SMB

echo "[*] Limiting SSH brute-force attempts..."
sudo ufw limit ssh/tcp

echo "[*] Enabling logging..."
sudo ufw logging on

echo "[*] Current firewall status:"
sudo ufw status verbose

