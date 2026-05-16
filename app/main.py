from fastapi import FastAPI,HTTPException,status
from scalar_fastapi import get_scalar_api_reference
from typing import Any

from .schemas import shipment

app=FastAPI()
    
shipments={
    12011:{
        "weight":.4,
        "content":"shard",
        "status":"delivered"
    },
    12012:{
        "weight":1.5,
        "content":"glass",
        "status":"in transit"
    },
    12013:{
        "weight":2.1,
        "content":"ceramic vase",
        "status":"pending"
    },
    12014:{
        "weight":0.8,
        "content":"book",
        "status":"delivered"
    },
    12015:{
        "weight":3.2,
        "content":"wooden box",
        "status":"in transit"
    },
    12016:{
        "weight":0.6,
        "content":"phone case",
        "status":"processing"
    },
    12017:{
        "weight":1.9,
        "content":"laptop bag",
        "status":"pending"
    }

}
@app.get("/shipment/latest")
def shipment_latest():
    id=max(shipments.keys())
    return (shipments[id],id)
    
    
@app.get("/shipment")
def get_shipment(id: int|None=None) -> dict[str,Any]:
    #if not id:
        #id=max(shipments.keys())
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="values or id not found"
        )
    
    return shipments[id] 

@app.post("/shipment")
def submit_shipment(body:shipment)->dict[str,Any]:
   
    new_id=max(shipments.keys())+1

    # if body.weight>25:
    #     raise HTTPException(
    #         status_code=status.HTTP_406_NOT_ACCEPTABLE,
    #         detail="weight cant be more than 25 kgs"
    #     )
    
    shipments[new_id]={
        "content":body.content,
        "weight":body.weight,
        "destination":body.destination,
        "status":"passed"
    }
    return{"id":new_id}

@app.get("/shipment/{field}")
def get_shipments_field(field:str,id:int)-> dict[str,Any]:
    return{
        field: shipments[id][field]
    }

@app.put("/shipment")
def shipment_update(id:int,content:str,weight:int,status:str)->dict[Any,Any]:
    shipments[id]={
        "content":content,
        "weight":weight,
        "status":status,
    }
    return shipments[id]

@app.patch("/shipment")
def patch_update(id:int,
                 content:str|None=None,
                 weight:int|None=None,
                 status:str|None=None):
    shipment=shipments[id]
    if content:
        shipment["content"]=content
    if weight:
        shipment['weight']=weight
    if status:
        shipment["status"]=status
 
    shipments[id]=shipment
    return shipment


@app.delete("/shipment")
def delete_shipment(id:int)-> dict[str,str]:
    shipments.pop(id)
    return{"details":f"the details off the id {id} is deleted"}
    



    
#custom documentation
@app.get("/scalar",include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",

    )