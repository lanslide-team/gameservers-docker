#!/bin/bash


# backgrounds itself
php-fpm8.1 --fpm-config /etc/php/8.1/fpm/php-fpm.conf

exec nginx -c /etc/nginx/nginx.conf -g "daemon off;"

