from sqlalchemy import Column, Integer, String, Text, VARCHAR, TIMESTAMP, ForeignKey, Table
from pydantic import BaseModel
from .db import Base
from sqlalchemy.orm import relationship


# Промежуточная таблица для связи "многие ко многим"
service_record = Table('service_record', Base.metadata,
    Column('record_id', Integer, ForeignKey('record.id'), primary_key=True),
    Column('service_id', Integer, ForeignKey('service.id'), primary_key=True)
)

class BarberSchema(Base):
    __tablename__ = "barber"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    experience_years = Column(Integer)
    working_hours_start = Column(Text)
    working_hours_stop = Column(Text)
    working_days_start = Column(Integer)
    working_days_stop = Column(Integer)
    records = relationship('RecordSchema', backref='barber')
    
class CreateBarberRequest(BaseModel):
    first_name: str
    last_name: str
    experience_years: int
    working_hours_start: str
    working_hours_stop: str
    working_days_start: int
    working_days_stop: int



class ClientSchema(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(Text)
    last_name = Column(Text)
    phone = Column(VARCHAR)
    records = relationship('RecordSchema', backref='client')
    
class CreateClientRequest(BaseModel):
    first_name: str
    last_name: str
    phone: VARCHAR



class ServiceSchema(Base):
    __tablename__ = "service"

    id = Column(Integer, primary_key=True, autoincrement=True)   
    name = Column(Text)
    price = Column(Integer)
    duration = Column(Integer)
    records = relationship('RecordSchema', secondary=service_record, backref='services')

class CreateServiceRequest(BaseModel):
    name: str 
    price: int
    duration: int 



class RecordSchema(Base):
    __tablename__ = "record"

    id = Column(Integer, primary_key=True, autoincrement=True) 
    barber_id = Column(Integer, ForeignKey('barber.id'))
    client_id = Column(Integer, ForeignKey('client.id'))
    datetime = Column(TIMESTAMP)
    barber = relationship('Barber', backref='records')
    client = relationship('Client', backref='records')
    service = relationship('ServiceSchema', secondary=service_record, backref='records')

class CreateRecordRequest(BaseModel):
    barber_id: int
    client_id: int
    datetime: TIMESTAMP





