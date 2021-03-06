from flask import Flask,render_template,abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pymongo import MongoClient

app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELODA']=True
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/shiyanlou'
db=SQLAlchemy(app)
client=MongoClient('127.0.0.1',27017)
db_mongo=client.shiyanlou

class File(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(80))
	created_time=db.Column(db.DateTime)
	category_id=db.Column(db.Integer,db.ForeignKey('category.id'))
	category=db.relationship('Category',backref=db.backref('files'))
	content=db.Column(db.Text)
	def __init__(self,title,created_time,category,content):
		self.title=title
		self.created_time=created_time
		self.category=category
		self.content=content
	def __repr__(self):
		return '<File %s>'%self.title
	def add_tag(self,tag_name):
		if tag_name not in  db_mongo.tag.find_one({'file_id':self.id})['tag_name']:
			file_tag={'file_id':self.id,'tag_name':tag_name}
			db_mongo.tag.insert_one(file_tag)
	def remove_tag(self,tag_name):
		db_mongo.tag.delect_one({'tag_name':tag_name})
	@property 
	def tags(self):
		tags=[]
		tags_file=db_mongo.tag.find({'file_id':self.id})
		for tag in tags_file:
			tags.append(tag['tag_name'])
		return tags

class Category(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(80))
	def __init__(self,name):
		self.name=name
	def __repr__(self):
		return '<Category %s>'%self.name

titles=File.query.all()
print(titles)
category1=titles[0]
category2=titles[1]

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'),404

@app.route('/')
def index():
	return render_template('index.html',titles=titles)

@app.route('/files/<file_id>')
def file(file_id):
	content={
	'title1':category1.title,
	'created_time1':category1.created_time,
	'category_id1':category1.category_id,
	'content1':category1.content,
	'title2':category2.title,
	'created_time2':category2.created_time,
	'category_id2':category2.category_id,
	'content2':category2.content
	}
	print(type(file_id))
	print(type(category1.id))
	if file_id == str(category1.id) or file_id == str(category2.id):
		return render_template('file.html',content=content,file_id=file_id)
	else:
		abort(404)

if __name__=='__main__':
	app.run()
