from flask import Flask
from flask_restful import Api, Resource
import random

app = Flask(__name__)
api = Api(app)


tasks = [1, 2, 3]


class TasksAPI(Resource):

    def get(self):
        return {'tasks': tasks}

    def post(self):
        tasks.append(random.randint(0, 9))
        return {'tasks': tasks}

    def delete(self):
        tasks.remove(tasks[0])
        return {'tasks': tasks}


class TaskCount(Resource):
    def get(self):
        return len(tasks)


api.add_resource(TasksAPI, '/tasks', endpoint='tasks')
api.add_resource(TaskCount, '/tasks/count', endpoint='count')

if __name__ == '__main__':
    app.run(debug=True)