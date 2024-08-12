FROM httpd:2.4.62

# Super simple dockerisation for static websites
# Contact Memphis if this file causes problems

COPY ./www/ /usr/local/apache2/htdocs/
RUN find /usr/local/apache2/htdocs/ -type d -exec chmod 755 \{\} \; &&\
    chmod -R +r /usr/local/apache2/htdocs/

EXPOSE 80
