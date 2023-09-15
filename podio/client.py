import json
from urllib.parse import urlencode

import requests

from podio.exceptions import UnauthorizedError, WrongFormatInputError, ContactsLimitExceededError


class Client(object):
    URL = "https://api.podio.com/"
    AUTH_URL = "https://podio.com/oauth/authorize?"
    APPLICATION_JSON = "application/json"
    headers = {"Content-Type": APPLICATION_JSON, "Accept": APPLICATION_JSON}

    def __init__(self, access_token=None, client_id=None, client_secret=None, redirect_uri=None) -> None:
        self.CLIENT_ID = client_id
        self.CLIENT_SECRET = client_secret
        self.REDIRECT_URI = redirect_uri

    def authorization_url(self, state=None):
        params = {"client_id": self.CLIENT_ID, "redirect_uri": self.REDIRECT_URI}
        if state:
            params["state"] = state
        return self.AUTH_URL + urlencode(params)

    def get_access_token(self, code):
        body = {
            "grant_type": "authorization_code",
            "client_id": self.CLIENT_ID,
            "redirect_uri": self.REDIRECT_URI,
            "client_secret": self.CLIENT_SECRET,
            "code": code,
        }
        return self.post("oauth/token/v2", data=json.dumps(body))

    def set_token(self, access_token):
        self.headers.update(Authorization=f"OAuth2 {access_token}")

    def list_organizations(self):
        return self.get("org/")

    def get_organization_spaces(self, org_id):
        return self.get(f"org/{org_id}/space/")

    def get_space_members(self, space_id):
        return self.get(f"space/{space_id}/member/")

    def list_applications(self):
        return self.get("app/")

    def get_application(self, app_id):
        return self.get(f"app/{app_id}")

    def create_item(self, app_id, body):
        return self.post(f"item/app/{app_id}", data=json.dumps(body))

    def create_task(self, body):
        return self.post("task/", data=json.dumps(body))

    def get_task_labels(self):
        return self.get("task/label/")

    def get(self, endpoint, **kwargs):
        response = self.request("GET", endpoint, **kwargs)
        return self.parse(response)

    def post(self, endpoint, **kwargs):
        response = self.request("POST", endpoint, **kwargs)
        return self.parse(response)

    def delete(self, endpoint, **kwargs):
        response = self.request("DELETE", endpoint, **kwargs)
        return self.parse(response)

    def put(self, endpoint, **kwargs):
        response = self.request("PUT", endpoint, **kwargs)
        return self.parse(response)

    def patch(self, endpoint, **kwargs):
        response = self.request("PATCH", endpoint, **kwargs)
        return self.parse(response)

    def request(self, method, endpoint, **kwargs):
        return requests.request(method, self.URL + endpoint, headers=self.headers, **kwargs)

    def parse(self, response):
        status_code = response.status_code
        if "Content-Type" in response.headers and self.APPLICATION_JSON in response.headers["Content-Type"]:
            try:
                r = response.json()
            except ValueError:
                r = response.text
        else:
            r = response.text
        if status_code == 200:
            return r
        if status_code == 204:
            return None
        if status_code == 400:
            raise WrongFormatInputError(r)
        if status_code == 401:
            raise UnauthorizedError(r)
        if status_code == 406:
            raise ContactsLimitExceededError(r)
        if status_code == 500:
            raise Exception
        return r

