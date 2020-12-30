import os, datetime, time
import library.db_utils as db_utils
from bson.objectid import ObjectId

domain = 'user'
domain_role_permissions = 'role_permissions'

def find(request, space_id):
    data = find_by_user_id(space_id, request.user_id)
    return (200, {'data': data})

def find_all(request, space_id):
    data = db_utils.find(space_id, domain, {})
    return (200, {'data': data})

def expand_authors(space_id, data):
    for item in data:
        last_modified_by = db_utils.find(space_id, domain, {'_id': item.get('lastModifiedBy')})
        created_by = db_utils.find(space_id, domain, {'_id': item.get('createdBy')})
        item['lastModifiedByEmail'] = last_modified_by[0].get('email')
        item['createdByEmail'] = created_by[0].get('email')
    return data

def do_update_user(request, space_id):
    updated_record = update_user(space_id, request.body, request.user_id)
    return (200, {'data': updated_record})

def find_permitted_actions(space_id, user_id):
    roles = db_utils.find(space_id, domain, {'_id': user_id})[0].get('roles')
    roles.append('open')
    return db_utils.find(space_id, domain_role_permissions, {'role': {'$in': roles}})

def find_by_user_id(space_id, user_id):
    return db_utils.find(space_id, domain, {'_id': user_id})

def update_user(space_id, data, user_id=None):
    return db_utils.upsert(space_id, domain, data, user_id)

def insert_user(space_id, data, user_id=None):
    data['_id'] = ObjectId(data['_id'])
    return db_utils.insert(space_id, domain, data, user_id)

def is_first_user(space_id):
    data = db_utils.find(space_id, domain, {})
    if len(data) == 0:
        return True
    else:
        return False
