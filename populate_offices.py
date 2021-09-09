from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

import json

engine = create_engine('sqlite:///flag.db')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Offices(Base):
    __tablename__ = 'offices'
    
    usa_state = Column(String(10))
    office_code = Column(String(10), primary_key=True, nullable=False)
 
def populate_offices():
    with open('offices.json',) as offices_json:
        offices = json.load(offices_json)
    for office in offices:
        usa_state = office['usa_state']
        office_code = office['office_code']

        session.add(Offices(usa_state = usa_state, office_code=office_code))
    session.commit()
 
if __name__ == '__main__':
    populate_offices()