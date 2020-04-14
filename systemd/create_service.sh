#!/bin/bash

cp systemd/service_template dummyrest.service

# Create the folder where the application will run
sudo mkdir -p /var/run/dummyrest/logs
sudo chown -R ${USER}:${USER} /var/run/dummyrest

# Copy the configuration file to the created folder
sudo cp systemd/uwsgi.ini /var/run/dummyrest/

# Read the database url, if any
read -p "External DB? (y/N) > " ans
if [ $ans == "y" ]
then
    read -p "Database URL > " DB_URL
    sed -i -e "s/\${db_url}/${DB_URL}/" dummyrest.service
else
    sed -i -e "/\${db_url}/d" dummyrest.service
fi


UWSGI_PATH=$(which uwsgi)

# Create the service file
sed -i -e "s/\${user}/${USER}/" \
-e "s+\${UWSGI_PATH}+${UWSGI_PATH}+" \
dummyrest.service

sudo chown root:root dummyrest.service
sudo mv dummyrest.service /etc/systemd/system/

# sudo systemctl start dummyrest
# sleep 2