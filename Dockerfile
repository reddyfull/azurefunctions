# Use the official Apache HTTP Server image as base
FROM httpd:2.4

# Remove the default Apache welcome page
RUN rm -f /usr/local/apache2/htdocs/index.html

# Copy the welcome.html file to the Apache document root
COPY ./welcome.html /usr/local/apache2/htdocs/index.html
