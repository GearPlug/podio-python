# podio-python
![](https://img.shields.io/badge/version-0.1.4-success) ![](https://img.shields.io/badge/Python-3.8%20|%203.9%20|%203.10%20|%203.11-4B8BBE?logo=python&logoColor=white)  

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
```python
# if you are using Oauth2 to get an access_token:
from intercom.client import Client
client = Client(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
```
To obtain and set an access token:
1. **Get authorization URL**
```python
url = client.authorization_url(state=None)
```
2. **Get access token using code**
```python
response = client.get_access_token(code)
```
3. **Set access token**
```python
client.set_token(access_token)
```
Check more information about Podio Oauth: https://developers.podio.com/authentication/server_side
#### Refresh token
If your access token expired you can use your refresh token to obtain a new one:
```python
token = client.refresh_token(refresh_token)
# And then set your token again:
client.set_token(token["access_token"])
```
#### Get user status
```python
user = client.get_user_status()
```
### Organizations
#### List organizations
```python
orgs = client.list_organizations()
```
#### List organization spaces
```python
spaces = client.get_organization_spaces(org_id)
```
#### Get space
```python
spaces = client.get_space(space_id)
```
#### List space members
```python
members = client.get_space_members(space_id)
```
### Applications
#### List applications
```python
apps = client.list_applications()
```
#### Get application
```python
app = client.get_application(app_id)
```
#### Create item
```python
body = {"fields": {"title": "Juan Assignment", "status": 1}}
item = client.create_item(app_id, body)
```
#### Create task
```python
body = {"text": "Text of the task", "description": "desc"}
task = client.create_task(body)
```
#### Get task labels
```python
labels = client.get_task_labels()
```
### Webhooks
#### List webhooks
```python
hooks = client.list_webhooks(ref_type, ref_id)
```
#### Create webhook
```python
hook = client.create_webhook(ref_type, ref_id, url, hook_type)
```
#### Validate hook verification
```python
client.validate_hook_verification(webhook_id, code)
```
#### Delete webhook
```python
client.delete_webhook(webhook_id)
```