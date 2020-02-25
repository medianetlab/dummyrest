# Dummy REST API

Tool for testing POST Function

## Installation
```
git clone 
pip install .
```

##  Usage
```
gunicorn -w 2 --bind 0.0.0.0:8000 wsgi:app
```