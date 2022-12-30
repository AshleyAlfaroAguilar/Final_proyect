import datetime

class Form():
    def __init__(self, id ,identify_card=None, name=None, direction=None, gender=None, phone_number=None, birth_date=None, career=None, genre=None, register_date=None, participation_date=None, age=None):
        self.id= id
        self.identify_card = identify_card
        self.name = name 
        self.direction = direction 
        self.gender= gender
        self.phone_number = phone_number
        self.birth_date = birth_date
        self.career = career
        self.genre= genre
        self.register_date = datetime.datetime.today()
        self.participation_date = participation_date
        self.age = age

class list():
    def __init__(self, identify_card=None, name=None, direction=None, gender=None, phone_number=None, birth_date=None, career=None, genre=None, register_date=None, participation_date=None, age=None):
        self.identify_card = identify_card
        self.name = name
        self.direction = direction
        self.gender = gender
        self.phone_number = phone_number
        self.birth_date = birth_date
        self.career = career
        self.genre = genre
        self.register_date = register_date
        self.participation_date = participation_date
        self.age = age

    def to_json(self):
        return{
            #'carnet': self.carnet,
            'name': self.name,
            #'address': self.address,
            #'gender': self.gender,
            #'phone_number': self.phone_number,
            #'birth_date': self.birth_date,
            'career': self.career,
            'genre': self.genre,
            #'ins_date': self.ins_date,
            'participation_date': self.participation_date,
            'age': self.age 
        }
        