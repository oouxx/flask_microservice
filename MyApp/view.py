from flask import Blueprint, jsonify, request, redirect, flash, render_template, url_for
from MyApp import db
from .models import User

users_blueprint = Blueprint('users', __name__, template_folder='./templates')


@users_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


@users_blueprint.route('/users', methods=['POST'])
def add_user():
    # 获取POST的数据
    post_data = request.get_json()
    if not post_data:
        response_data = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        return jsonify(response_data), 400
    email = post_data.get('email')
    username = post_data.get('username')
    try:
        user = User.query.filter_by(email=email).first()
        if not user:
            # 证明数据库中不存在该email的用户，可以添加
            db.session.add(User(username=username, email=email))
            db.session.commit()
            response_data = {
                'status': 'success',
                'message': '%s was added!' % email
            }
            return jsonify(response_data), 201
        # 证明该email已经存在
        response_data = {
            'status': 'fail',
            'message': 'Sorry. That email already exists.'
        }
        return jsonify(response_data), 400
    except Exception as e:
        print(e)
        response_data = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        return jsonify(response_data), 400


@users_blueprint.route('/')
@users_blueprint.route('/index', methods=['GET'])
def index():
    return render_template("index.html")
