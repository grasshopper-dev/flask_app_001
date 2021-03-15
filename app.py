from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title="Form sample", message='This is sample page')

@app.route('/', methods=['POST'])
def form():
    ck = request.form.get('check')
    rd = request.form.get('radio')
    sel = request.form.getlist('sel')
    return render_template('index.html', title="Form sample", message=[ck, rd, sel])

@app.route('/next', methods=['GET'])
def next():
    return render_template('next.html', title="Next page", message='This is next page sample', data=['One', 'Two', 'Three'])

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')