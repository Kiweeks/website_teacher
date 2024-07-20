from flask import Flask, render_template, request
from database import cursor, db

app = Flask(__name__)


# @app.post('/load-file-admin')
# def load_file():
#     return


def load_menu(link_window):
    cursor.execute('SELECT title, link FROM view')
    result = cursor.fetchall()

    cursor.execute('SELECT title, link FROM view WHERE link = %s', (link_window,))
    titels = cursor.fetchone()['title']
    return result, titels


@app.get('/')
def index():
    result, titels = load_menu('/')
    return render_template('index.html', array=result, name_title=titels)


@app.get('/login')
def authorization():
    return render_template('logining.html')


@app.get('/discharge')
def discharge():
    result_menu, titels = load_menu('/discharge')

    cursor.execute("SELECT name_file FROM data WHERE name_file LIKE '%.docx' ")
    result_word_data = cursor.fetchall()
    cursor.execute("SELECT name_file FROM data WHERE name_file LIKE '%.xlsx' ")
    result_exel_data = cursor.fetchall()
    cursor.execute("SELECT name_file FROM data WHERE name_file NOT LIKE '%.docx' AND name_file NOT LIKE '%.xlsx'")
    result_else = cursor.fetchall()
    cursor.execute("SELECT name_file, date FROM data")
    full_data = cursor.fetchall()

    return render_template('discharg.html', array=result_menu, name_title=titels,
                           word_data=result_word_data, exel_data=result_exel_data, else_data=result_else,
                           full_data=full_data)


# @app.get('/portfolio')
# def parfolio():
#     return render_template('logining.html')


if __name__ == '__main__':
    app.run(debug=True)

# array = {'Информация о сайте': '/', 'Портфолио': '/Portfolio', 'Новости сайта': '/news', 'Карта сайта': '/site-map',
#          'Тематические планы': '/thematic-plans', 'География в цифрах и фактах, а также их': '/ewt',
#          'Методическая копилка': '/tests'}