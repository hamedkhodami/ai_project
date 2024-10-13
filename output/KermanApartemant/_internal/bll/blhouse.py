from dal.Rapository import rapository
from be.House import house

class HouseService():

    rp=rapository()

    def AddHouse(self,Area,Rooms,Floors,Location,Price):
        obj=house(Area=Area,Rooms=Rooms,Floors=Floors,Location=Location,Price=Price)
        self.rp.add(obj)

    def DeleteHouse(self,id):
        House=self.rp.reedById(house,id)
        if House:
            self.rp.delete(House)

    def ReadHouse(self):
        return self.rp.read(house)

    def GetHouseById(self,id):
        return self.rp.reedById(house,id)

    def UpdateHouse(self,obj,id,**kwargs):
        return self.rp.update(obj,id,**kwargs)




