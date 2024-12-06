# Machine learning part
In the first part, I needed to find the correct dataset for training. For this model, I used a small amount of data downloaded from Google Images. Here, I only classified 5 popular persons in the world. If you need to classify more people or complex features, you can use a much larger dataset and a bigger model.

Secondly, I carried out data preprocessing and feature engineering tasks:
- Removing unclear images, such as when the face is not clearly visible.
- Cropping the face and saving the image.
For cropping, I used OpenCV's CascadeClassifier, which has pre-trained eye and face detectors. Using this, I detected faces and identified the eyes. If the eyes were not clearly visible, I removed those images from the dataset.

In the feature engineering part, I vertically stacked RGB channels and wavelet-transformed grayscale images of the original images. This contains a lot of valuable information about the image. In simple terms, it is similar to a Fourier transform, as it detects various features and how the image is built.

Using the above-stacked images, the training process was carried out.

## UI Design
An HTML/CSS/JavaScript-based UI is designed. In the UI, you can drag and drop an image, and it will show you the probabilities of who is most likely in the given image.

The drag-and-drop feature works using the Dropzone.js JavaScript and CSS library. The uploaded image is transformed into a Base64 text format, and at the backend, we need to re-transform the image back into its original format.

# server desing
A Flask server is used to develop the server setup. The server folder contains the previously trained model, server files, and utility files. The utility files contain all the necessary tools for the inference.


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
















