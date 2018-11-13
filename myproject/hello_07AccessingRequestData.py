# -*- coding: UTF-8 -*-
# Accessing Request Data 访问请求数据
# Context Locals 本地环境

from flask import Flask, request

app = Flask(__name__)


with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'
