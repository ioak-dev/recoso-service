import os, datetime, time
import library.db_utils as db_utils
import app.sequence.service as sequence_service

domain = 'role'

def find(request, space_id):
    return (200, {'data': find_all_roles(space_id)})

def update(request, space_id, data):
    authorized = False
    if data['type'] == 'ProjectAdministrator':
        authorized = is_project_admin(space_id, request.user_id, data['domainId'])
    elif data['type'] == 'TeamAdministrator':
        authorized = is_team_admin(space_id, request.user_id, data['domainId'])
    
    if authorized:
        updated_record = add(space_id, data, request.user_id)
        return (200, {'data': updated_record})
    else:
        return (401, {'data': 'unauthorized'})

def add(space_id, data, user_id):
    return db_utils.upsert(space_id, domain, data, user_id)

def delete(request, space_id, id):
    existing_record = db_utils.find(space_id, domain, {'_id': id})
    if len(existing_record) > 0:
        authorized = False
        if existing_record[0]['type'] == 'ProjectAdministrator':
            authorized = is_project_admin(space_id, request.user_id, existing_record[0]['domainId'])
        elif existing_record[0]['type'] == 'TeamAdministrator':
            authorized = is_team_admin(space_id, request.user_id, existing_record[0]['domainId'])

        if authorized:
            result = db_utils.delete(space_id, domain, {'_id': id}, request.user_id)
            return (200, {'deleted_count': result.deleted_count})
        else:
            return (401, {'data': 'unauthorized'})
    else:
        return (404, {'data': 'no matching role found'})

def find_all_roles(space_id):
    return db_utils.find(space_id, domain, {})

def find_admin_projects(space_id, user_id):
    return db_utils.find(space_id, domain, {'userId': user_id, 'type': 'ProjectAdministrator'})

def find_admin_teams(space_id, user_id):
    return db_utils.find(space_id, domain, {'userId': user_id, 'type': 'TeamAdministrator'})

def is_project_admin(space_id, user_id, project_id):
    role = db_utils.find(space_id, domain, {'userId': user_id, 'type': 'ProjectAdministrator', 'domainId': project_id})
    if len(role) > 0:
        return True
    else:
        return False

def is_team_admin(space_id, user_id, project_id):
    role = db_utils.find(space_id, domain, {'userId': user_id, 'type': 'TeamAdministrator', 'domainId': project_id})
    if len(role) > 0:
        return True
    else:
        return False
