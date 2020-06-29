from flask import Flask
app = Flask(__name__) 
# app = Flask(__name__) 은 플라스크 어플리케이션을 생성하는 문장이다. 
# 여기서 사용된 __name__ 변수는 실행된 모듈명을 의미하므로 pybo라는 문자열이 대입된다.

@app.route('/')
# @app.route 는 특정 URL(예:/)로 접속하면 해당함수(예:hello_python)를 호출하는 플라스크의 데코레이터이다.
def hello_pybo():
    return 'Hello, Pybo!'
