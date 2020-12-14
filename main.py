from flask import Flask, request
from flask_apscheduler import APScheduler
from datetime import datetime, date, time
from firebase import firebase
from random import random

app = Flask(__name__)
scheduler = APScheduler()
database = firebase.FirebaseApplication('https://vietlongpro1999-default-rtdb.firebaseio.com/', None)

def update_status_onl():
  database.put('/controller/', 'pump', 1)
  print("turn onl")

def update_status_off():
  database.put('/controller/', 'pump', 0)
  print("turn off")

@app.route("/")
def index():
  return "Welcome to the scheduler"

def test_job():
  print('hello World')


@app.route('/add-job', methods=["POST"])
def add_job():
  req_data = request.get_json(force=True)
  datetime_start = datetime.strptime(req_data['start'], "%m-%d-%Y %H:%M:%S")
  scheduler.add_job(id='start_pump_' + str(random()), func=update_status_onl,trigger="date", run_date=datetime_start)
  datetime_stop = datetime.strptime(req_data['stop'], "%m-%d-%Y %H:%M:%S")
  scheduler.add_job(id="stop_pump_" + str(random()), func=update_status_off,trigger="date", run_date=datetime_stop)
  return {"messsage": "success"}



if __name__ == "__main__":
  scheduler.start()
  app.run(host="0.0.0.0", port=8080)