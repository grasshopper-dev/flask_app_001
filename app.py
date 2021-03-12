from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title="Form sample", message="お名前は？")

@app.route('/', methods=['POST'])
def form():
    field = request.form['field']
    return render_template('index.html', title="Form sample", message="こんにちは、%sさん！" % field)


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')