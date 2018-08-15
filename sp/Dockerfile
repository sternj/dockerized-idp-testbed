FROM unicon/shibboleth-sp

RUN yum -y update \
    && yum -y install php mod_ssl httpd-devel git gcc

RUN git clone https://github.com/unbit/uwsgi.git
WORKDIR uwisgi/apache2
RUN apxs -i -c /uwsgi/apache2/mod_proxy_uwsgi.c
WORKDIR /
RUN rm -rf uwsgi

COPY etc-shibboleth /etc/shibboleth/
COPY etc-httpd/ /etc/httpd/
COPY var-www-html/ /var/www/html/

