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





































This Repository contain FaceRecognition projects.



# AWS

I have tested this deployemnt on ubuntu ec2 instance. creating instence and connecting with it from your computer throug the ssh protocol is straight forward.
after conneting with it. first you can install nginx on the server. you can do the following command 
sudo apt-get update
sudo apt-get install nginx (automatically start nginx server)

these command wil helpfull for the work with nginx
sudo service nginx start
sudo service nginx stop
sudo service nginx restart


nginx will be located in /etc/nginx folder.

in there there will be the nginx.conf file inside the nginx it has "include /etc/nginx/sites-enabled/"
this entry so default nginx rendering page should locate inside the site-enable. if you cd into it you will see there is default file it is symbolic link to the site-available directory.
so we can following .config file save inside the site-available directory and linked it to site-enable. 

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

this will redirect the /api/ traffic to 5000 port and it will render the app.html page inside the root directorty when it call.



#Flask

we need to run Flask server at the backend to make the prediction. so python packages should be properly installed.
in newer version of ubuntu there is problem. From Ubuntu 23.04 you may encounter a new error in Python due to a change in the package installation policy that prevents packages installed through pip from colliding in any way with those installed with APT.

sudo apt install python3-venv
python3 -m venv .venv
user@server# ls .venv/
source .venv/bin/activate
pip install openai

you need to create vertual envirenmont to run the pythnon thing

after that cd to the server directory, run the server by puting python server.py

this will actvate the Flask server at port 5000 in here it will lisntening to /api/ addresses. andif get the data it will run the model and responded the prediction result.


