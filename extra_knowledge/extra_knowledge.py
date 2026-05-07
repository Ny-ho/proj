from typing import Any
#type hinting
class city:
    def __init__(self,name,location):
        self.name=name
        self.location=location
nepal=city("nepal",2374)
tuplessss:tuple[city,int]=(nepal,10)
        
name: str="name"
num: float=10.9
value="string"
number:int|float=12#int or float
optiounal:str|None
optiounal="string"
digite:list[int]=[1,2,3,4,5]
tuples:tuple[int, ...]=(1,2,3,4,5)
tuplecity_temp:tuple[str,float]=("city",40.7)
dictionary:dict[str,Any]={
    "name":"wooden box",
    "content":"in transit",
    "id":1,
    "weight":12.3
}


def underoot(num:int|float,exp:float|None=0.5) ->float:#float for the return . number hinting for pow
    #num.
    return pow(num,.5)

underoot_5:float=underoot(25) 
underoot_5
#root=underoot("23")

