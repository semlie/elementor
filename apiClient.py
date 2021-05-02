# -*- coding: utf-8 -*-

import  json, requests, re



# https://docs.python-requests.org/en/master/user/authentication/
# https://docs.informatica.com/integration-cloud/cloud-api-manager/current-version/api-manager-guide/authentication-and-authorization/oauth-2-0-authentication-and-authorization/python-3-example--invoke-a-managed-api-with-oauth-2-0-authentica.html
# response = requests.get(    'https://website.com/id', headers={'Authorization': 'access_token myToken'})
import logging
import sys
import time
import base64

logging.captureWarnings(True)

def _get(prams):
    session = requests.Session()
    session.headers.update({'x-apikey': '6b26918a6971ea154a2b119553ec6eba7dcd4ec2b0889ea3768e011a00cbaceb'})
    return session.get(prams)

def get_url_id(url):

    return base64.urlsafe_b64encode(url.encode()).decode().strip("=")

def build_url(parms):
    return "https://www.virustotal.com/api/v3/domains/{}".format(parms)
    # return "https://www.virustotal.com/api/v3/urls/{}".format(get_url_id(parms))

def get(url):
    return _get(build_url(url))
#
# class apiClient():
#
#     test_api_url = "https://www.virustotal.com/api/v3{}/{}"
#     def __init__(self):
#         self.session =None
#         if not self.session:
#             self.session =self._get_new_token()
#
#     ##
#     ##    function to obtain a new OAuth 2.0 token from the authentication server
#     ##
#     def _get_new_token(self):
#
#         #
#         auth_server_url = "https://dm-us.informaticacloud.com/authz-service/oauth/token"
#         client_id = 'Jl88QzqE3GYvaibOVb1Fx'
#         client_secret = '9xy23jdl'
#
#         token_req_payload = {'grant_type': 'client_credentials'}
#
#         token_response = requests.post(auth_server_url,
#                                        data=token_req_payload, verify=False, allow_redirects=False,
#                                        auth=(client_id, client_secret))
#
#         if token_response.status_code != 200:
#             print("Failed to obtain token from the OAuth 2.0 server", file=sys.stderr)
#             return 'text'
#
#         print("Successfuly obtained a new token")
#         tokens = json.loads(token_response.text)
#         return tokens['access_token']
#
#     ##
#     ## 	obtain a token before calling the API for the first time
#     ## 	the token is valid for 15 minutes
#     ##
#
#     def getClient(self):
#
#         ##
#         ##   call the API with the token
#         ##
#         api_call_headers = {'Authorization': 'Bearer ' + self.session}
#         api_call_response = requests.session()
#         api_call_response.headers.update(api_call_headers)
#         # test_api_url, headers=, verify = False)
#         #
#         # ##
#         # ##
#         # if api_call_response.status_code == 401:
#         #     token = get_new_token()
#         # else:
#     #     print(api_call_response.text)
#         #
#         # time.sleep(30)
#         return api_call_response
#     def get(self,url):
#         r= self.getClient()
#         return r.get(url,verify = False)
#
#     def post(self,url,data):
#         r= self.getClient()
#         return r.post(url,data=data,verify = False)

# if __name__ == '__main__':
#
#     c = apiClient()
#     print(c.get('https://httpbin.org/ip').json())

