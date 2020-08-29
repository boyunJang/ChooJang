# file name : index.py
# pwd : /project_name/app/main/index.py

from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

# 추가할 모듈이 있다면 추가

main = Blueprint('main', __name__, url_prefix='/')

testData = {
    'batch': 50,
    'train_epch': 10,
    'param_conv': [3, 3, 3],
    'conv_active': 'relu',
    'pooling': 'Max',
    'param_dense': [(10, 'relu'), (10, 'softmax')],
    # 'loss': tf.keras.losses.mean_squared_error
}

@main.route('/', methods=['GET'])
def index():
    # /main/index.html은 사실 /project_name/app/templates/main/index.html을 가리킵니다.


    return render_template('/main/index.html', test=testData['conv_active'])


@main.route('/test')
def test():
    return render_template('/main/index.html')

@main.route('/post', methods=['POST'])
def post():
    testData['conv_active'] = request.form['conv_active']
    print(testData)
    return render_template('/main/index.html', test=testData['conv_active'])
