#Setup Evilginx Automation Script

Automates the installation and initial configuration of Evilginx3 on a VPS. Designed for ethical red team exercises and lab environments. 

##Usage

Run the script with domain and public IP as arguments:

chmod +x setup-evilginx.sh
sudo ./setup-evilginx.sh <domain> <public-ip>


##Example:

sudo ./setup-evilginx.sh example.com 1.1.1.1


##The script will:

Prepare the system (install dependencies if needed).

Download and unzip the latest Evilginx release.

Set executable permissions on the binary.

Configure your domain and public IP.

Optionally provide reminders to check DNS and firewall settings.

##Notes

Ensure ports 80 and 443 are open on your VPS.

For TLS support with your domain, make sure DNS records point correctly.

The script is designed for non-interactive usage (fully automated).

##Tips

Use environment variables or command-line arguments to easily reuse the script with different domains.

Keep your phishlets and redirectors directories organized in the same folder as the script.

This is intended for ethical testing only! Never target live users without permission.
