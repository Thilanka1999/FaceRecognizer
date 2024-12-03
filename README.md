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


