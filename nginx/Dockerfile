FROM nginx:1.24.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY project.conf /etc/nginx/conf.d
COPY nginx.conf /etc/nginx
