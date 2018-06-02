#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import json
import requests

_HEADERS = {'Accept': 'application/json'}

_session = requests.session()

def fetch_json(url, headers=None):
    return _fetch(url, headers).json()

def fetch_text(url, headers=None):
    return _fetch(url, headers).text

def _fetch(url, headers=None):
    headers = headers or {}
    for k, v in _HEADERS.items():
        headers.setdefault(k, v)
    resp = _session.get(url, headers=headers)
    resp.raise_for_status()
    return resp
 