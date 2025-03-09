from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#creating the engine and sessiom
engine= create_engine("sqlite:///crime.db")
Session= sessionmaker(bind=engine)
session= Session()

#base class
Base= declarative_base()