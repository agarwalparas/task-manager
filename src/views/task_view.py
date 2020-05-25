from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.task_model import TaskModel, TaskSchema

task_api = Blueprint('task_api', __name__)
task_schema = TaskSchema()


@task_api.route('', methods=['POST'])
@Auth.auth_required
def create():
    """
    Create Task Function
    """
    req_data = request.get_json()
    req_data['owner_id'] = g.user.get('id')
    data = task_schema.load(req_data)
    post = TaskModel(data)
    post.save()
    data = task_schema.dump(post)
    return custom_response(data, 201)

@task_api.route('/', methods=['GET'])
def get_all():
    """
    Get All Tasks
    """
    posts = TaskModel.get_all_tasks()
    data = task_schema.dump(posts, many=True)
    return custom_response(data, 200)

@task_api.route('/<int:task_id>', methods=['GET'])
def get_one(task_id):
    """
    Get A Task
    """
    post = TaskModel.get_one_task(task_id)
    if not post:
        return custom_response({'error': 'task not found'}, 404)
    data = task_schema.dump(post)
    return custom_response(data, 200)

@task_api.route('/<int:task_id>', methods=['PUT'])
@Auth.auth_required
def update(task_id):
    """
    Update A task
    """
    req_data = request.get_json()
    post = TaskModel.get_one_task(task_id)
    if not post:
        return custom_response({'error': 'task not found'}, 404)
    data = task_schema.dump(post)
    if data.get('owner_id') != g.user.get('id'):
        return custom_response({'error': 'permission denied'}, 400)

    data = task_schema.load(req_data, partial=True)
    post.update(data)

    data = task_schema.dump(post)
    return custom_response(data, 200)

@task_api.route('/<int:task_id>', methods=['DELETE'])
@Auth.auth_required
def delete(task_id):
    """
    Delete A Task
    """
    post = TaskModel.get_one_task(task_id)
    if not post:
        return custom_response({'error': 'task not found'}, 404)
    data = task_schema.dump(post)
    if data.get('owner_id') != g.user.get('id'):
        return custom_response({'error': 'permission denied'}, 400)

    post.delete()
    return custom_response({'message': 'deleted'}, 204)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
