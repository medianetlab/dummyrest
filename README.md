# Dummy REST API

Tool for testing POST Function

## Available APIs
### Dummy
| API | Method | Data | Description |
| --- | --- | --- | --- |
| /dummy | GET | - | Get a list of all the items in the dummy resource |
| /dummy | POST | JSON | Add a new item to the dummy resource |
| /dummy/{id} | GET | - | Get the item with id=id from the dummy resource |
| /dummy/{id} | POST | JSON | Create an item with id=id from the dummy resource |
| /dummy/{id} | PUT | JSON | Update the item with id=id from the dummy resource |
| /dummy/{id} | DELETE | - | Delete the item with id=id from the dummy resource |

## Requirements

* python >= 3.7
* pip3.7

To install python3.7 and pip3.7 on Ubuntu system run:

``` bash
sudo apt install python3.7-minimal
sudo apt install python3-pip
python3.7 -m pip install --upgrade pip
```

> Note that `pip3.7` is installed in directory `/home/{username}/.local/bin` which might not be in the `PATH` variable. Add the directory to the `PATH` variable in order to be able to use it

## Installation

``` bash
git clone https://github.com/themisAnagno/dummyrest.git
cd dummyrest
pip install -e .
```

## Usage

``` bash
gunicorn --chdir /home/{username} -w 2 --bind 0.0.0.0:8000 --access-logfile /home/{username}/dummyrest/output.log --log-level INFO --capture-output --error-logfile /home/{username}/dummyrest/error.log wsgi:app
```
