# -*- coding: UTF-8 -*-
# 访问url时使用不同的HTTP方法

from flask import Flask, request

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
