from flask import Flask, render_template
app = Flask(__name__) #define app using flask

@app.route('/')
def test():
    return 'It works'

@app.route('/ken')
def test2():
    return 'KEN……'

@app.route('/ken/<string:var>')
def test3(var):
    return 'KEN……{}'.format(var)

@app.route('/hello')
def test4():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)