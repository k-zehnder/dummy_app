import os
from dotenv import load_dotenv
import datetime

from app import create_app, db
from app.models import User
import config as Config

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

def create_context(config=Config):
    # create app context and push it
    app = create_app()
    app.app_context().push()

def create_fake_users(n_users):
    create_context()


def create_random_data(create_db=False, drop_all=False):
    create_context()
    if drop_all:
        db.drop_all()
    if create_db:
        db.create_all()
    u1 = User(
        username="kevin" + str(datetime.datetime.utcnow())
    )
    print(u1)
    db.session.add(u1)
    db.session.commit()

# >>> from app import db
# >>> from app.models import User
# >>> db.create_all()

if __name__ == "__main__":
    # create_random_data() 
    from app import db
    print(dir(db))