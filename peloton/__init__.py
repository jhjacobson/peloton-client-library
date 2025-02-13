#! /usr/bin/env python3.6
# -*- coding: latin-1 -*-

from .peloton import NotLoaded
from .peloton import PelotonException
from .peloton import PelotonAPI
from .peloton import PelotonUser
from .peloton import PelotonWorkout
from .peloton import PelotonRide
from .peloton import PelotonMetric
from .peloton import PelotonInstructor
from .peloton import PelotonWorkoutSegment
from .peloton import PelotonWorkoutFactory

from flask import Flask, render_template
from bson.objectid import ObjectId

"""
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.peloton_db
workouts_db = db.workouts
"""

app = Flask(__name__)

from peloton import routes

_ALL_ = [
    "NotLoaded",
    "PelotonException",
    "PelotonAPI",

    "PelotonUser",
    "PelotonWorkout",
    "PelotonRide",
    "PelotonMetric",
    "PelotonInstructor",
    "PelotonWorkoutSegment",

    "PelotonWorkoutFactory"
]