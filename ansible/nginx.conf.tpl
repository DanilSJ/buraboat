user www-data;
worker_processes auto;
worker_priority -5;
timer_resolution 100ms;
worker_rlimit_nofile 100000;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;


events {
   worker_connections  10240;
}


http {
   include       /etc/nginx/mime.types;
   default_type  application/octet-stream;

   log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                     '$status $body_bytes_sent "$http_referer" '
                     '"$http_user_agent" "$http_x_forwarded_for"';

   access_log  /var/log/nginx/access.log  main;

   sendfile on;
   tcp_nopush on;
   tcp_nodelay on;
   keepalive_timeout 65;
   types_hash_max_size 2048;
   server_tokens off;

   ### SSL settings ###
   ssl_session_cache    shared:SSL:50m;
   ssl_session_timeout  10m;
   ssl_prefer_server_ciphers on;
   ssl_protocols TLSv1.2 TLSv1.3;
   ssl_dhparam /etc/nginx/ssl/dhparam.pem;
   ssl_ciphers 'HIGH:!aNULL:!eNULL:!EXPORT:!DES:!3DES:!RC4:!MD5:!PSK';
   
   proxy_connect_timeout           300;
   proxy_send_timeout              300;
   proxy_read_timeout              300;
   
   proxy_buffer_size               64k;
   proxy_buffers        32         64k;
   
   proxy_ignore_client_abort        on;
   
   client_max_body_size          1024m;
   
   client_body_buffer_size         64k;
   client_header_buffer_size       64k;
   large_client_header_buffers 32  64k;

   server_names_hash_bucket_size  1024;

   client_header_timeout           300;
   fastcgi_connect_timeout         300;
   fastcgi_read_timeout            300;

   fastcgi_buffer_size             64k;
   fastcgi_buffers             32  64k;

  ### Protection Clickjacking, Framesniffing, etc
   add_header X-Frame-Options SAMEORIGIN;

   gzip on;
   gzip_disable "msie6";
   gzip_vary on;
   gzip_proxied any;
   gzip_comp_level 4;
   gzip_buffers 16 8k;
   gzip_http_version 1.1;
   gzip_types text/plain text/css application/json application/x-javascript
                         text/xml application/xml application/xml+rss
                         text/javascript application/javascript image/svg+xml;

### upstream conf
   #include /etc/nginx/upstream.conf;

### vhosts conf
   #include /etc/nginx/conf.d/*.conf;
   include /etc/nginx/sites-available/*.conf;
}
