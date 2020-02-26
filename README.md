# Dummy REST API

Tool for testing POST Function

## Requirements

* python >= 3.7

## Installation

``` bash
git clone https://github.com/themisAnagno/dummyrest.git
cd dummyrest
pip install -e .
```

## Usage

``` bash
gunicorn -w 2 --bind 0.0.0.0:8000 wsgi:app
```
