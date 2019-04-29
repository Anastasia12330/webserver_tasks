from flask import Flask, render_template, url_for, request

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


@app.route('/bootstrap_sample')
def bootstrap():
    return render_template('bootstrap.html')


@app.route('/yandex_music')
def yandex_music():
    return render_template('yandex_music.html')


@app.route('/list/<int:n>')
def list(n):
    return render_template('list.html', n=range(1, n + 1))


@app.route('/table/<int:n>/<int:m>')
def table(n, m):
    return render_template('table.html', n=range(1, n + 1), m=range(1, m + 1))


@app.route('/youtube/<int:n>')
def youtube(n):
    clips = ['https://www.youtube.com/embed/sU36sIJ31iA', 'https://www.youtube.com/embed/vR5ykbDSV-4',
             'https://www.youtube.com/embed/Htd_2MfQhLA', 'https://www.youtube.com/embed/Q2wWiAvRgvc',
             'https://www.youtube.com/embed/2wsVEBPAnRM']
    return render_template('youtube.html', n=n, clips=clips[:n])


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    print(request.method)
    if request.method == 'GET':
        return '''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport"
                            content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                            crossorigin="anonymous">
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <form method="post">
                                <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                <div class="form-group">
                                    <label for="classSelect">В каком вы классе</label>
                                    <select class="form-control" id="classSelect" name="class">
                                      <option>7</option>
                                      <option>8</option>
                                      <option>9</option>
                                      <option>10</option>
                                      <option>11</option>
                                    </select>
                                 </div>
                                <div class="form-group">
                                    <label for="about">Немного о себе</label>
                                    <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                </div>
                                <div class="form-group">
                                    <label for="form-check">Укажите пол</label>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                      <label class="form-check-label" for="male">
                                        Мужской
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                      <label class="form-check-label" for="female">
                                        Женский
                                      </label>
                                    </div>
                                </div>
                                <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8011, host='127.0.0.1')
