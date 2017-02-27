# -*- coding: utf-8 -*-
import types
from flask import Flask
from .core import configure_logging
from .helpers import JSONEncoder


def create_app(package_name, settings_override=None, static_url_path=None,
               template_folder='templates'):

    app = Flask(package_name,
                instance_relative_config=True,
                static_url_path=static_url_path,
                template_folder=template_folder)

    app.config.from_pyfile('settings.cfg', silent=True)
    app.config.from_object('app.common.settings')
    if isinstance(settings_override, types.DictType):
        app.config.update(settings_override)
    else:
        app.config.from_object(settings_override)

    configure_logging(app)

    app.json_encoder = JSONEncoder

    return app
