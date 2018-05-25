import os
from flask import Flask, render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# set up SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


# define database tables
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)
    book = db.relationship('Song', backref='author', cascade='delete')


# define database tables
class Book(db.Model):
    __tablename__ = 'Bookbase'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    year = db.Column(db.Integer)
    arthor_id = db.Column(db.Integer, db.ForeignKey('authors.id'))


@app.route('/')
def index():
    # return "hello judy yang"
    return render_template ('index.html')


@app.route('/about')
def about():
    return render_template('resume.html')


@app.route('/arthors')
def all_arthors():
    artists=Authors.query.all()
    return render_template ('all-authors.html', authors=authors)


@app.route('/user')
def user():
    return "this is the page for users"


@app.route('/users/<string:username>')
def users(username):
    # return "hello %s" %username
    return render_template('user.html', uname=username)


@app.route('/authors/edit/<int:id>', method=['GET', 'POST'])
def artist_edit(id):
    author = Author.query.filter_by(id=id).first()
    if request.method =='GET':
        return redner_template('authors-edit.html', author=author)

    if request.method =='POST':
        author.name=request.form['name']
        db.session.commit()
        return redirect(url_for('all_authors'))

    return "this is authors %d  updated" % id
    #return render_template('user.html', uname=username)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method=='GET':
        #return "hello GET"
        return redner_template ('form.html')
    if request.method=='POST':
        first_name=request.form("first_name")
        # return "Hi, your name is %s" % first_name
        return redner_template ('form.html', first_name=first_name)

if __name__ =='__main__':
    app.run()
