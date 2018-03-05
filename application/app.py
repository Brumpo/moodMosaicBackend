from flask import request, jsonify, url_for, redirect, g
from .models import Users, Dates
from index import app, db
from sqlalchemy.exc import IntegrityError
from .utils.auth import generate_token, requires_auth, verify_token
from flask import Flask
from flask_cors import CORS

@app.route('/', methods=['GET'])
def index():
    return request.query_string

@app.route('/api/dates',methods=['GET'])
def get_date_by_frame():
    queryParams = request.query_string.split('=')
    userId = queryParams[2].split('&')[0]
    startDate = queryParams[3].split('&')[0]
    endDate = queryParams[4].split('&')[0]
    Dates.get_user_journal_on_date(userId=userId, startDate=startDate, endDate=endDate)

@app.route('/api/create_date', methods=['POST'])
def create_date():
    incoming = request.get_json()
    date = Dates(
        userId=incoming["userId"],
        day=incoming["day"],
        year=incoming["year"],
        atAGlance=incoming["atAGlance"],
        journal=incoming["journal"]
    )
    db.session.add(date)
    db.session.commit()
    return jsonify({'data': Dates.serialize(date)})

@app.route('/api/test/', methods=['GET'])
def get_dates():
    print('test')
    a,b,c,d = request.query_string.split('=')
    userId = b.split('&')[0]
    atAGlance = c.split('&')[0]
    journal = d.split('&')[0]
    date = Dates(userId=userId,atAGlance=atAGlance,journal=journal)
    db.session.add(date)
    db.session.commit()
    return jsonify({'data': Dates.serialize(date)})

@app.route("/api/user", methods=["GET"])
@requires_auth
def get_user():
    return jsonify(result=g.current_user)



@app.route("/api/create_user", methods=["POST"])
def create_user():
    incoming = request.get_json()
    user = Users(
        email=incoming["email"],
        password=incoming["password"],
        fname=incoming["fname"],
        lname=incoming["lname"]
    )
    db.session.add(user)

    try:
        db.session.commit()
    except IntegrityError:
        return jsonify(message="User with that email already exists"), 409

    new_user = Users.query.filter_by(email=incoming["email"]).first()

    return jsonify(
        id=user.id,
        token=generate_token(new_user)
    )


@app.route("/api/get_token", methods=["POST"])
def get_token():
    incoming = request.get_json()
    user = Users.get_user_with_email_and_password(incoming["email"], incoming["password"])
    if user:
        return jsonify(token=generate_token(user))

    return jsonify(error=True), 403


@app.route("/api/is_token_valid", methods=["POST"])
def is_token_valid():
    incoming = request.get_json()
    is_valid = verify_token(incoming["token"])

    if is_valid:
        return jsonify(token_is_valid=True)
    else:
        return jsonify(token_is_valid=False), 403
