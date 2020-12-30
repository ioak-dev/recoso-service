import os, datetime, time
import library.db_utils as db_utils
import app.sequence.service as sequence_service
import app.role.service as role_service
import app.projectmember.service as projectmember_service
from bson.objectid import ObjectId

domain = 'project'


def find(request, space_id):
    # member_projects = find_member_projects(space_id, request.user_id)
    # admin_projects = find_admin_projects(space_id, request.user_id)
    all_projects = find_all_projects(space_id)
    projectid_list = []
    # for item in member_projects:
    #     if item['projectId'] not in projectid_list:
    #         projectid_list.append(ObjectId(item['projectId']))
    # for item in admin_projects:
    #     if item['domainId'] not in projectid_list:
    #         projectid_list.append(ObjectId(item['domainId']))

    # projects = db_utils.find(space_id, domain, {'_id': {'$in': projectid_list}})
    projects = db_utils.find(space_id, domain, {})

    return 200, {'data': projects}


def update(request, space_id, data):
    new_record = False
    if '_id' not in data:
        new_record = True
    updated_record = db_utils.upsert(space_id, domain, data, request.user_id)
    if new_record:
        sequence_service.create_sequence(space_id, 'taskOrder', updated_record['_id'], 1)
        sequence_service.create_sequence(space_id, 'stageOrder', updated_record['_id'], 1)
        sequence_service.create_sequence(space_id, 'taskId', updated_record['_id'], 1)
        sequence_service.create_sequence(space_id, 'epicColor', updated_record['_id'], 1)
        role_service.add(space_id,
                         {'type': 'ProjectAdministrator', 'userId': request.user_id, 'domainId': updated_record['_id']},
                         request.user_id)
    return 200, {'data': updated_record}


def delete(request, space_id, id):
    project_member_list = projectmember_service.find_by_projectid_userid(request, space_id, id, request.user_id)
    for item in project_member_list:
        print(item)
        if item['type'] == 'ADMINISTRATOR':
            result = db_utils.delete(space_id, domain, {'_id': id}, request.user_id)
            return 200, {'deleted_count': result.deleted_count}
        else:
            return 406, {'data': 'User is not a Member or administrator'}


def find_by_id(request, space_id, id):
    project_member_list = projectmember_service.find_by_projectid_userid(request, space_id, id, request.user_id)
    for item in project_member_list:
        print(item)
        if item['type'] == 'MEMBER' or item['type'] == 'ADMINISTRATOR':
            data = db_utils.find(space_id, domain, {'_id': id})
            return 200, {'data': data}
        else:
            return 406, {'data': 'User is not a Member or administrator'}

        # TBD deprecated should be removed


def find_all_projects(space_id):
    return db_utils.find(space_id, domain, {})


def get_by_reference(space_id, project_reference):
    data = db_utils.find(space_id, domain, {"reference": project_reference})
    if len(data) == 1:
        return data[0]
    else:
        return None
