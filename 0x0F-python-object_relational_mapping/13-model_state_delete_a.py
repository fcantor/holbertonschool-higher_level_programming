#!/usr/bin/python3
'''
Script that changes the name of a State object
from the database hbtn_0e_6_usa
'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    ''' create an instance of Engine=core interface to the database '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    '''pool_pre_ping tests connections for liveness upon each checkout'''

    ''' create a session '''
    session = sessionmaker(bind=engine)()

    ''' work with session to change object name '''
    result = session.query(State).all()
    for row in result:
        if 'a' in str(row.name):
            session.delete(row)
    session.commit()
    session.close()
