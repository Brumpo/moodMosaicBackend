from index import db, bcrypt
from datetime import datetime

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    fname = db.Column(db.String(255))
    lname = db.Column(db.String(255))
    def __init__(self, email, password, fname, lname):
        self.email = email
        self.active = True
        self.fname = fname
        self.lname = lname
        self.password = Users.hashed_password(password)

    @staticmethod
    def hashed_password(password):
        return bcrypt.generate_password_hash(password).decode("utf-8")

    @staticmethod
    def get_user_with_email_and_password(email, password):
        user = Users.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return None

class Dates(db.Model):
    __tablename__ = 'dates'
    id = db.Column(db.Integer(), primary_key=True)
    day = db.Column(db.Integer(), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    userId = db.Column(db.Integer(), nullable=False)
    atAGlance = db.Column(db.VARCHAR(3000))
    journal = db.Column(db.VARCHAR(3000))

    def __init__(self,userId,day,year,atAGlance,journal):
        self.day = day
        self.year = year
        self.userId = userId
        self.atAGlance = atAGlance
        self.journal = journal

    def serialize(self):
        return{
            'day' : self.day,
            'year' : self.year,
            'userId' : self.userId,
            'atAGlance' : self.atAGlance,
            'journal' : self.journal,
        }
    @staticmethod
    def get_user_journal_on_date(userId, startDate, endDate):
        data = Dates.query.filter(db.Dates.userId==userId, db.Dates.date>=startDate , db.Dates.date<= endDate)
        return data
