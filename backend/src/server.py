from flask import request, Flask, jsonify, url_for, redirect, make_response, render_template
from authlib.integrations.flask_client import OAuth
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from cryptography.fernet import Fernet
from datetime import datetime
from flask_cors import CORS
from bson import ObjectId
import config as cfg
import waitress
import pymongo
import hashlib
import json 
import uuid
import os

CURRENT_SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_PATH = os.path.join(CURRENT_SCRIPT_DIRECTORY, 'templates')
key = Fernet.generate_key()


class Server:
    def __init__(self, name):
        self.app = Flask(import_name=name, template_folder=TEMPLATES_PATH)
        CORS(self.app, supports_credentials=True)
        self.app.config['CORS_HEADERS'] = 'Content-Type'
        self.app.config['CORS_SUPPORTS_CREDENTIALS'] = True
        self.app.config['JSON_SORT_KEYS'] = False
        self.app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
        self.app.secret_key = cfg.APP_SECRET_KEY
        self.oauth = OAuth(self.app)
        self.oauth.register(
            name='google',
            client_id=cfg.GOOGLE_CLIENT_ID,
            client_secret=cfg.GOOGLE_CLIENT_SECRET,
            access_token_url='https://accounts.google.com/o/oauth2/token',
            access_token_params=None,
            authorize_url='https://accounts.google.com/o/oauth2/auth',
            authorize_params=None,
            api_base_url='https://www.googleapis.com/oauth2/v1/',
            userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
            client_kwargs={'scope': 'email profile'},
            server_metadata_url='https://accounts.google.com/.well-known/openid-configuration'
        )

        self.mongo_client = pymongo.MongoClient(host=cfg.MONGODB_HOST,
                                                port=cfg.MONGODB_PORT)

        # ======================= home page ==========================
        @self.app.route('/categories', methods=['GET'])
        def send_categories():
            return self.__send_categories()

        @self.app.route('/', methods=['get'])
        def index():
            return self.__index()

        # ==================== authenticate ===========================
        @self.app.route('/authenticate')
        def authenticate():
            return self.__authenticate()

        @self.app.route('/google_login')
        def google_login():
            return self.__google_login()

        @self.app.route('/sign_up', methods=['POST'])
        def sign_up():
            return self.__sign_up()

        @self.app.route('/sign_in', methods=['POST'])
        def sign_in():
            return self.__sign_in()

        # ============================ posts =========================
        @self.app.route('/post', methods=['GET'])
        def send_post():
            return self.__send_post()

        @self.app.route('/posts', methods=['GET'])
        def send_posts():
            return self.__send_posts()

        @self.app.route('/write', methods=['POST'])
        def write_post():
            return self.__write_post()

        # ============================ comments ======================
        @self.app.route('/load_comment', methods=['GET'])
        def load_comment():
            return self.__load_comment()

        @self.app.route('/save_comment', methods=['POST'])
        def save_comment():
            return self.__save_comment()

        # ==================== error ================================

        @self.app.errorhandler(401)
        def handle_unauthorized(error):
            return self.__handle_unauthorized(error)

        @self.app.errorhandler(404)
        def handle_not_found(error):
            return self.__handle_not_found(error)

        @self.app.errorhandler(405)
        def handle_method_not_allowed(error):
            return self.__handle_method_not_allowed(error)

        @self.app.errorhandler(500)
        def handle_internal_server_error(error):
            return self.__handle_internal_server_error(error)

    def run(self):
        print('Running server...')

        print('Host: {}'.format(cfg.SERVER_HOST))
        print('Port: {}'.format(cfg.SERVER_PORT_NUMBER))

        # if cfg.SERVER_DEBUG_MODE:
        # self.app.run(host=cfg.SERVER_HOST, port=cfg.SERVER_PORT_NUMBER, debug=True)
        # else:
        waitress.serve(app=self.app, host=cfg.SERVER_HOST, port=cfg.SERVER_PORT_NUMBER,
                       threads=cfg.SERVER_WSGI_THREADS)

    # ==================== authenticate =============================

    def __authenticate(self):
        client = self.oauth.create_client('google')
        redirect_uri = url_for('google_login', _external=True)
        return client.authorize_redirect(redirect_uri)

    def __google_login(self):
        client = self.oauth.create_client('google')
        token = client.authorize_access_token()
        resp = client.get('userinfo')
        user_info = dict(resp.json())

        db = self.mongo_client.test_database
        user_collection = db.User

        email = dict(user_info)['email']
        exist_user = user_collection.find_one({'email': email})
        if not exist_user:
            name = dict(user_info)['name']
            image = dict(user_info)['picture']
            verify = dict(user_info)['verified_email']
            user_id = str(ObjectId())

            exist_user = {'_id': user_id,
                          'email': email,
                          'name': name,
                          'image': image,
                          'verified_email': verify,
                          'password': 'google'}
            user_collection.insert_one(exist_user)

        cookie = generate_user_cookie()

        response = redirect(cfg.FRONT_SERVICE_ADDRESS)
        resp = generate_response(response, cookie, login_res=True)
        resp.set_cookie('user_id', exist_user['_id'], domain='127.0.0.1')
        return resp

    def __sign_up(self):
        req = json.loads(request.data)
        email = req['email']
        name = req['name']
        password = req['password']
        image = req['image']
        db = self.mongo_client.test_database
        user_collection = db.User
        user_collection.insert_one(
            {
                '_id': str(ObjectId()),
                'email': email,
                'name': name,
                'password': calculate_password_hash(password),
                'verified_email': False,
                'image': image,
            }
        )

        return jsonify({'status': 'ok'})

    def __sign_in(self):
        db = self.mongo_client.test_database
        user_collection = db.User

        request_form = json.loads(request.data)
        email = request_form.get('email')
        password = request_form.get('password')

        h = hashlib.md5(password.encode())
        hashed_password = h.hexdigest()
        user = user_collection.find_one(
            {
                "password": {"$ne": "google"},
                "email": email
            }
        )
        if user:
            if user['password'] == hashed_password:

                encrypted_user_cookie = generate_user_cookie()
            else:
                return make_response(jsonify({'message': 'Wrong password!'}), 401)
        else:
            return make_response(jsonify({'message': 'No such user exists!'}), 401)

        response = {'status': 'ok'}
        resp = generate_response(response, encrypted_user_cookie)
        resp.set_cookie('user_id', user['_id'], domain='127.0.0.1')
        return resp

    # ======================= home page =========================

    @staticmethod
    def __index():
        cookie = confirm_authenticate(request.cookies)

        return generate_response({'status': 'authenticated' if cookie else 'unauthenticated'},
                                 cookie)

    def __send_categories(self):
        collection = self.mongo_client.test_database.Categories
        res = [category for category in collection.find()]

        return jsonify(res)

    # ============================ posts =========================

    def __send_post(self):
        req = request.args.to_dict()
        post_id = req['post_id']
        db = self.mongo_client.test_database
        posts_collection = db.Posts
        user_collection = db.User
        post = posts_collection.find_one({'_id': post_id})
        user = user_collection.find_one({'_id': post['user_id']})
        res = {'post': post,
               'user': user}

        return jsonify(res)

    def __send_posts(self):
        req = request.args.to_dict()

        collection = self.mongo_client.test_database.Posts
        post_per_page = int(req['postPerPage'])
        page = int(req['page'])
        category = req['category']
        start = post_per_page * (page - 1)
        posts = [post for post in
                 collection.find({'categories': category} if category else {}).skip(start).limit(post_per_page)]
        posts_count = collection.count_documents({'categories': category} if category else {})

        resp = {'previous': True if page == 1 else False,
                'next': True if (start + post_per_page) >= posts_count else False,
                'posts': posts}
        return jsonify(resp)

    def __write_post(self):
        cookie = confirm_authenticate(request.cookies)
        req = request.get_json()
        db = self.mongo_client.test_database
        posts_collection = db.Posts
        user_collection = db.User

        user_id = req['user_id']
        title = req['title']
        description = req['description']
        image = req['image']
        category = req['category']

        user = user_collection.find_one({'_id': user_id})

        views = 0
        username = user['name']

        post = {'_id': str(ObjectId()),
                'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
                'title': title,
                'description': description,
                'image': image,
                'views': views,
                'categories': category,
                'user_name': username,
                'user_id': user_id}
        posts_collection.insert_one(post)
        response = {'status': 'ok'}

        return generate_response(response, cookie)

    # ============================ comments =======================

    def __load_comment(self):
        cookie = confirm_authenticate(request.cookies)

        req = request.args.to_dict()
        post_id = req['post_id']

        db = self.mongo_client.test_database

        comment_collection = db.Comments
        user_collection = db.User

        comments = [comment for comment in comment_collection.find({'post_id': post_id})]
        comment_user = [[comment, user_collection.find_one({'_id': comment['user_id']})] for comment in comments]

        return generate_response({'comment_user': comment_user,
                                  'status': 'authenticated' if cookie else 'unauthenticated'},
                                 cookie)

    def __save_comment(self):
        req = request.get_json()

        post_id = req['post_id']
        user_id = req['user_id']
        description = req['description']
        db = self.mongo_client.test_database

        comment_collection = db.Comments

        comment = {'_id': str(ObjectId()),
                   'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
                   'post_id': post_id,
                   'description': description,
                   'user_id': user_id}
        comment_collection.insert_one(comment)
        return jsonify({'status': 200,
                        'massage': 'comment saved successfully'})

    def __handle_unauthorized(self, error):
        return render_template('unauthorized.htm', error=str(error)), 401

    def __handle_not_found(self, error):
        return render_template('not_found.htm', error=str(error)), 404

    def __handle_method_not_allowed(self, error):
        return render_template('method_not_allowed.htm', error=str(error)), 405

    def __handle_internal_server_error(self, error):
        return render_template('internal_server_error.htm', error=str(error.original_exception)), 500


def confirm_authenticate(cookies):
    if len(cookies) != 0:
        user_token_list = cookies.getlist('user_token')

        if user_token_list:
            user_token_decrypted = Fernet(key).decrypt(user_token_list[0]).decode('utf_8')
            user_token_parts = user_token_decrypted.split('_')

            if user_token_parts[0] == 'shabnamamdsmimajnooni':
                last_login = datetime.fromisoformat(user_token_parts[2])
                current_datetime = datetime.utcnow()
                minutes = divmod((current_datetime - last_login).total_seconds(), 60)[0]

                if minutes < 30:
                    return generate_user_cookie()

    return False


def generate_user_cookie():
    last_login = datetime.utcnow().isoformat()
    salt = 'shabnamamdsmimajnooni'
    user_cookie = salt + '_' + str(uuid.uuid4()) + '_' + last_login
    encrypted_user_cookie = Fernet(key).encrypt(user_cookie.encode('utf_8'))
    return encrypted_user_cookie


def generate_response(response, cookie, login_res=False):
    resp = make_response(response if login_res else jsonify(response))

    if cookie:
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS,HEAD'
        resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
        resp.set_cookie('user_token', cookie.decode('utf_8'), domain='127.0.0.1')
        return resp
    return resp


def calculate_password_hash(password):
    password_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    return password_hash


if __name__ == '__main__':
    server = Server(__name__)
    server.run()
