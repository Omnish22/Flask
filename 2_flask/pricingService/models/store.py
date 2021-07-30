import uuid 
from typing import Dict 
import re 
from models.model import Model 
from dataclasses import dataclass, field 

@dataclass(eq=False)
class Store(Model):
    # collection="store"
    collection:str=field(init=False,default="store")
    name:str 
    url_prefix:str
    tag_name:str 
    query:str 
    _id:str=field(default_factory=lambda:uuid.uuid4().hex)

    # def __init__(self,name:str, url_prefix:str, tag_name:str, query:Dict, _id:str=None):
    #     super().__init__()
    #     self.name = name 
    #     self.url_prefix = url_prefix  # https://www.flipkart.com/
    #     self.tag_name = tag_name
    #     self.query = query 
    #     self._id = _id or uuid.uuid4().hex

    def json(self)->Dict:
        return {
            "_id":self.id,
            "name":self.name,
            "url_prefix":self.url_prefix,
            "tag_name":self.tag_name,
            "query":self.query
        }

    @classmethod
    def get_by_name(cls,store_name:str)->"Store":
        return cls.find_one_by("name",store_name)

    @classmethod
    def get_by_url_prefix(cls,url_prefix:str)->"Store":
        ''' It will find if any url is start with given url_prefix '''
        # mongodb can perform regular expression queries also
        # here $ is for regular expression 
        # this will search on basis of regular expression
        url_regex = {"$regex":"^{}".format(url_prefix)} # all url starts with url_prefix
        # print("url_regex:",url_regex)
        return cls.find_one_by("url_prefix",url_regex) 


    @classmethod
    def find_by_url(cls,url:str)->"Store":
        pattern = re.compile(r"(https?://.*?/)")  # https://www.flipkart.com/
        match = pattern.search(url)
        # print("match:",match)
        url_prefix = match.group(1)
        # print("url_prefix:",url_prefix)
        return cls.get_by_url_prefix(url_prefix)

