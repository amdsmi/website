# # AS simeple as possbile flask google oAuth 2.0
# from flask import Flask, redirect, url_for, session
# from authlib.integrations.flask_client import OAuth
# import os
# from datetime import timedelta
#
#
# class Server:
#     def __init__(self, name):
#         self.app = Flask(name)
#         # Session config
#         self.app.secret_key = os.getenv("APP_SECRET_KEY")
#         self.app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
#         self.app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)
#
#         # oAuth Setup
#         self.oauth = OAuth(self.app)
#         self.oauth.register(
#             name='google',
#             client_id=os.getenv("GOOGLE_CLIENT_ID"),
#             client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
#             access_token_url='https://accounts.google.com/o/oauth2/token',
#             access_token_params=None,
#             authorize_url='https://accounts.google.com/o/oauth2/auth',
#             authorize_params=None,
#             api_base_url='https://www.googleapis.com/oauth2/v1/',
#             userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
#             client_kwargs={'scope': 'email profile'},
#             server_metadata_url='https://accounts.google.com/.well-known/openid-configuration'
#         )
#
#         @self.app.route('/')
#         def hello_world():
#             return self.__hello_world()
#
#         @self.app.route('/authenticate')
#         def authenticate():
#             return self.__authenticate()
#
#         @self.app.route('/google_login')
#         def google_login():
#             return self.__google_login()
#
#     def run(self):
#         self.app.run(debug=True)
#
#     def __hello_world(self):
#         email = dict(session)['profile']['email']
#         return f'Hello, you are logge in as {email}!'
#
#     def __authenticate(self):
#         client = self.oauth.create_client('google')  # create the google oauth client
#         redirect_uri = url_for('google_login', _external=True)
#         return client.authorize_redirect(redirect_uri)
#
#     def __google_login(self):
#         client = self.oauth.create_client('google')  # create the google oauth client
#         token = client.authorize_access_token()  # Access token from google (needed to get user info)
#         resp = client.get('userinfo')  # userinfo contains stuff u specificed in the scrope
#         user_info = dict(resp.json())
#          # uses openid endpoint to fetch user info
#
#         return user_info
#
#
# if __name__ == '__main__':
#     server = Server(__name__)
#     server.run()
#
import os

import config as cfg

print(os.getenv('APP_SECRET_KEY'))