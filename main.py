from flask import Flask, render_template, request
from database import cursor, db

app = Flask(__name__)


@app.get('/')
def index():
    cursor.execute('SELECT title, link FROM view')
    result = cursor.fetchall()
    
    cursor.execute('SELECT title, link FROM view WHERE link = %s', '/',)
    titels = cursor.fetchone()['title']
    return render_template('index.html', array=result, name_title=titels)


@app.get('/login')
def authorization():
    return render_template('logining.html')


# @app.get('/portfolio')
# def parfolio():
#     return render_template('logining.html')


if __name__ == '__main__':
    app.run(debug=True)

# array = {'Информация о сайте': '/', 'Портфолио': '/Portfolio', 'Новости сайта': '/news', 'Карта сайта': '/site-map',
#          'Тематические планы': '/thematic-plans', 'География в цифрах и фактах, а также их': '/ewt',
#          'Методическая копилка': '/tests'}