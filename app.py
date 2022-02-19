from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from datetime import date, datetime
from sqlalchemy import or_, and_

port = int(os.environ.get('PORT', 5000))
app = Flask(__name__)

app.config.from_object("config.DevelopmentConfig")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Users
from models import Account



@app.route("/")
def hello():
    return "Hello World!"


@app.route("/user", methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        user_name = request.json.get('user_name')
        account_number = request.json.get('account_number')
        try:
            user = Users(
                user_name=user_name,
                account_number=account_number
            )
            db.session.add(user)
            db.session.commit()
            return "User added. user id={}".format(user.id)
        except Exception as e:
            return str(e)
    else:
        # user_mapped = Users.query.filter(Users.account_number == 123123123123).first()
        # print(user_mapped.id)
        # print(user_mapped.user_name)
        # print(user_mapped.account_number)
        all_users = Users.query.all()
        return jsonify([e.serialize() for e in all_users])


@app.route("/account", methods=['POST'])
def add_account():
    try:
        account_number = request.json.get('Account No')
        date = request.json.get('Date')
        transaction_details = request.json.get('Transaction Details')
        value_date = request.json.get('Value Date')
        withdraw_amount = request.json.get('Withdrawal AMT')
        deposit_amount = request.json.get('Deposit AMT')
        balance_amount = request.json.get('Balance AMT')
        user_mapped = Users.query.filter(Users.account_number == account_number).first()
        print(user_mapped)
        account_trans_user = Account(
            account_number_id=user_mapped.id,
            date=date,
            transaction_details=transaction_details,
            value_date=value_date,
            withdraw_amount=withdraw_amount,
            deposit_amount=deposit_amount,
            balance_amount=balance_amount
        )
        db.session.add(account_trans_user)
        db.session.commit()
        return "account transaction added for this user {}".format(user_mapped.user_name)
    except Exception as e:
        return str(e)


@app.route("/<user>/transactions/<date>", methods=['GET'])
def transactions_user_date(user=None, date=None):
    try:
        date_process = str(datetime.strptime(date, '%d-%m-%y').strftime("%d %b %y"))
        # print(date,date_process)
        user_mapped = Users.query.filter(Users.user_name == user).first()
        account_mapped = Account.query.filter(and_(
            Account.account_number_id == user_mapped.id, Account.date == date_process)).all()
        return jsonify([e.serialize() for e in account_mapped])
    except Exception as e:
        return str(e)


@app.route("/<user>/details/<ID>", methods=['GET'])
def transactions_user_id(user=None, ID=None):
    try:
        user_mapped = Users.query.filter(Users.user_name == user).first()
        account_mapped = Account.query.filter(and_(
            Account.account_number_id == user_mapped.id, Account.id == int(ID))).first()
        return jsonify([account_mapped.serialize()])
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
