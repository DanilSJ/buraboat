upstream app_{{ name_project }} {
   server 127.0.0.1:{{ app_port }};
}

server {
    server_name {{ my_hostname }} www.{{ my_hostname }};

    listen 80;
    listen 443 ssl http2;

    ssl_certificate     /etc/letsencrypt/certs/fullchain_{{ my_hostname }};
    ssl_certificate_key /etc/letsencrypt/keys/{{ my_hostname }}.key;

    access_log  /var/log/nginx/app_{{ name_project }}-access.log;
    error_log   /var/log/nginx/app_{{ name_project }}-error.log;

    root {{ work_dir }};
   
    ### Redirect http to https
    if ( $scheme = 'http' ) {
      rewrite ^/(.*) https://$host/$1 permanent;
    }
  
    ### Redirect www to non-www
    if ($host = 'www.{{ my_hostname }}') {
      rewrite ^/(.*) https://{{ my_hostname }}/$1 permanent;
    }

   
    ### Let's Encrypt cert
    location ^~ /.well-known/acme-challenge/ {
            alias /var/www/html/.well-known/acme-challenge/;
            auth_basic off;
    }
    
    location / {
            root {{ work_dir }};
            try_files $uri @app;
            gzip_static on;
            expires max;
            add_header Cache-Control public;
    }
    
    location @app {
            proxy_pass        http://app_{{ name_project }};
            proxy_set_header  X-Real-IP  $remote_addr;
            proxy_set_header  X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header  X-Forwarded-Proto $scheme;
            proxy_set_header  Host $http_host;
            
            proxy_connect_timeout 15000;
            proxy_send_timeout 15000;
            proxy_read_timeout 15000;
            proxy_redirect    off;
            send_timeout 15000;
    }

    location /cable {
            proxy_pass http://app_{{ name_project }};
            proxy_http_version 1.1;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $http_host;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "Upgrade";
    }

}
