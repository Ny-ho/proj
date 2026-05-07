from typing import Any,Callable

routes:dict[str,Callable[[Any],Any]]={}

def route(path:str):
    def resisteer_func(funct):
        routes[path]=funct
        return funct
    return resisteer_func

@route("/shipment")
def shipment():
    print("coming alinf")

request:str=""
while request != "null":
    request=input("> ")
    if request in routes:
        response=routes[request]()
        print(response,end="\n\n")
