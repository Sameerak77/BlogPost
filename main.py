from flask import Flask,render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy 
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///blog.db'
db=SQLAlchemy(app)

@app.route('/')
def intro():
	return render_template('intro.html')

@app.route('/post')
def post():
	return render_template('post.html')

@app.route('/all')
def all():
	posts=Blogpost.query.all()
	return render_template('all.html',posts=posts)


@app.route('/show/<int:pos_id>')
def show(pos_id):
	posts=Blogpost.query.filter_by(id=pos_id).one()
	return render_template('show.html',posts=posts)

@app.route('/output',methods=['POST'])
def output():
	title=request.form.get('title')
	subtitle=request.form.get('subtitle')
	author=request.form.get('author')
	content=request.form.get('content')
	pos=Blogpost(title=title,subtitle=subtitle,author=author,content=content)
	db.session.add(pos)
	db.session.commit()
	return redirect(url_for('all'))


class Blogpost(db.Model):
	id=db.Column(db.Integer(),primary_key=True)
	title=db.Column(db.String(length=30),nullable=False)
	subtitle=db.Column(db.String(length=30),nullable=False)
	author=db.Column(db.String(length=20),nullable=False)
	content=db.Column(db.Text)
