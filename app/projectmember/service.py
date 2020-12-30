import os, datetime, time
import library.db_utils as db_utils
import app.sequence.service as sequence_service
import app.role.service as role_service
from bson.objectid import ObjectId

domain = 'project.member'


def find(request, space_id, project_id):
    data = db_utils.find(space_id, domain, {'projectId': project_id})
    return (200, {'data': data})


def add(request, space_id, data):
    updated_record = db_utils.upsert(space_id, domain, data, request.user_id)
    return (200, {'data': updated_record})


def delete(request, space_id, id):
    result = db_utils.delete(space_id, domain, {'_id': id}, request.user_id)
    return (200, {'deleted_count': result.deleted_count})


def find_by_projectid_userid(request, space_id, project_id, user_id):
    return db_utils.find(space_id, domain, {'projectId': project_id, 'userId': user_id})
