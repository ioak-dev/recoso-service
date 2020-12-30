from app.space.service import get_all_spaces
import app.project.service as project_service
import app.sequence.service as sequence_service

def run():
    spaces = get_all_spaces()
    for space in spaces:
        projects = project_service.find_all_projects(space['name'])
        for project in projects:
            if sequence_service.is_present(space['name'], 'taskOrder', project['_id']) == False:
                sequence_service.create_sequence(space['name'], 'taskOrder', project['_id'], 1)
                sequence_service.create_sequence(space['name'], 'taskId', project['_id'], 1)
            if sequence_service.is_present(space['name'], 'stageOrder', project['_id']) == False:
                sequence_service.create_sequence(space['name'], 'stageOrder', project['_id'], 1)
            if sequence_service.is_present(space['name'], 'epicColor', project['_id']) == False:
                sequence_service.create_sequence(space['name'], 'epicColor', project['_id'], 1)
