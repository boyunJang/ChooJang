# file name : index.py
# pwd : /project_name/app/main/index.py

from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
from OS_engine.venv import Engine_for_train
# 추가할 모듈이 있다면 추가

main = Blueprint('main', __name__, url_prefix='/')

testData = {
    'batch': 50,
    'train_epch': 10,
    'param_conv': [3, 3, 3],
    'conv_active': 'relu',
    'pooling': 'Max',
    'param_dense': [(10, 'relu'), (10, 'softmax')],
    'loss': "tf.keras.losses.mean_squared_error"
}

@main.route('/', methods=['GET'])
def index():
    # /main/index.html은 사실 /project_name/app/templates/main/index.html을 가리킵니다.


    return render_template('/main/index.html')

@main.route('/post', methods=['POST'])
def post():
    # testData['conv_active'] = request.form['conv_active']
    # print(testData)
    instance = Engine_for_train
    instance.cg()

    return render_template('/main/index.html')

@main.route('/test', methods=['POST'])
def test():
    req_data = request.get_json()
    print(req_data)

    testData['batch'] = int(req_data['batch'])
    testData['train_epch'] = int(req_data['train_epch'])
    testData['param_conv'] = list(map(int, req_data['param_conv'].split(',')))
    testData['conv_active'] = req_data['conv_active']
    testData['pooling'] = req_data['pooling']


    # print(list(testData['param_dense'][0]))
    # print(list(testData['param_dense'][0])[0])
    # print(type((req_data['param_dense'].split(','))[0]))
    # print(len(testData['param_dense']))
    # print(req_data['param_dense'].split(','))

    for i in range(len(testData['param_dense'])):
        # print(list(testData['param_dense'][i])[0])
        print("req값", req_data['param_dense'].split(',')[i])
        list(testData['param_dense'][i])[0] = req_data['param_dense'].split(',')[i]
        print(testData['param_dense'][i][0])

    print(testData['param_dense'])
    # print(testData)


    return req_data

