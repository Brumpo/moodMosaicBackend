from index import db, bcrypt
from datetime import datetime

class User(db.Model):
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
        self.password = User.hashed_password(password)

    @staticmethod
    def hashed_password(password):
        return bcrypt.generate_password_hash(password).decode("utf-8")

    @staticmethod
    def get_user_with_email_and_password(email, password):
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return None

class Date(db.Model):
    __tablename__ = 'dates'
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.DateTime(), default=datetime.utcnow())
    userId = db.Column(db.Integer(), nullable=True, )
    atAGlance = db.Column(db.VARCHAR(3000))
    journal = db.Column(db.VARCHAR(3000))

    def __init__(self,userId,atAGlance,journal):
        self.date = datetime.utcnow()
        self.userId = userId
        self.atAGlance = atAGlance
        self.journal = journal

    def serialize(self):
        return{
            'date' : self.date,
            'userId' : self.userId,
            'atAGlance' : self.atAGlance,
            'journal' : self.journal,
        }
    @staticmethod
    def get_user_journal_on_date(userId, startDate, endDate):
        data = Date.query.filter(db.Date.userId==userId, db.Date.date>=startDate , db.Date.date<= endDate)
        return data
