from __main__ import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(), nullable=False)
    account_number = db.Column(db.BigInteger, unique=True, nullable=False)
    account = db.relationship('Account', backref='users', lazy=True)

    # account_number = db.Column(db.BigInteger(), db.ForeignKey('accounts.account_number'),
    #                            nullable=False)
    def __init__(self, user_name, account_number):
        self.user_name = user_name
        self.account_number = account_number

    def __repr__(self):
        return f"id:{self.id} user_name:{self.user_name} account_number:{self.account_number}"

    def serialize(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'account_number': self.account_number
        }


class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    # account_number = db.relationship('Users', backref='Accounts', lazy=True)
    account_number_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                                  nullable=False)
    date = db.Column(db.String())
    transaction_details = db.Column(db.String())
    value_date = db.Column(db.String())
    withdraw_amount = db.Column(db.String())
    deposit_amount = db.Column(db.String())
    balance_amount = db.Column(db.String())

    def __init__(self, account_number_id, date, transaction_details, value_date, withdraw_amount, deposit_amount,
                 balance_amount):
        self.account_number_id = account_number_id
        self.date = date
        self.transaction_details = transaction_details
        self.value_date = value_date
        self.withdraw_amount = withdraw_amount
        self.deposit_amount = deposit_amount
        self.balance_amount = balance_amount

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'account_number_id': self.account_number_id,
            'date': self.date,
            'transaction_details': self.transaction_details,
            'value_date': self.value_date,
            'withdraw_amount': self.withdraw_amount,
            'deposit_amount': self.deposit_amount,
            'balance_amount': self.balance_amount
        }
