# Flask

### 가상환경 만들기

```bash
$ pyenv virtualenv 3.6.1 flask
```

- 실행

``` bash
$ activate flask
```

- Flask 설치

```bash
$ pip install flask
```

- app.py 파일 생성

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"
```

- Flask 실행

``` bash
$ flask run --host 0.0.0.0 --port 8080
```
