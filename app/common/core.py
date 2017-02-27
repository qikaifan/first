# -*- coding: utf-8 -*-
import httplib, json
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, current_user
from flask_principal import Principal, identity_loaded, RoleNeed, UserNeed

db = SQLAlchemy()


class User(UserMixin):

    def __init__(self, uid, roles=[]):
        self.uid = uid
        self.roles = roles

    def get_id(self):
        return self.uid

    def get_roles(self):
        return self.roles

    def __str__(self):
        return '<User id={}, roles={}>'.format(self.uid, self.roles)

    @property
    def is_anonymous(self):
        return not bool(self.uid)

    @staticmethod
    def verity_token(token):
        conn = httplib.HTTPConnection('qsso.corp.qunar.com')
        conn.request('GET', '/api/verifytoken.php?token=%s' % token)
        resp = conn.getresponse().read()
        conn.close()

        return json.loads(resp)

    @staticmethod
    def load_user(uid):
        # TODO replace it
        return User(uid, ['dev'])


def configure_logging(app):

    import logging

    logging.basicConfig(**{
        'filename' : app.config.get('errorlog', None),
        'format' : app.config.get('logformat', logging.BASIC_FORMAT),
        'level' : logging._levelNames[app.config.get('loglevel', 'INFO').upper()]
    })


def configure_flask_sqlalchemy(app):
    db.init_app(app)


def configure_flask_login(app):
    login_manager = LoginManager()
    login_manager.login_view = 'default.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.load_user(user_id)

    login_manager.init_app(app)


def configure_flask_principal(app):

    principals = Principal(app)

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):

        identity.user = current_user

        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role))


def configure_flask_sqlalchemy(app):
    db.init_app(app)


def dict_conf(conf, key):
    conf[key] = dict(item.split('=') for item in conf[key].split(';'))


def list_conf(conf, key):
    conf[key] = [item for item in conf[key].split(';')]


def bind_of(bind_key):
    return db.get_engine(current_app, bind_key)
