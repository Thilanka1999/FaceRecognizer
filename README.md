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


