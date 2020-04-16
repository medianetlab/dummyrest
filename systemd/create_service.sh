#!/bin/bash


cp systemd/service_template dummyrest.service

# Check the PATH - It should include /usr/local/bin as most modules are isntalled there
if [[ $PATH != *"/usr/local/bin"* ]]
then
    PATH="${PATH}:/usr/local/bin"
    sed -i -e "s/\${path}/${PATH}/" dummyrest.service
else
    sed -i -e "/\${path}/d" dummyrest.service
fi

# Install the modules
pip3.7 install . || pip3.6 install .

# Create the folder where the application will run
mkdir -p /var/run/dummyrest/logs
cp /dummyrest/dummyrest.db /var/run/dummyrest/

# Copy the configuration file to the created folder
cp systemd/uwsgi.ini /var/run/dummyrest/

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

mv dummyrest.service /etc/systemd/system/

systemctl start dummyrest
sleep 2

systemctl enable dummyrest

echo "Succesfully started dummyrest service\n"
