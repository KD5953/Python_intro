from flask import Flask, render_template

app = Flask(__name__)



@app.route('/play')
def playl1():
    return render_template('index.html',)

@app.route('/play/<int:x>')
def playlv2(x):
    return render_template('index2.html', times=x)

@app.route('/play/<int:x>/<color>')
def playlv3(x, color):
    return render_template('index3.html', times=x, color=color)


if __name__=="main":
    app.run(debug=True)