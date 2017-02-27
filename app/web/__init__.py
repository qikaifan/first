# -*- coding: utf-8 -*-
#
from ..common.factory import create_app
from ..common.core import *
from ..common.helpers import register_blueprints


def app_factory(global_conf, **local_conf):
    conf = {
        'SQLALCHEMY_DATABASE_URI': 'sqlite://'
    }

    conf.update(global_conf)
    conf.update(local_conf)

    app = create_app(__name__, conf, static_url_path='',
                     template_folder='static')

    configure_flask_sqlalchemy(app)

    register_blueprints(app, __name__, __path__)

    return app
