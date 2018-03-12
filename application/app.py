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

@app.route('/api/dates/',methods=['GET'])
def get_date_by_frame():
    queryParams = request.query_string.split('=')
    userId = queryParams[1].split('&')[0]
    year = queryParams[2].split('&')[0]
    startDate = queryParams[3].split('&')[0]
    endDate = queryParams[4]
    results = Dates.get_user_journal_on_date(userId=userId, year=year, startDate=startDate, endDate=endDate)
    data = []
    for result in results:
        data.append(Dates.serialize(result))
    return jsonify({'data': data})

@app.route('/api/create_date', methods=['POST'])
def create_date():
    incoming = request.get_json()
    date = Dates(
        userId=incoming["userId"],
        day=incoming["day"],
        year=incoming["year"],
        x1 = incoming["x1"],
        x2 = incoming["x2"],
        x3 = incoming["x3"],
        x4 = incoming["x4"],
        x5 = incoming["x5"],
        x6 = incoming["x6"],
        summary=incoming["summary"],
        journal=incoming["journal"]
    )
    db.session.add(date)
    db.session.commit()
    return jsonify({'data': Dates.serialize(date)})

@app.route('/api/test/', methods=['GET'])
def get_dates():
    return('test')

@app.route("/api/user/", methods=["GET"])
@requires_auth
def get_user():
    a,b = request.query_string.split('=')
    userId = b.split('&')[0]
    user = Users.get_current_AaG(userId)
    return jsonify({'data': Users.serialize(user)})


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
        return jsonify(
            id=user.id,
            token=generate_token(user)
        )

    return jsonify(error=True), 403


@app.route("/api/is_token_valid", methods=["POST"])
def is_token_valid():
    incoming = request.get_json()
    is_valid = verify_token(incoming["token"])

    if is_valid:
        return jsonify(token_is_valid=True)
    else:
        return jsonify(token_is_valid=False), 403
