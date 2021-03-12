from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Index with Jinja", message="これはJinjaテンプレートの利用例です。！")

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')