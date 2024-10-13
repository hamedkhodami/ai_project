from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine= create_engine("mssql+pyodbc://@./HousePriceProphet?driver=ODBC+Driver+17+for+SQL+Server")
Session=sessionmaker(bind=engine)


class rapository():

    def add(self,obj):
        session = Session()
        try:
            session.add(obj)
            session.commit()
        finally:
            session.close()

    def delete(self,obj):
        session = Session()

        try:
            session.delete(obj)
            session.commit()
            return True
        except:
            return False
        finally:
            session.close()

    def read(self,obj):
        session = Session()
        try:
            session.query(obj).all()
        finally:
            session.close()
    def reedById(self,obj,id):
        session = Session()
        try:
            session.query(obj).filter(obj.id==id).first()
        finally:
            session.close()

    def update(self,obj,id,**kwargs):
        session = Session()
        try:
            objects=self.reedById(obj,id)
            for key,val in kwargs.items():
                setattr(objects,key,val)
            session.commit()
        finally:
            session.close()
