FROM nginx

MAINTAINER filipp218@gmail.com

COPY nginx.conf /etc/nginx/conf.d

COPY uwsgi_params /etc/nginx

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
