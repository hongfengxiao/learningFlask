# -*- coding: UTF-8 -*-
# File Uploads文件加载
#
from flask import request


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    ...


# 如果您想知道文件在上载到应用程序之前如何在客户机上命名，您可以访问filename属性。
# 如果您想使用客户端的文件名在服务器上存储文件，通过secure_filename()函数传递它

from flask import request
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))
    ...