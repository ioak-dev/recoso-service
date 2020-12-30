import os, datetime, time
from pymongo import MongoClient
import library.db_utils as db_utils
from gridfs import GridFS
import base64
from bson.binary import Binary
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

DATABASE_URI = os.environ.get('DATABASE_URI')

domain = 'space'
self_space_id = 'recoso'

def do_create(data):
    updated_record = db_utils.upsert(self_space_id, domain, data)
    return (200, {'data': updated_record})

def do_get_banner(space_id):
    spaceData = db_utils.find(self_space_id, domain, {'name': space_id})[0]
    spaceData['_id'] = str(spaceData['_id'])
    if 'banner' in spaceData:
        return (200, base64.b64encode(spaceData['banner']))
    else:
        return (404, None)

def do_get_space(space_id):
    spaceData = db_utils.find(self_space_id, domain, {'name': space_id})[0]
    spaceData['_id'] = str(spaceData['_id'])
    spaceData.pop('banner', None)
    return (200, spaceData)

def do_update_space(space_id, data):
    spaceData = db_utils.find(self_space_id, domain, {'name': space_id})[0]
    updated_data = db_utils.upsert(self_space_id, domain, data)
    return (200, {'data': updated_data})

def get_all_spaces():
    return db_utils.find('recoso', 'space', {})
