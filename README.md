# podio-python
![](https://img.shields.io/badge/version-0.1.0-success) ![](https://img.shields.io/badge/Python-3.8%20|%203.9%20|%203.10%20|%203.11-4B8BBE?logo=python&logoColor=white)  

*podio-python* is an API wrapper for Podio, written in Python.  
This library uses Oauth2 for authentication.
## Installing
```
pip install podio-python
```
## Usage
```python
# if you have an access token:
from podio.client import Client
client = Client(access_token=access_token)
```