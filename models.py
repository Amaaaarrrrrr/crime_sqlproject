from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base, engine, session

#joint table
detective_case= Table(
    "detective_case",
    Base.metadata,
    Column("detective_id", Integer, ForeignKey("detectives.id")),
    Column("case_id", Integer, ForeignKey("cases.id"))
)
#Case class
class Case(Base):
    __tablename__="cases"
    id =Column(Integer, primary_key=True)
    crime_type = Column(String, nullable=False)
    status = Column(String, default="Open")
    location = Column(String, nullable=False)
    date = Column(String, nullable=False)

    #relationships
    suspects= relationship("Suspect", back_populates="case", cascade="all, delete")
    evidence= relationship("Evidence", back_populates="case", cascade="all, delete")
    detectives= relationship("DEtective", back_populates="cases", secondary=detective_case)

    

pass
#suspect class
class Suspect(Base):
    __tablename__="suspects"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    alibi = Column(String, nullable=True)

    #relationship(case-class(one to many, one to one(suspect-record)))
    case_id =Column(Integer, ForeignKey("cases.id"))
    case = relationship("Case", back_populates="suspects")
    case= relationship("Case", back_populates="suspects")
    criminal_record= relationship("CriminalRecord", back_populates="suspect", uselist=False)


pass
#evidence class
class Evidence(Base):
    __tablename__="evidence"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    found_location = Column(String)

    #relationships(case-evidence(one to many))
    case_id= Column(Integer, ForeignKey("cases.id"))
    case = relationship("Case", back_populates="evidence")

pass

#detective class
class Detective(Base):
    __tablename__="detectives"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rank = Column(String, default="Junior")
    solved_cases = Column(Integer, default=0)

    #relationship(cases-detectives(many-many))
    cases= relationship("Case", back_populates="detectives", secondary=detective_case)

pass
#criminal_record class
class CriminalRecord(Base):
    __tablename__="criminal_records"
    id = Column(Integer, primary_key=True)
    previous_crimes = Column(String)
    sentence = Column(String)

    #relationship(suspect-criminal_record(one to one))
    suspect_id = Column(Integer, ForeignKey("suspects.id"), unique=True)
    suspect= relationship("Suspect", back_populates="criminal_record", uselist=False)


# Create tables in the database
Base.metadata.create_all(engine)

