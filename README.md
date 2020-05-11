# Dummy REST API

Tool for testing REST APIs Function

## 1. Requirements

* python >= 3.6
* python-dev >= 3.6
* pip3.6

### 1.1 Install python3.7 and pip3.7 on Debian system

> Run as root

``` bash
apt update
apt install gcc git python3.7-minimal python3.7-dev python3-pip -y
python3.7 -m pip install --upgrade pip
```

> Note that if you execute the last command without `sudo`, `pip3.7` is installed in directory `/home/{username}/.local/bin` which might not be in the `PATH` variable, depending on the distribution you are running. Add the directory to the `PATH` variable in order to be able to use it.

### 1.2 Install python3.7 and pip3.7 on CentOS > 7 system

> Run as root

```bash
yum update -y
yum install -y epel-release && yum update -y
yum install -y gcc git python3 python3-devel python3-pip
```

## 2. Installation

### 2.1 PyPI

``` bash
pip3.7 install dummyrest
```

### 2.2 Github

```bash
git clone https://github.com/medianetlab/dummyrest.git
cd dummyrest
sudo pip3.7 install .
```

> Note that if you execute the last command without `sudo`, `dummyrest` script is installed in directory `/home/{username}/.local/bin` which might not be in the `PATH` variable, depending on the distribution you are running. Add the directory to the `PATH` variable in order to be able to use it.

## 3. Usage

A new command has been installed. which starts the dummyrest application:

``` bash
dummyrest
```

Add the `&` at the end to run at the background

The dummyrest application is listening by default on port **8000**. To check that the application has started run a curl request `curl http://<IP>:8000/dummy`. You should get a **200** response with the message `"Dummy REST API"`. By default the application writes a log file at the home directory of the user that started the application.

## 4. Database

A sample database to store the resources of the example REST API is supported by the application. You can set it to use an external database by setting the `DB_URL` environmental variable to the external databse URL before you start the application.

If no external database url is given, the application will use a local SQLITE3 database. You can set the path for the local db file by setting the `SQLITE_DB_PATH` environmental variable before you start the application. If this variable is not set, by default the application will create the databse file on the home directory of the user that started the application, under the name `dummyrest.db`.

## 5. Create a systemd service

To create a systemd service that will run the dummyrest application download the Github repository and run the script:

``` bash
sudo ./systemd/create_service
```

Run `systemctl status dummyrest` to check if the service has started successfully. The logs are stored in `/var/run/dummyrest/logs/dummyrest.log`

## 6. Use dummyrest with NGINX

### 6.1 Install NGINX

#### 6.1.1 Debian

> Run as root

```bash
apt install -y nginx
systemctl start nginx
systemctl enable nginx
systemctl status nginx
```

#### 6.1.2 CentOS

> Run as root

Set up the yum repository for RHEL or CentOS by creating the file nginx.repo: `vim /etc/yum.repos.d/nginx.repo`

```bash
[nginx]
name=nginx repo
baseurl=https://nginx.org/packages/mainline/centos/7/$basearch/
gpgcheck=0
enabled=1
```

Install nginx:

```bash
yum update -y
yum install -y nginx
systemctl start nginx
systemctl enable nginx
systemctl status nginx
```

If the SELINUX is enabled, then it must be allowed to serve http

```bash
semanage permissive -a httpd_t
systemctl reload nginx
```

### 6.2. Configure NNGINX

Remove any default file in `/etc/nginx/conf.d/` or `/etc/nginx/sites-enabled/` directories and create the `/etc/nginx/conf.d/dummyrest.conf` file:

```bash
server {
    listen 80 default_server;
    server_name _;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/var/www/html/dummyrest/socket.sock;
    }

    error_page 404 /404.html;
    location /404.html {
        root /usr/share/nginx/html;
    }

}
```

Reload the nginx service: `sudo systemctl reload nginx`

Create the folder where the socket file will be saved:

``` bash
sudo mkdir -p /var/www/html/dummyrest/
sudo chown -R ${USER}:${USER} /var/www/html/dummyrest
```

Run the `dummyrest-nginx` script to start serving the dummyrest application on port **80**

### 6.3 Create systemd service with nginx

To make create a systemd service using the nginx as webserver, configure the nginx as described above and run the script:

```bash
./nginx/systemd/create_service.sh
```

## 7. Available APIs

### 7.1 Dummy

| API | Method | Data | Description |
| --- | --- | --- | --- |
| /dummy | GET | - | Get a list of all the items in the dummy resource |
| /dummy | POST | JSON | Add a new item to the dummy resource |
| /dummy/{id} | GET | - | Get the item with id=id from the dummy resource |
| /dummy/{id} | POST | JSON | Create an item with id=id from the dummy resource |
| /dummy/{id} | PUT | JSON | Update or create the item with id=id from the dummy resource |
| /dummy/{id} | DELETE | - | Delete the item with id=id from the dummy resource |

### 7.2 Books

| API | Method | Data | Description |
| --- | --- | --- | --- |
| /books | GET | - | Get a list of all the books in the database |
| /books | POST | JSON | Add a new book in the database |
| /book/{title} | GET | - | Get the book with title=title from the database |
| /book/{title} | POST | JSON | Add a new book with title=title in the database |
| /book/{title} | PUT | JSON | Update or create the book with title=title in the database |
| /book/{title} | DELETE | - | Delete the book with title=title from the database |

### 7.3 Authors

| API | Method | Data | Description |
| --- | --- | --- | --- |
| /authors | GET | - | Get a list of all the authors in the database |
| /authors | POST | JSON | Add a new author in the database |
| /author/{name} | GET | - | Get the author with name=name from the database |
| /author/{name} | POST | JSON | Add a new author with name=name in the database |
| /author/{name} | PUT | JSON | Update or create the author with name=name in the database |
| /author/{name} | DELETE | - | Delete the author with name=name from the database |
