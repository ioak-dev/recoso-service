import library.db_utils as db_utils
import app.project.service as project_service

domain = 'endpoint.custom'


def find(request, space_id):
    custom_domains = db_utils.find(space_id, domain, {})
    return 200, {'data': custom_domains}

def find_by_project_id(request, space_id, project_id):
    data = db_utils.find(space_id, domain, {'project_id': project_id})
    return 200, {'data': data}


def update(request, space_id, data):
    updated_record = db_utils.upsert(space_id, domain, data, request.user_id)
    return 200, {'data': updated_record}


def delete(request, space_id, id):
    result = db_utils.delete(space_id, domain, {'_id': id}, request.user_id)
    return 200, {'deleted_count': result.deleted_count}


def find_by_id(request, space_id, id):
    data = db_utils.find(space_id, domain, {'_id': id})
    return 200, {'data': data}


# TBD deprecated should be removed
def find_all_custom_domains(space_id):
    return db_utils.find(space_id, domain, {})

def get_by_project_and_custom(space_id, project_id, custom_name):
    data = db_utils.find(space_id, domain, {"projectId": project_id, "name": custom_name})
    if len(data) == 1:
        return data[0]
    else:
        return None
