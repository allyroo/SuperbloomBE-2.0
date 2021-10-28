from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import Task, db, User, Habit, habit_schema, habits_schema, task_schema, tasks_schema

api = Blueprint('api',__name__, url_prefix='/api')

################################
#             HABITS           #
################################


# create habit endpoint
@api.route('/habit', methods = ['POST'])
@token_required
def create_habit(current_user_token): 
    smart_goal = request.json['smart_goal']
    habit_category = request.json['habit_category']
    date_created = request.json['date_created']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    habit = Habit( smart_goal,habit_category,date_created, user_token = user_token )

    db.session.add(habit)
    db.session.commit()

    response = habit_schema.dump(habit)
    return jsonify(response)


# retrieve ALL habit endpoints
@api.route('/habit', methods = ['GET'])
@token_required
def get_habits(current_user_token):
    owner = current_user_token.token
    habit = Habit.query.filter_by(user_token = owner).all()
    response = habits_schema.dump(habit)
    return jsonify(response)


# retrieve ONE habit endpoint
@api.route('/habit/<id>', methods = ['GET'])
@token_required
def get_habit(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        habit = Habit.query.get(id)
        response = habit_schema.dump(habit)
        return jsonify(response)
    else:
        return jsonify({"message": "Valid Token Required"}),401


# update habit endpoint
@api.route('/habit/<id>', methods = ['PUT'])
@token_required
def update_habit(current_user_token,id):
    habit = Habit.query.get(id) 

    habit.smart_goal = request.json['smart_goal']
    habit.habit_category = request.json['habit_category']
    habit.habit_date = request.json['habit_date']
    habit.user_token = current_user_token.token

    db.session.commit()
    response = habit_schema.dump(habit)
    return jsonify(response)


# delete habit endpoint
@api.route('/habit/<id>', methods = ['DELETE'])
@token_required
def delete_habit(current_user_token, id):
    habit = Habit.query.get(id)
    db.session.delete(habit)
    db.session.commit()
    response = habit_schema.dump(habit)
    return jsonify(response)


################################
#             TO-DO            #
################################

# create task

@api.route('/todo', methods = ['POST'])
@token_required
def create_task(current_user_token):
    todo_task = request.json['todo_task']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    task = Task( todo_task, user_token = user_token )

    db.session.add(task)
    db.session.commit()

    response = task_schema.dump(task) #converting python object to JSON object :)
    return jsonify(response)


# retrieve ALL THE TASKS!
@api.route('/todos', methods = ['GET'])
@token_required
def get_task(current_user_token):
    owner = current_user_token.token
    entries = Task.query.filter_by(user_token = owner).all()
    response = habits_schema.dump(entries)
    return jsonify(response)

# delete task endpoint
@api.route('/todo', methods = ['DELETE'])
@token_required
def delete_entry(current_user_token, id):
    entry = Task.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    response = task_schema.dump(entry)
    return jsonify(response)