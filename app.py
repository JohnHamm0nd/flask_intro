from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/welcome")
def welcome():
    return "welcome flask!!"
    
@app.route("/html_tag")
def html_tag():
    return """
    <h1>안녕하세요!!!</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """