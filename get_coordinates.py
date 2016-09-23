from __future__ import print_function
import requests
from flask import Flask,g,request,abort,jsonify,redirect,url_for
from requests.auth import HTTPBasicAuth
import json
import decimal
from flask_restful import reqparse, abort, Api, Resource
import time
DEBUG = True
HOST = '127.0.0.1'
PORT  = 8000
app = Flask(__name__)
api = Api(app)
@app.route("/get_coordinates/<int:index>")
def starter(index):
	lat_temp = ["12.92470" , "12.92540", "12.92603", "12.92683",
		   "12.92770", "12.92880", "12.92958", "12.93063", 
		   "12.93210", "12.93280", "12.93350", "12.93432",
		   "12.93518", "12.93545", "12.93589", "12.93613",
		   "12.93629", "12.93638", "12.93640"]	

	longi_temp = ["77.49859","77.49937", "77.50006", "77.50110", "77.50239", 
			 "77.50336","77.50509","77.50605","77.50763","77.50856", 
			 "77.50931" ,"77.51029", "77.51162", "77.51250",
			 "77.51392", "77.51502", "77.51625","77.51717","77.51793"]
	

	dummy_lat = lat_temp[index]
	dummy_long=longi_temp[index]
	lists = [{'lattitude': dummy_lat, 'longitude' : dummy_long}]
	return jsonify(coordinates = lists)

if __name__ == '__main__':
	app.run(debug = DEBUG, host =HOST, port = PORT)