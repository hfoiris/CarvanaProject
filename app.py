from flask import Flask, render_template, request
from analysis import *
from dataloader import DataLoader
data_root = "./Data"
data = DataLoader(data_root)
analysis = Analysis(data)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'GET':
        # redirect to the previous page
        return f"The URL /result is accessed directly. Try going to '/' to submit form"
    if request.method == 'POST':
        res_loc = []
        res_trip = []
        results_by_location = {}
        for item in request.form["LocationCode"].split(","):
            results_by_location[item] = {}
            user_input = item
            loc = analysis.find_loc_detail(user_input)
            if loc == -1:
                return "More than one of the location codes is not valid. Please try again."
            trips = analysis.find_trips_detail(user_input)
            if trips == -1:
                return "More than one of the location info is not found. Please try again."
            res_loc.append(loc)
            res_trip.append(trips)
            results_by_location[item]["LOC"] = loc
            results_by_location[item]["Trips"] = trips
        return render_template('result.html', results_by_location=results_by_location)