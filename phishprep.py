#!/usr/bin/env python3
import os
import json
import subprocess
import time
import sys
import random

RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def banner():
    print(f"{BOLD}{RED}\
 ██▓███   ██░ ██  ██▓  ██████  ██░ ██  ██▓███   ██▀███  ▓█████  ██▓███  \n\
▓██░  ██▒▓██░ ██▒▓██▒▒██    ▒ ▓██░ ██▒▓██░  ██▒▓██ ▒ ██▒▓█   ▀ ▓██░  ██▒\n\
▓██░ ██▓▒▒██▀▀██░▒██▒░ ▓██▄   ▒██▀▀██░▓██░ ██▓▒▓██ ░▄█ ▒▒███   ▓██░ ██▓▒\n\
▒██▄█▓▒ ▒░▓█ ░██ ░██░  ▒   ██▒░▓█ ░██ ▒██▄█▓▒ ▒▒██▀▀█▄  ▒▓█  ▄ ▒██▄█▓▒ ▒\n\
▒██▒ ░  ░░▓█▒░██▓░██░▒██████▒▒░▓█▒░██▓▒██▒ ░  ░░██▓ ▒██▒░▒████▒▒██▒ ░  ░\n\
▒▓▒░ ░  ░ ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒▒▓▒░ ░  ░░ ▒▓ ░▒▓░░░ ▒░ ░▒▓▒░ ░  ░\n\
░▒ ░      ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░░▒ ░       ░▒ ░ ▒░ ░ ░  ░░▒ ░     \n\
░░        ░  ░░ ░ ▒ ░░  ░  ░   ░  ░░ ░░░         ░░   ░    ░   ░░       \n\
          ░  ░  ░ ░        ░   ░  ░  ░            ░        ░  ░         \n\
{RESET}")
    print("Author: Jorge Taylor AkA L0rdV0ld3m0rt")
    print("Inspired by Tyler Ramsbey — take his Hands-On Phishing course, it’s FIRE")
    print("HACK THE PLANET!\n")

    tips = [
        "🐟 Hook 'em with realism.",
        "🛡️ OpSec first. Always.",
        "📜 Logs are your paper trail — Don't forget to clear them!",
        "🚀 Automate or perish.",
    ]
    print(f"[TIP] {random.choice(tips)}\n")

def system_update():
    print("[*] Updating system packages...")
    subprocess.run(["apt", "update", "-y"])
    subprocess.run(["apt", "upgrade", "-y"])
    subprocess.run(["apt", "install", "-y", "unzip", "certbot"])

def download_gophish():
    print("[*] Downloading GoPhish...")
    os.makedirs("gophish", exist_ok=True)
    os.chdir("gophish")
    subprocess.run([
        "wget", "https://github.com/gophish/gophish/releases/download/v0.12.1/gophish-v0.12.1-linux-64bit.zip"
    ])
    subprocess.run(["unzip", "-o", "gophish-v0.12.1-linux-64bit.zip"])
    subprocess.run(["chmod", "+x", "gophish"])

def update_config(cert_path, key_path):
    print("[*] Updating config.json with SSL cert paths...")
    with open("config.json", "r") as f:
        config = json.load(f)
    config["admin_server"]["listen_url"] = "0.0.0.0:3333"
    config["admin_server"]["use_tls"] = True
    config["admin_server"]["cert_path"] = cert_path
    config["admin_server"]["key_path"] = key_path
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

def wait_fixed_time_then_continue(proc):
    wait_seconds = 180
    print(f"[*] Waiting {wait_seconds} seconds for DNS TXT record to propagate...")
    time.sleep(wait_seconds)
    print("[*] Done waiting. Pressing Enter to continue Certbot challenge...")
    proc.stdin.write("\n")
    proc.stdin.flush()

def run_certbot_with_manual_dns(domain):
    print("[*] Starting Certbot manual DNS challenge for domain:", domain)
    proc = subprocess.Popen([
        "certbot", "certonly", "-d", domain,
        "--manual", "--preferred-challenges", "dns",
        "--register-unsafely-without-email"
    ], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    wait_fixed_time_then_continue(proc)

    out, err = proc.communicate()
    print(out)
    if proc.returncode == 0:
        print("[*] Certbot finished successfully.")
    else:
        print("[!] Certbot failed or DNS propagation took longer than 3 minutes.")
        print("[!] Please rerun the script or complete the TXT record manually.")

def launch_gophish(real=False):
    print("[*] Ready to launch GoPhish...")
    if real:
        print("[*] Launching GoPhish now!")
        subprocess.run(["./gophish"])
    else:
        print("    (In a real pentest, uncomment the command below or run with --real)")
        # subprocess.run(["./gophish"])
    time.sleep(2)

def main():
    banner()
    if os.geteuid() != 0:
        print("[!] Please run as root.")
        sys.exit(1)
    real_mode = False
    if len(sys.argv) > 1 and sys.argv[1] == "--real":
        real_mode = True
    domain = input("Enter your domain name: ").strip()
    system_update()
    download_gophish()
    run_certbot_with_manual_dns(domain)
    cert_path = f"/etc/letsencrypt/live/{domain}/fullchain.pem"
    key_path = f"/etc/letsencrypt/live/{domain}/privkey.pem"
    update_config(cert_path, key_path)
    launch_gophish(real=real_mode)
    print(f"[*] Deployment complete. Access GoPhish at: https://{domain}:3333")

if __name__ == "__main__":
    main()
