from index import db, bcrypt
from datetime import datetime

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    fname = db.Column(db.String(255))
    lname = db.Column(db.String(255))
    key1 = db.Column(db.String(255))
    key2 = db.Column(db.String(255))
    key3 = db.Column(db.String(255))
    key4 = db.Column(db.String(255))
    key5 = db.Column(db.String(255))
    key6 = db.Column(db.String(255))

    def __init__(self, email, password, fname, lname, key1, key2, key3, key4, key5, key6):
        self.email = email
        self.active = True
        self.fname = fname
        self.lname = lname
        self.key1 = key1
        self.key2 = key2
        self.key3 = key3
        self.key4 = key4
        self.key5 = key5
        self.key6 = key6
        self.password = Users.hashed_password(password)

    def serialize(self):
        return{
            'email' : self.email,
            'fname' : self.fname,
            'lname' : self.lname,
            'key1' : self.key1,
            'key2' : self.key2,
            'key3' : self.key3,
            'key4' : self.key4,
            'key5' : self.key5,
            'key6' : self.key6,
            'password' : self.password
        }

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

    @staticmethod
    def get_current_AaG(userId):
        AaG = Users.query.filter(Users.id==userId).first()
        return AaG

class Dates(db.Model):
    __tablename__ = 'dates'
    id = db.Column(db.Integer(), primary_key=True)
    day = db.Column(db.Integer(), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    userId = db.Column(db.Integer(), nullable=False)
    x1 = db.Column(db.VARCHAR(3000))
    x2 = db.Column(db.VARCHAR(3000))
    x3 = db.Column(db.VARCHAR(3000))
    x4 = db.Column(db.VARCHAR(3000))
    x5 = db.Column(db.VARCHAR(3000))
    x6 = db.Column(db.VARCHAR(3000))
    summary = db.Column(db.VARCHAR(3000))
    journal = db.Column(db.VARCHAR(3000))

    def __init__(self,userId,day,year,x1,x2,x3,x4,x5,x6,summary,journal):
        self.day = day
        self.year = year
        self.userId = userId
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.x5 = x5
        self.x6 = x6
        self.summary = summary
        self.journal = journal

    def serialize(self):
        return{
            'day' : self.day,
            'year' : self.year,
            'userId' : self.userId,
            'x1' : self.x1,
            'x2' : self.x2,
            'x3' : self.x3,
            'x4' : self.x4,
            'x5' : self.x5,
            'x6' : self.x6,
            'summary' : self.summary,
            'journal' : self.journal,
        }

    @staticmethod
    def get_user_journal_on_date(userId, startDate, endDate, year):
        data = Dates.query.filter(Dates.userId==userId, Dates.year==year, Dates.day >= startDate , Dates.day <= endDate).all()
        return data
