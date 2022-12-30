from flask import Blueprint, jsonify, request
from entities import Form
import datetime
from model import FormModel, ListModel
from dateutil.relativedelta import relativedelta
from age import Age

StudentForm_main= Blueprint('StudentForm_blueprints', __name__)
StudentList_main = Blueprint('StudentList_blueprints',__name__)

@StudentList_main.route('/list',methods = ['GET'])
def list_students():
    try:
        students= ListModel.get_students()
        return jsonify(students)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500


@StudentForm_main.route('/',methods = ['POST'])
def form():
    try:
        identify_card = request.json['identify_card']
        name = request.json['name']
        direction = request.json['direction']
        gender= request.json['gender']
        phone_number= request.json['phone_number']
        birth_date=request.json['birth_date']
        career= request.json['career']
        genre =request.json['genre']
        participation_date=request.json['participation_date']

        if not val_identify_card(identify_card):
            return jsonify({'message': 'Carnet invalido'}), 400
        else:
            if not val_birth_date(birth_date):
                return jsonify({'message': 'es menor de edad'}), 400
            else:
                today = datetime.datetime.now()
                if identify_card[5] == '1' and genre == 'poesia dramatica':
                    days_inc = 5
                    while days_inc > 0:
                        today += datetime.timedelta(days=1)
                        if today.weekday() not in (5, 6):
                            days_inc -= 1
                elif identify_card[5] == '3' and genre == 'poesia epica':
                    month_last_day = (datetime.datetime(today.year, today.month, 1) - datetime.timedelta(days=1)).day
                    today = datetime.datetime(today.year, today.month, month_last_day)
                    while today.weekday() in (5, 6):
                        today -= datetime.timedelta(days=1)
                else: 
                    while today.weekday() != 4:
                        today += datetime.timedelta(days=1)      
                participation_date = today.strftime('%Y-%m-%d')
                edad = Age(birth_date)
                age = edad.years
                form = Form("", identify_card, name, direction, gender, phone_number, birth_date, career, genre, "", participation_date, age )
                affected_row = FormModel.form(form)
                if affected_row == 1:
                    return jsonify('Agregado')
                else: 
                        return None
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

def val_identify_card(identify_card):
            if len(identify_card) != 6:
                return False
            if identify_card[0].upper() != 'A':
                return False
            if identify_card[2] != '5':
                return False
            if identify_card[-1] not in ('1','3','9'):
                return False
            return True
def val_birth_date(birth_date):
    try:
        birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d')
    except ValueError:
        return False
    today = datetime.datetime.now()
    return (today - birth_date).days // 365 >= 17

