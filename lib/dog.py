from sqlalchemy import create_engine

from models import Dog


engine = create_engine('sqlite:///memory:')


def create_table(base):
    base.metadata.create_all(engine)
    return engine


def save(session, dog):
    pass


def get_all(session):
    pass


def find_by_name(session, name):
    pass


def find_by_id(session, id):
    pass


def find_by_name_and_breed(session, name, breed):
    pass


def update_breed(session, dog, breed):
    pass
