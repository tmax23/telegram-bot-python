
Create DEV connection for Bot:

curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
  echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | \
  sudo tee /etc/apt/sources.list.d/ngrok.list && \
  sudo apt update && sudo apt install ngrok

ngrok authtoken <token>

sudo apt install -y nginx
sudo nano /etc/nginx/sites-enabled/mybot.conf

server {
  listen 8080;
  server_name localhost;

  location / {
    proxy_set_header Host $http_host;
    proxy_redirect off;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Scheme $scheme;
    proxy_pass http://localhost:3001/;
  }
}

ngrok http 8080
