import os, datetime, time
import library.db_utils as db_utils

domain = 'sequence'

def is_present(space_id, field, context):
    if len(db_utils.find(space_id, domain, {'field': field, 'context':context})) == 1:
        return True
    return False

def create_sequence(space_id, field, context, factor):
    db_utils.upsert(space_id, domain, {
        'field': field,
        'context': context,
        'nextVal': 1,
        'factor': factor
    })

def reset_sequence(space_id, field, context):
    sequence = db_utils.find(space_id, domain, {'field': field, 'context': context})[0]
    sequence['nextVal'] = 1
    return db_utils.upsert(space_id, domain, sequence)

def nextval(space_id, field, context):
    data = db_utils.find(space_id, domain, {'field': field, 'context': context})[0]
    currVal = data['nextVal']
    data['nextVal'] = data['nextVal'] + data['factor']
    db_utils.upsert(space_id, domain, data)
    return currVal
