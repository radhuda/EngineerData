from sqlalchemy import Column, Integer, String
from database import Base

class Zinc(Base):
    __tablename__ = 'zinc_table'
    smiles = Column(String, primary_key=True)


    def __init__(self, smiles=None):
        self.smiles = smiles


    def __repr__(self):
        return '<_c0 %r>' % (self.flight)