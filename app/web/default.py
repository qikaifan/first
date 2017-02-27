# -*- coding: utf-8 -*-


from flask import Blueprint

bp = Blueprint('default', __name__)


@bp.route('/<name>', methods=['GET', 'POST'])
def test(name):
    return name
