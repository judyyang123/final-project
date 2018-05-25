from flask_script import Manager
from songbase import app, db, Author, Book

manager = Manager(app)


@manager.command
def deploy():
    print ("resetting database")
    db.drop_all()
    db.create_all()

    print ("inserting initial data")
    rowling = Author(name="JK Rowling", about="this is jk rowling")
    austin = Author(name="Jane Austin", about="this is jane")
    lee = Author(name="Harper Lee", about="this is harper")
    potter = Song(name='Harry Potter', year=1997, author=rowling)
    pride= Song(name='Pride and Prejudice', year=1813, author=austin)
    mockingbird = Song(name='To Kill a Mockingbird', year=1960, author=lee)

    db.session.add(rowling)
    db.session.add(austin)
    db.session.add(lee)
    db.session.add(potter)
    db.session.add(pride)
    db.session.add(mockingbird)

    db.session.commit()


if __name__ == '__main__':
    manager.run()
