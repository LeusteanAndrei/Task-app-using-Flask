from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from User import  User
from Comment import Comment
from Task import Task
from datetime import datetime

app = Flask(__name__)
api = Api(app)

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = User.get_user(user_id)
            if user:
                return jsonify(user)
            else:
                return {'error_message': 'User not found'}, 404
        else:
            users = User.get_users()
            return jsonify(users)
    
    def post(self):
        new_user = request.get_json()
        try:
            User.create_user(new_user['username'], new_user['email'], new_user['password'])
            return {'message': 'User created successfully'}, 201
        except Exception as e:
            return {'error_message': str(e)}, 400

    def delete(self, user_id):
        try:
            User.delete_user(user_id)
            return {'message': 'User deleted successfully'}, 200
        except Exception as e:
            return {'error_message': str(e)}, 400

class TaskResource(Resource):
    def get(self, task_id=None):
        if task_id:
            task = Task.get_task(task_id)
            if task:
                return jsonify(task)
            else:
                return {'error_message': 'Task not found'}, 404
        else:
            tasks = Task.get_tasks()
            return jsonify(tasks)
    
    def delete(self, task_id):
        try:
            Task.delete_task(task_id)
            return {'message': 'Task deleted successfully'}, 200
        except Exception as e:
            return {'error_message': str(e)}, 400

    def post(self):
        new_task = request.get_json()
        try:
            if 'due_date' not in new_task:
                new_task['due_date'] = None
            if 'responsabil' not in new_task:
                new_task['responsabil'] = None
            if 'parent_id' not in new_task:
                new_task['parent_id'] = None
            if 'descriere' not in new_task:
                new_task['descriere'] = None
            Task.create_task(titlu=new_task['titlu'], descriere=new_task['descriere'],
                                 due_date=new_task['due_date'],responsabil=new_task['responsabil'], parent_id=new_task.get('parent_id'))
            return {'message': 'Task created successfully'}, 201
        except Exception as e:
            return {'error_message': str(e)}, 400
        
class CommentResource(Resource):
    def get(self, comment_id=None):
        if comment_id:
            comment = Comment.get_comment(comment_id)
            if comment:
                return jsonify(comment)
            else:
                return {'error_message': 'Comment not found'}, 404
        else:
            comments = Comment.get_comments()
            return jsonify(comments)
    
    def post(self):
        new_comment = request.get_json()
        try:
            Comment.create_comment(new_comment['task_id'], new_comment['user_id'], new_comment['comment'])
            return {'message': 'Comment created successfully'}, 201
        except Exception as e:
            return {'error_message': str(e)}, 400

    def delete(self, comment_id):
        try:
            Comment.delete_comment(comment_id)
            return {'message': 'Comment deleted successfully'}, 200
        except Exception as e:
            return {'error_message': str(e)}, 400

api.add_resource(UserResource, '/users', '/users/<int:user_id>')
api.add_resource(TaskResource, '/tasks', '/tasks/<int:task_id>')
api.add_resource(CommentResource, '/comments', '/comments/<int:comment_id>')


if __name__ == '__main__':
    app.run(debug=True)