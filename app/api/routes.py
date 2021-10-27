from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Habit, habit_schema, habits_schema, task_schema, tasks_schema

api = Blueprint('api',__name__, url_prefix='/api')