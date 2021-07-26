import uuid 
from typing import Dict,List
from models.items import Item
from models.model import Model
from common.database import Database

class Alert(Model):
    collection = "alerts"
    def __init__(self, item_id:str, price_limit:float, _id:str=None):
        super().__init__()
        self.item_id = item_id
        self.item = Item.getById(item_id)
        self.price_limit = price_limit
        self.collection = "alerts"
        self._id = uuid.uuid4().hex if _id is None else _id 

    def json(self)->Dict:
        return {
            "item_id":self.item_id,
            "price_limit":self.price_limit,
            "_id":self._id 
        }

    def add(self):
        Database.insert(self.collection,data=self.json()) 

    def loadItemPrice(self):
        self.item.load_price() # it will load the price from website
        return self.item.price 

    def notifyIfPriceReached(self):
        if self.item.price < self.price_limit:
            print(f"{self.item.name}'s price reached low value {self.item.price}")
    
    