import uuid 
from typing import Dict,List
from models.items import Item
from models.model import Model
# from common.database import Database
from models.user.users import User
from libs.mailgum import Mailgun



from dataclasses import dataclass, field # this is to convert Alert class to dataclass

# to convert class to dataclass use @dataclass decorator
@dataclass(eq=False) # eq=False remove ability to compare with == to different obj. init=False will remove ability to define init automatically
class Alert(Model):
    # collection = "alerts"
    # " we want collection  as class variable without includeing it in init"
    
    collection:str = field(init=False, default="alerts")
    name:str
    item_id:str 
    price_limit:float 
    user_email:str 
    _id:str = field(default_factory=lambda:uuid.uuid4().hex) # default_factory is to pass any function, it means _id or uuid.uuid4().hex
    
    #" super init is taken care by dataclasses "
    #" but dataclasses cannot access values which are passed to dataclass therefore self.item will not work in dataclasses"
    # for that use extra dunder method called __post_init__()

    def __post_init__(self):
        # this dunder will run after init and so it has item_id  and can be accessed using self.item_id
        self.item = Item.get_by_id(self.item_id) 
        self.user = User.find_by_email(self.user_email)

    # =========================================================================================================

    # def __init__(self, item_id:str, price_limit:float, _id:str=None):
    #     super().__init__()
    #     self.item_id = item_id
    #     self.item = Item.get_by_id(item_id)
    #     self.price_limit = price_limit
    #     self.collection = "alerts"
    #     self._id = uuid.uuid4().hex if _id is None else _id 

    def json(self)->Dict:
        return {
            "name":self.name,
            "item_id":self.item_id,
            "price_limit":self.price_limit,
            "_id":self._id,
            "user_email":self.user_email
        }

    # def add(self):
    #     Database.insert(self.collection,data=self.json()) 

    def loadItemPrice(self):
        self.item.load_price() # it will load the price from website
        return self.item.price 

    def notifyIfPriceReached(self):
        if self.item.price < self.price_limit:
            print(f"{self.item.name}'s price reached low value {self.item.price}")
            Mailgun.send_mail(
                [self.user_email],
                f"notification for {self.name}",
                f"Your alert {self.name} has reached a price under {self.price_limit}. The latest price is {self.item.price}. Go to this address to check your item:{self.item.url}",
                "<p>Your alert {self.name} has reached price under {self.price_limit}.</p><p>The Latest Price is {self.item.price}.</p><p>Click <a href='{self.item.url}'>here</a>to perchase your item</p>"

            )
    
    