from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "<h1>Привет, Яндекс! Я - Настя</h1>"


@app.route('/image_sample')
def image_sample():
    return '''<h1>Привет, Яндекс! Смотри картинку</h1>, <img src="{}", alt="здесь должна была быть картинка,
        но не нашлась">'''.format(url_for('static', filename='img/Риана.jpg'))


@app.route('/text_in_alert/<words>')
def alert(words):
    return f'''
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
     integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" 
     crossorigin="anonymous">
    <div class="alert alert-success" role="alert">
        <h2>{words}</h2>
    </div>
    '''


if __name__ == '__main__':
    app.run(port=8010, host='127.0.0.1')