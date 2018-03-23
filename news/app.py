from flask import Flask,render_template,abort
import os,json

app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELODA']=True
path='/home/shiyanlou/files/'
dir_list=os.listdir(path)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'),404

@app.route('/')
def index():
	filename_json=[]
	title_list=[]
	for filename in dir_list:
		filename_json.append(path+filename)
		with open(path+filename) as file:
			data=json.loads(file.read())
			title_list.append(data['title'])
	return render_template('index.html',filename_json=filename_json,title_list=title_list)




@app.route('/files/<filename>')
def file(filename):
	filename=filename+'.json'
	data=[]
	if filename in dir_list:
		with open(path+filename) as file:
			data=json.loads(file.read())
			print(data)
		return render_template('file.html',file_data=data)
	else:
		abort(404)

if __name__=='__main__':
	app.run()
