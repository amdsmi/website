import os

APP_SECRET_KEY = os.getenv("APP_SECRET_KEY", 'flask_oauth')

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", '253692784240-bnp7l0igljg2jppa1c3gjlk0ko6kaa04.apps.googleusercontent.com')

GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", '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')

FRONT_SERVICE_ADDRESS = os.getenv('FRONT_HOST', 'http://127.0.0.1:3000')

SERVER_DEBUG_MODE = os.getenv('SERVER_DEBUG_MODE', 'False')

SERVER_WSGI_THREADS = int(os.getenv('SERVER_WSGI_THREADS', '16'))

SERVER_HOST = os.getenv('SERVER_HOST', '127.0.0.1')

MONGODB_HOST = os.getenv('SERVER_HOST', '127.0.0.1')

MONGODB_PORT = os.getenv('SERVER_HOST', 27017)

SERVER_PORT_NUMBER = int(os.getenv('SERVER_PORT_NUMBER', '5000'))