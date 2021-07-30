import requests 
from bs4 import BeautifulSoup
import re 
from typing import  Dict
import uuid 
from models.model import Model
# from common.database import Database
from dataclasses import dataclass, field

@dataclass(eq=False)
class Item(Model):
    # collection = "items"
    collection:str = field(init=False,default="items")
    url:str 
    tag_name:str
    query:Dict 
    _id:str = field(default_factory=lambda:uuid.uuid4().hex)

    def __post_init__(self):
        self.price = None 


    # def __init__(self, url:str, tag_name: str, query:Dict, name:str="Item", _id:str=None):
    #     super().__init__()
    #     self.name = name
    #     self.url = url 
    #     self.tag_name = tag_name 
    #     self.query = query 
    #     self.price = None
    #     self._id = uuid.uuid4().hex if _id is None else _id

    # def __repr__(self):
    #     return f"Item: {self.name}"

    def json(self)-> Dict:
        return {
            "name":self.name,
            "url":self.url,
            "tag_name":self.tag_name,
            "query":self.query,
            "_id":self._id
        }

    def load_price(self) -> float:
        response = requests.get(url=self.url)
        content = response.content 
        soup = BeautifulSoup(content,"html.parser")
        element = soup.find(self.tag_name,self.query)
        string_price = element.text.strip()

        pattern = re.compile(r"(\d+,?\d*\.?\d?)")
        match = pattern.search(string_price)
        found_price = match.group(1)
        without_commas = found_price.replace(",","")
        self.price = float(without_commas)
        return self.price

    # def add(self):
    #     Database.insert(collection=self.collection,data=self.json())

    # @classmethod
    # def getAll(cls):
    #     ''' this return class object for every item in database '''
    #     items_cursor = Database.find(collection='items',query={})
    #     return [cls(**item) for item in items_cursor]

    # @classmethod 
    # def get_by_id(cls,_id:str)->"Item":
    #     item_json = Database.find_one("items",{"_id":_id})
    #     return cls(**item_json)