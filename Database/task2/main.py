import os
from sqlalchemy import create_engine, Connection
from models import Base, Account
from flask import Flask

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'bank.db'))

ACCOUNTS = [
        ('ACC-1001', 5000.0, 'active'),
        ('ACC-1002', 3000.0, 'active'),
        ('ACC-2001', 10000.0, 'frozen')  # 冻结账户
    ]

def init_database():
    Base.metadata.create_all(engine)
    conn = engine.connect()
    return conn

def create_account(conn: Connection):
    for account_number, balance, status in ACCOUNTS:
        conn.execute(
            Account.__table__.insert().values(
                account_number=account_number,
                balance=balance,
                status=status
            )
        )

if __name__ == '__main__':
    _conn = init_database()
    create_account(_conn)
    app.run(debug=True)