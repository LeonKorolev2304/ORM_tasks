from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()

    user = User()
    user.name = "Пользователь 1"
    user.about = "биография пользователя 1"
    user.hashed_password = 'qwerty'
    user.email = "email@email.ru"
    db_sess.add(user)

    user2 = User()
    user2.name = "Пользователь 2"
    user2.about = "биография пользователя 2"
    user2.hashed_password = 'qwertyu'
    user2.email = "email2@email.ru"
    db_sess.add(user2)

    user3 = User()
    user3.name = "Пользователь 3"
    user3.about = "биография пользователя 3"
    user3.hashed_password = 'qwertyui'
    user3.email = "email3@email.ru"
    db_sess.add(user3)

    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()
