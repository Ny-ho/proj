from pydantic import BaseModel,Field

class shipment(BaseModel):
        content:str
        weight:float=Field(le=25)
        destination:int