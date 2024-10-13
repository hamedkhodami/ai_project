from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import declarative_base,session


Base=declarative_base()


class house(Base):
    __tablename__="house"
    Id=Column(Integer,primary_key=True)
    Area=Column(Integer)
    Rooms=Column(Integer)
    Floors=Column(Integer)
    Location=Column(String(50))
    Price=Column(Integer)

    def __init__(self,Area,Rooms,Location,Price):
        self.Area=Area
        self.Rooms=Rooms
        self.Location=Location
        self.Price=Price

    def __repr__(self):
        return f"house(ID: {self.Id},Area: {self.Area},Rooms: {self.Rooms},Location: {self.Location},Price: {self.Price})"


engine= create_engine("mssql+pyodbc://@./HousePriceProphet?driver=ODBC+Driver+17+for+SQL+Server")
Base.metadata.create_all(engine)