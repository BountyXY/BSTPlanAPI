import requests
import urllib.request
import time
import teacher
import classes
import rooms
import getPage
import datetime
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
kw = datetime.date.today().isocalendar()[1]

@app.route('/schoolAPI/test', methods=['GET'])
def get_test():
    return str('<u>LOL</u>')

@app.route('/schoolAPI/teachers', methods=['GET'])
def get_teacher():
    return jsonify(teacher.teacherRaw), 200

@app.route('/schoolAPI/teachers/<int:teacher_id>', methods=['GET'])
def get_teacherById(teacher_id):
    i = teacher_id
    return str(teacher.teacherRaw[i])

@app.route('/schoolAPI/teachers/<int:teacher_id>/plan', methods=['GET'])
def get_teacherPlan(teacher_id):
    i = teacher_id + 1
    file = 't0000' + str(i)
    if i > 9:
        file = 't000' + str(i)
    if i > 99:
        file = 't00' + str(i)
    return jsonify(getPage.getPage('https://bs-technik-schwerin.de/lankow/lehrer/' + str(kw) + '/t/' + str(file))), 200

@app.route('/schoolAPI/classes', methods=['GET'])
def get_classes():
    return jsonify(classes.classesRaw), 200

@app.route('/schoolAPI/classes/<int:class_id>', methods=['GET'])
def get_classesById(class_id):
    i = class_id
    return str(classes.classesRaw[i])

@app.route('/schoolAPI/classes/<int:class_id>/plan', methods=['GET'])
def get_classesPlan(class_id):
    i = class_id + 1
    file = 'c0000' + str(i)
    if i > 9:
        file = 'c000' + str(i)
    if i > 99:
        file = 'c00' + str(i)
    return jsonify(getPage.getPage('https://bs-technik-schwerin.de/lankow/klassen/P8/c/' + str(file))), 200

@app.route('/schoolAPI/rooms', methods=['GET'])
def get_rooms():
    return jsonify(rooms.roomsRaw), 200

@app.route('/schoolAPI/rooms/<int:room_id>', methods=['GET'])
def get_roomsById(room_id):
    i = room_id
    return str(rooms.roomsRaw[i])

@app.route('/schoolAPI/rooms/<int:room_id>/plan', methods=['GET'])
def get_roomsPlan(room_id):
    i = room_id + 1
    file = 'r0000' + str(i)
    if i > 9:
        file = 'r000' + str(i)
    if i > 99:
        file = 'r00' + str(i)
    return jsonify(getPage.getPage('https://bs-technik-schwerin.de/lankow/lehrer/' + str(kw) + '/r/' + str(file))), 200

if __name__ == '__main__':
    app.run(debug=True)
