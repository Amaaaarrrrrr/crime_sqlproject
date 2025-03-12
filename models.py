from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from database import Base, engine

Session=sessionmaker(bind=engine)

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
    detectives = relationship("Detective", back_populates="cases", secondary=detective_case, cascade="all, delete")

    #CRUD operations
    @classmethod
    def create(cls, crime_type, status, location, date):  #creates a new case
        session=Session()
        new_case=cls(crime_type=crime_type, status=status, location=location, date=date)
        session.add(new_case)
        session.commit()
        session.close()
        print("Case added successfully")
    
    @classmethod
    def get_all(cls): #retrieves all cases
        session=Session()
        cases= session.query(cls).all()
        session.close()
        return cases

    @classmethod
    def find_by_id(cls, case_id):  #retrieves cases by id
        session = Session()
        case = session.query(cls).filter_by(id=case_id).first()
        session.close()
        return case

    @classmethod
    def delete(cls, case_id):  #deletes cases by id
        session = Session()
        case = session.query(cls).filter_by(id=case_id).first()
        if case:
            session.delete(case)
            session.commit()
            print("Case deleted successfully!")
        else:
            print("Case not found!")
        session.close()


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
    criminal_record= relationship("CriminalRecord", back_populates="suspect", uselist=False)

    #crud operation
    @classmethod
    def create(cls, name, age, alibi, case_id):
        session = Session()
        new_suspect = cls(name=name, age=age, alibi=alibi, case_id=case_id)
        session.add(new_suspect)
        session.commit()
        session.close()
        print("Suspect added successfully!")

    @classmethod
    def get_all(cls):
        session = Session()
        suspects = session.query(cls).all()
        session.close()
        return suspects

    @classmethod
    def find_by_id(cls, suspect_id):
        session = Session()
        suspect = session.query(cls).filter_by(id=suspect_id).first()
        session.close()
        return suspect

    @classmethod
    def delete(cls, suspect_id):
        session = Session()
        suspect = session.query(cls).filter_by(id=suspect_id).first()
        if suspect:
            session.delete(suspect)
            session.commit()
            print("Suspect deleted successfully!")
        else:
            print("Suspect not found!")
        session.close()

    


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

    #crud operations
    @classmethod
    def create(cls, description, found_location, case_id):
        session = Session()
        new_evidence = cls(description=description, found_location=found_location, case_id=case_id)
        session.add(new_evidence)
        session.commit()
        session.close()
        print("Evidence added successfully!")

    @classmethod
    def get_all(cls):
        session = Session()
        evidences = session.query(cls).all()
        session.close()
        return evidences

    @classmethod
    def find_by_id(cls, evidence_id):
        session = Session()
        evidence = session.query(cls).filter_by(id=evidence_id).first()
        session.close()
        return evidence

    @classmethod
    def delete(cls, evidence_id):
        session = Session()
        evidence = session.query(cls).filter_by(id=evidence_id).first()
        if evidence:
            session.delete(evidence)
            session.commit()
            print("Evidence deleted successfully!")
        else:
            print("Evidence not found!")
        session.close()

pass

#detective class
class Detective(Base):
    __tablename__="detectives"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rank = Column(String, default="Junior")
    solved_cases = Column(Integer, default=0)

    #relationship(cases-detectives(many-many))
    cases = relationship("Case", back_populates="detectives", secondary=detective_case, cascade="all, delete")


    #crud operations
    @classmethod
    def create(cls, name, rank, solved_cases=0):  #add new detective
        session=Session()
        new_detective= cls(name=name, rank=rank, solved_cases=solved_cases)
        session.add(new_detective)
        session.commit()
        session.close()
        print("New detective added successfully")

    @classmethod
    def get_all(cls):
        session=Session()
        detectives =session.query(cls).all()
        session.close()
        return detectives
    
    @classmethod
    def find_by_id(cls, detective_id):
        session=Session()
        detective= session.query(cls).filter_by(id=detective_id).first()
        session.close()
        return detective
    
    @classmethod
    def delete(cls, detective_id):
        session=Session()
        detective = session.query(cls).filter_by(id=detective_id).first()
        if detective:
            session.delete(detective)
            session.commit()
            print("Detective deleted successfully!")
        else:
            print("Detective not found!")
        session.close()


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

    #crud operation
    @classmethod
    def create(cls, suspect_id, previous_crimes, sentence):
        session = Session()
        new_record = cls(suspect_id=suspect_id, previous_crimes=previous_crimes, sentence=sentence)
        session.add(new_record)
        session.commit()
        session.close()
        print("Criminal record added successfully!")

    @classmethod
    def get_all(cls):
        session = Session()
        records = session.query(cls).all()
        session.close()
        return records

    @classmethod
    def find_by_id(cls, record_id):
        session = Session()
        record = session.query(cls).filter_by(id=record_id).first()
        session.close()
        return record

    @classmethod
    def delete(cls, record_id):
        session = Session()
        record = session.query(cls).filter_by(id=record_id).first()
        if record:
            session.delete(record)
            session.commit()
            print("Criminal record deleted successfully!")
        else:
            print("Criminal record not found!")
        session.close()


# Create tables in the database
Base.metadata.create_all(engine)

