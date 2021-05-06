# Import dependencies and asign aliases
import datetime as dt
import numpy as np
import pandas as pd

# import sqlalchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import Flask dependencies
from flask import Flask, jsonify

# set up the database
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect database into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# Create variables for each of the classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# create session link from Python to database
session = Session(engine)

# define flask app
app = Flask(__name__)

# define the welcome route as the root
@app.route("/")

# Create a welcome function with a return statement of the precipiation, stations, tobs, and temp routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# new route for precipitation
@app.route("/api/v1.0/precipitation")

# Create a precipitation function
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# new route for station
@app.route("/api/v1.0/stations")

# Create a station function
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# new route for temperature observations
@app.route("/api/v1.0/tobs")

# create a temp function
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# new route for min, max, and avg temps with start and end dates
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# create a function called stats() with list called sel and if-not statement for starting and end dates
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)