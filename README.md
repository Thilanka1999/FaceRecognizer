# Deployment on Ubuntu EC2 Instance

## Overview
This deployment has been tested on an Ubuntu EC2 instance. Setting up the instance and connecting to it using SSH is a straightforward process.

## Steps for Nginx Installation and Setup

1. **Update the Package List**  
   Run the following command to update the package list:
   ```bash
   sudo apt-get update

2. **nstall Nginx**
  Install Nginx using the following command:
    ```bash
    sudo apt-get install nginx

3. **Manage Nginx Service**
    Use the following commands to manage the Nginx service:
   ```bash
   sudo service nginx start
   sudo service nginx stop
   sudo service nginx restart

4. **Nginx configuration is located at /etc/nginx/.**
    Within the nginx.conf file, there is an entry:
   ```bash
   include /etc/nginx/sites-enabled/*

default Nginx rendering page is defined in the /etc/nginx/sites-enabled/ directory.
5. ** To configure a custom server: **
- Navigate to /etc/nginx/sites-available/ and create a new .conf file. For example:
    ```bash
      sudo vim /etc/nginx/sites-available/fd.conf
- add following configuaration:
   ```bash
   server {
    listen 80;
    server_name FD;
    root /home/ubuntu/FaceRecognizer/UI;
    index app.html;

    location /api/ {
        rewrite ^/api(.*) $1 break;
        proxy_pass http://127.0.0.1:5000;
    }
   }
- Link the new configuration to the sites-enabled directory:
  ```bash
  sudo ln -s /etc/nginx/sites-available/fd.conf /etc/nginx/sites-enabled/
- Test the Nginx configuration and restart the server:
  ```bash
  sudo nginx -t
  sudo service nginx restart
This configuration will serve app.html located in /home/ubuntu/FaceRecognizer/UI and route all /api/ traffic to port 5000.

# Running the Flask Backend

## Prerequisites

- Python3 and pip should be installed.
- From Ubuntu 23.04 onwards, pip-installed packages may conflict with APT-installed packages. To avoid issues, use a virtual environment.

##Steps
- Install the virtual environment package:
   ```
   sudo apt install python3-venv

- Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
- Install required Python packages:
   ```
   pip install -r requirements.txt
- Navigate to the server directory and start the Flask server:
  ```
  cd server
  python server.py
The Flask server will start on port 5000 and listen for /api/ requests.
















