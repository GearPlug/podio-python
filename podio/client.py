import requests

from podio.exceptions import UnauthorizedError, WrongFormatInputError, ContactsLimitExceededError


class Client(object):
    URL = "https://api.podio.com"
    AUTH_URL = "https://podio.com/oauth/authorize?"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    def __init__(self, access_token=None, client_id=None, client_secret=None) -> None:
        self.CLIENT_ID = client_id
        self.CLIENT_SECRET = client_secret
