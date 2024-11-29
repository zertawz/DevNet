#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException
import json
from nornir import InitNornir
from services.devices import (get_inventory, add_device)


app = Flask(__name__)

def init_nornir():
    app.config['nr'] = InitNornir(config_file="fastprod/inventory/config.yaml")

init_nornir()

"""
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
"""

@app.route('/')
def welcome():
    response = {
        "env": "DEV",
        "name": "fastprod_backend",
        "version": 1.0
    }
    return jsonify(response)

@app.route("/devices", methods=['GET', 'POST'])
def devices():
    init_nornir()
    if request.method == 'GET':
        devices = get_inventory()
        return jsonify(devices=devices, total_count=len(devices))
    #Add a new device to host, must add some sanitarisation
    if request.method == 'POST':
        data = request.get_json()
        new_device = add_device(data)
        return jsonify(device=new_device)

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
    "code": e.code,
    "name": e.name,
    "description": e.description,
    })
    response.content_type = "application/json"
    return response