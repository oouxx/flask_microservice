from flask import Blueprint, jsonify, request, redirect, flash, render_template, url_for
from MyApp import db
from .models import User
import logging

users_blueprint = Blueprint('users', __name__, template_folder='./templates')


@users_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


@users_blueprint.route('/')
@users_blueprint.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        if not all((username, password, email)):
            return jsonify({'message': 'Invalid payload', 'status': 'fail'}), 400
        else:
            try:
                user = User.query.filter_by(email=email).first()
                if not user:
                    # 证明数据库中不存在该email的用户，可以添加
                    db.session.add(User(username=username, email=email, password_hash=password))
                    db.session.commit()
                    response_data = {
                        'status': 'success',
                        'message': 'add user success'
                    }
                    return jsonify(response_data), 201
                # 证明该email已经存在
                reponse_data = {
                    'status': 'success',
                    'message': 'login success'
                }
                # return redirect(url_for('users.index'))
                return jsonify(reponse_data), 200
            except Exception as e:
                logging.debug(e)
                return render_template('login.html')


