from abc import abstractclassmethod, ABCMeta
from typing import List, TypeVar, Type # types are for connecting cls with return value of function
from typing import Union,Dict
from common.database import Database


T = TypeVar("T",bound='Model')

class Model(metaclass=ABCMeta):
    # collection = "models"
    collection: str  # it tells collection exists but not define yet and it force to child class to have this property otherwise it throw error
    _id: str 

    def __init__(self,*args, **kwargs):
        ''' constructor is for avoiding warnings 
            we can't create instances of class containing abstract methods '''
        pass 

    
    def save(self):
        ''' This will find using _id and update if not find _id then it will add new item 
            self.collection can access cls.collection '''
        Database.update(self.collection,{"_id":self._id},self.json())

    def remove(self):
        Database.remove(self.collection,{"_id":self._id})


    @abstractclassmethod
    def json(self):
        raise NotImplementedError

    @classmethod
    def getAll(cls:Type[T]) -> List[T]: # this function was common in both alert and items class
        elements = Database.find(cls.collection,{}) # cls.collection is not defined in Model class but it's child class have this cls.collection
        return [cls(**element) for element in elements]

    @classmethod
    # def get_by_id(cls,_id:str)->"Model": # Item.get_by_id -> Item ; Alert.get_by_id -> Alert
    # cls and Model are not tie together means if cls got items it will not change Model to Items to do that we need to connect them
    def get_by_id(cls: Type[T],_id:str)->T:
        return cls.find_one_by("_id",_id)

    @classmethod 
    def find_one_by(cls:Type[T],attribute:str,value:Union[str,Dict])->T:
        object =Database.find_one(cls.collection,{attribute:value})
        print("class:",cls)
        print(f"query:{attribute}:{value}")
        print("object:",object)
        return cls(**object)

    @classmethod
    def find_many_by(cls:Type[T],attribute:str,value:str)->List[T]:
        ''' using attribute and value it will return all objects related to it '''
        return [cls(**element)for element in Database.find(cls.collection,{attribute:value})]

    