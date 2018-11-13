# -*- coding: UTF-8 -*-
# Redirects and Errors 重定向和错误
# 要将用户重定向到另一个端点 redirect()
# 要使用错误代码提前终止请求，abort()
from flask import Flask, abort, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()


# 如果您想定制错误页面，可以使用errorhandler()装饰器
from flask import render_template


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
