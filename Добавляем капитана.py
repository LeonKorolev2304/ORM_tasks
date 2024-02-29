from flask import Flask, render_template

from data import db_session
from data.news import News
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
@app.route('/login')
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    user1 = User(
        surname='Scott',
        name='Ridley',
        age=21,
        position='captain',
        speciality='research engineer',
        address='module_1',
        email='scott_chief@mars.org'
    )
    db_sess.add(user1)
    user2 = User(
        surname='Leonid',
        name='Korolev',
        age=15,
        position='capitain',
        speciality='programmer',
        address='module_2',
        email='leonidkorolev@mars.org'
    )
    db_sess.add(user2)
    user3 = User(
        surname='Dmitry',
        name='Laskin',
        age=15,
        position='captain',
        speciality='translater',
        address='module_3',
        email='dmitrylaskin@mars.org'
    )
    db_sess.add(user3)
    db_sess.commit()
    # app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
