Firewall Rules Configuration
🔐 Overview

This project uses UFW (Uncomplicated Firewall) to secure a Linux machine by defining strict firewall rules. It blocks unnecessary services, allows only essential ports, and helps prevent unauthorized access and brute-force attacks.
🚀 Features

    ✅ Enables UFW firewall

    ✅ Sets secure defaults: deny all incoming, allow outgoing

    ✅ Allows only necessary ports: 22 (SSH), 80 (HTTP), 443 (HTTPS)

    ❌ Blocks insecure ports: 23 (Telnet), 445 (SMB)

    🚫 Limits SSH brute-force attempts

    📜 Enables logging for auditing

⚙️ Setup Instructions
🧰 Prerequisites:

    Linux OS (Ubuntu/Debian preferred)

    Sudo privileges

    Internet connection to install UFW

🛠️ Installation & Usage
Step 1: Clone the Project

git clone https://github.com/your-username/CyberSecurity_Projects.git
cd CyberSecurity_Projects/Firewall_Rules_Configuration

Step 2: Install UFW (if not installed)

sudo apt update
sudo apt install ufw -y

Step 3: Make the Script Executable

chmod +x firewall_rules.sh

Step 4: Run the Script with Admin Privileges

sudo ./firewall_rules.sh

✅ What the Script Does:

    Enables UFW (if not already enabled)

    Sets:

        Incoming traffic to deny

        Outgoing traffic to allow

    Allows:

        Port 22 (SSH)

        Port 80 (HTTP)

        Port 443 (HTTPS)

    Blocks:

        Port 23 (Telnet)

        Port 445 (SMB)

    Limits SSH brute-force attempts

    Turns on logging

    Displays current firewall status

🔍 Verify Firewall Status

After setup, run:

sudo ufw status verbose

You should see output like:

Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing)
To                         Action      From
--                         ------      ----
22                         ALLOW IN    Anywhere
80                         ALLOW IN    Anywhere
443                        ALLOW IN    Anywhere
23                         DENY IN     Anywhere
445                        DENY IN     Anywhere
22/tcp                     LIMIT IN    Anywhere

📓 Notes

    To block ICMP/ping:

sudo ufw deny proto icmp

To allow SSH from only one IP:

sudo ufw allow from 192.168.1.5 to any port 22
