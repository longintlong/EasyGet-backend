#coding=utf8
from flask import Flask,jsonify
from spider import main1
from flask import request
from func import dlf,gdlt,gdlf,uc,deldl,cla,adc
from commend import tuijian 
from get_openid import get
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello Flask'

@app.route('/request',methods=['GET','POST'])
def request1():
	#print request.method;
	try:
		if request.method == 'POST':
			url = request.get_json()['url']
			list = main1(str(url))
			json_data ={ 'type':list[0],'url':list[1],'filename':list[2],'size':list[3] } 
			return jsonify(json_data)
		else:
			return None
	except Exception as e:
			json_data ={ 'type':'request not ok'}
			print e
			return jsonify(json_data)
			pass

@app.route('/download_finish',methods=['GET','POST'])
def request2():
	if request.method == 'POST':
		try:
			user = request.get_json()['user']
			url = request.get_json()['url']
			webpath = request.get_json()['webpath']
			filepath = request.get_json()['filepath']
			fname = request.get_json()['fname']
			ti = request.get_json()['ti']
			#print webpath
			#print fname
			return dlf(user,url,webpath,filepath,fname,ti)
		except Exception as e:
			json_data ={ 'type':'download_finish not ok'}
			print e
			return jsonify(json_data)
			pass
	else:
		return None

@app.route('/get_times',methods=['GET','POST'])
def request3():
	if request.method == 'POST':
		user = request.get_json()['user']
		print gdlt(user)
		json_data ={ 'time':str(gdlt(user)) }
		return jsonify(json_data)
	else:
		return None

@app.route('/get_file_list',methods=['GET','POST'])
def request4():
	if request.method == 'POST':
		try:
			user = request.get_json()['user']
			result = gdlf(user)
			json_data ={ 'result':result,'len':len(result) }
			return jsonify(json_data)
		except Exception as e:
			json_data ={ 'type':'get_file_list not ok'}
			print e
			return jsonify(json_data)
			pass
	else:
		return None

@app.route('/use_coupon',methods=['GET','POST'])
def request5():
	if request.method == 'POST':
		try:
			user = request.get_json()['user']
			coupon = request.get_json()['co']
			print coupon
			result = uc(user,coupon)
			json_data ={ 'type':result }
			return jsonify(json_data)
		except Exception as e:
			json_data ={ 'type':'use_coupon not ok'}
			print e
			return jsonify(json_data)
			pass
	else:
		return None

@app.route('/deldl',methods=['GET','POST'])
def request6():
	if request.method == 'POST':
		try:
			user = request.get_json()['user']
			time = request.get_json()['time']
			result = deldl(user,time)
			json_data ={ 'type':result }
			return jsonify(json_data)
		except Exception as e:
			json_data ={ 'type':'del not ok'}
			print e
			return jsonify(json_data)
			pass
	else:
		return None

@app.route('/clearall',methods=['GET','POST'])
def request7():
	if request.method == 'POST':
		user = request.get_json()['user']
		result =cla(user)
		json_data ={ 'type':result }
		return jsonify(json_data)
	else:
		return None

@app.route('/add_message',methods=['GET','POST'])
def request8():
	if request.method == 'POST':
		try:
			user = request.get_json()['user']
			msg = request.get_json()['msg']
			print msg		
			map_text = os.sep +'data'+os.sep+'www'+os.sep+'static'+os.sep+'msg'+os.sep +'msg.txt'
			f=open(map_text,'a')
			f.write(user+'      '+msg+'\n')
			f.close()
			json_data ={ 'type':'ok'}
			return jsonify(json_data)
		except Exception as e:
			json_data ={ 'type':'add_message not ok'}
			print e
			return jsonify(json_data)
			pass
		#result = mes(user,msg)	
	else:
		return None

@app.route('/adc',methods=['GET','POST'])
def request9():
	if request.method == 'POST':
		try:
			co = request.get_json()['co']
			ti = request.get_json()['ti']
			print adc(co,ti)
			return jsonify({ 'type':'ok' })
		except Exception as e:
			print e
			return jsonify({'error':'adc errorr'})
			pass
	else:
		return None

@app.route('/commend',methods=['GET','POST'])
def request10():
	if request.method == 'POST':
		try:
			url = request.get_json()['name']
			result = tuijian(url)			
			return jsonify(result)
		except Exception as e:
			print e
			return jsonify({'error':'commend errorr'})
			pass
	else:
		return None

@app.route('/getid',methods=['GET','POST'])
def request11():
	if request.method == 'POST':
		try:
			code = request.get_json()['code']
			result = get(code)
			print code
			print result			
			return jsonify(result)
		except Exception as e:
			print e
			return jsonify({'error':'getid errorr'})
			pass
	else:
		return None
# @app.route('/test',methods=['GET','POST'])
# def request9():
# 	if request.method == 'POST':
# 		pmes()
# 		return jsonify({ 'type':'4' })
# 	else:
# 		return None	

if __name__== '__main__':
	app.run()
