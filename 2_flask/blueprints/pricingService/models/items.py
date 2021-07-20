import requests 
from bs4 import BeautifulSoup
import re 
from typing import Dict
import uuid 


class Item:
    def __init__(self,url:str,tag_name: str,query:Dict,name:str="Item",_id:str=None):
        self.name = name
        self.url = url 
        self.tag_name = tag_name 
        self.query = query 
        self.price = None
        self.collection = 'items'
        self._id = uuid.uuid4.hex if _id is None else _id

    def __repr__(self):
        return f"Item: {self.url}"

    def json(self)-> Dict:
        return {
            "name":self.name,
            "url":self.url,
            "tag_name":self.tag_name,
            "query":self.query,
            "price":self.price,
            "collection":self.collection,
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