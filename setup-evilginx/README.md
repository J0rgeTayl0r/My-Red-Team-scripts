
# Setup Evilginx Automation Script

Automates the installation and initial configuration of **Evilginx3** on a VPS. Designed for ethical red team exercises and lab environments.

---

## Usage

Make the script executable and run it with your domain and public IP as arguments:

```bash
chmod +x setup-evilginx.sh
sudo ./setup-evilginx.sh <domain> <public-ip>
Example
bash
Copy
Edit
sudo ./setup-evilginx.sh example.com 1.1.1.1
What the Script Does
Prepares the system (installs dependencies if needed).

Downloads and unzips the latest Evilginx release.

Sets executable permissions on the binary.

Configures your domain and public IP.

Optionally provides reminders to check DNS and firewall settings.

Notes
Ensure ports 80 and 443 are open on your VPS.

For TLS support, make sure your DNS records point correctly to your VPS.

The script is designed for non-interactive usage (fully automated).

Tips
Use environment variables or command-line arguments to easily reuse the script with different domains.

Keep your phishlets and redirectors directories organized in the same folder as the script.

This is intended for ethical testing only! Never target live users without permission.

