# -*- coding: UTF-8 -*-
# 要渲染一个模板，可以使用render_template()方法。您所要做的就是提供模板的名称和要传递给模板引擎的变量作为关键字参数。

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run()
