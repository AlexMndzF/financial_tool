from flask import request
import os
import json

def uploadjson():
    upload    = request.files.get('upload')
    if upload == None or upload.filename == '':
        return 'Error no json'
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.json'):
        return 'Error'
    upload.save('/tmp/upload.json') # appends upload.filename automatically
    with open('/tmp/upload.json') as f:
        d = json.load(f)
        print(d)
    return d