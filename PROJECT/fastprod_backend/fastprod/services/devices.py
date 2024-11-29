#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from utils.inventory import add_item_to_hosts_yaml
from flask import abort, make_response, jsonify

def get_inventory():
    from api import app
    print(app.config.get('nr').inventory.dict())
    hosts = app.config.get('nr').inventory.dict().get('hosts').keys()
    return list(map(lambda item: app.config.get('nr').inventory.dict().get('hosts').get(item), hosts))

def add_device(device):
    device = add_item_to_hosts_yaml(item=device)
    return device

def get_device_by_name(name):
    host = app.config.get('nr').inventory.hosts.get(name)
    if not host:
        abort(make_response(jsonify(message="device not found"), 404))
    return host.dict()

def delete_device(device):
    try:
        delete_item_from_hosts_yaml(item=device)
    except Exception as e:
        abort(make_response(jsonify(message="Unable to delete this device", error=str(e)), 500))