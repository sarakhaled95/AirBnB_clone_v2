#!/usr/bin/env bash
# script that sets up your web servers for the deployment

sudo apt-get update
sudo apt-get -y install nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By $hostname;
	root   /var/www/html;
	index  index.html index.htm;
	location /hbnb_static {
		alias /data/web_static/current;
        	index index.html index.htm;
    	}
    	location /redirect_me {
        	return 301 http://github.com/sarakhaled95;
	}
	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
		internal;
	}" > /etc/nginx/sites-available/default

service nginx restart
