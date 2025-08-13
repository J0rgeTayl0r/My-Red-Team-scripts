# PhishPrep - Automated GoPhish Deployment Script

PhishPrep is an automated deployment script for setting up GoPhish, the phishing framework.  
This tool automates system updates, GoPhish download, SSL certificate generation via Certbot (manual DNS challenge), and config updates, making it easy to spin up a phishing lab quickly.

## What it does

PhishPrep automates setting up a GoPhish phishing platform with SSL. It:
- Updates and upgrades your Ubuntu server.
- Installs required packages: unzip, certbot.
- Downloads and extracts the latest GoPhish release.
- Runs Certbot manual DNS challenge with a **3-minute fixed wait** for DNS TXT propagation.
- Automatically updates GoPhish's config.json with the generated SSL certificate paths.
- Optionally launches GoPhish (use `--real` flag to actually start it).
- Prints access info and tips.


## Features

- Automated system update and package installation (unzip, certbot)  
- Downloads and extracts the latest GoPhish binary  
- Generates SSL certificates using Certbot manual DNS challenge  
- Automatically updates GoPhish `config.json` with proper listen URL and SSL cert paths  
- Safe-by-default mode prevents accidental GoPhish launch  
- `--real` mode flag to launch GoPhish after deployment   



## Requirements

- Ubuntu or Debian-based Linux server (tested on Ubuntu 20.04+)  
- Root or sudo privileges  
- Domain name pointing to your server for the SSL certificate  
- Certbot installed via script 
- Internet access to download GoPhish and Certbot packages  


## Usage

1. Clone or download the repository  
2. Make the script executable:  
    ```bash
    chmod +x phishprep.py
    ```  
3. Run the script:  
    - Dry run (safe mode, does not launch GoPhish):  
      ```bash
      sudo ./phishprep.py
      ```  
    - Real deployment (launches GoPhish after setup):  
      ```bash
      sudo ./phishprep.py --real
      ```  
4. Follow the prompts, especially for DNS TXT record creation when Certbot asks  
5. After completion, access your GoPhish admin panel at:  
 ```
    https://your-domain:3333  
   ```



## Notes

- The script uses Certbot with `--manual --preferred-challenges dns` so you will have to add DNS TXT records yourself manually during cert generation.  
- Auto-renewal of certificates is **not** configured, you will need to manually renew certificates before expiry.  
- The GoPhish launch command is disabled by default for safety and public repo reasons. Use `--real` to enable it.  
- This script is intended for educational, research, and red team training purposes only. Use responsibly and ethically.  



## License

MIT License 



## Author

Jorge Taylor AkA L0rdV0ld3m0rt - Red Team Edition.  Inspired by Tyler Ramsbey, during his Hands-On Phishing, which I definitely recommend EVERYONE take the course its great. HACK THE PLANET! 



## Disclaimer

This project is designed for authorized security research and educational use only. Unauthorized use against targets without consent is illegal and unethical.
