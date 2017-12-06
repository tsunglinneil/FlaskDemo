from flask import Flask, render_template
app = Flask(__name__)  # define app using flask


@app.route('/')
def test():
    return 'It works'

@app.route('/ken')
def test2():
    return 'KEN……'

@app.route('/ken/<string:var>')
def test3(var):
    return 'KEN{}'.format(var)

@app.route('/hello')
def test4():
    # render_template('檔案名稱') => render_template預設會去專案根目錄(以老師的範例來說，專案根目錄就是Flask這個資料夾名稱)
    # 底下的templates資料夾內找你指定的檔案名稱 (以這個例子來說就是index.html)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)