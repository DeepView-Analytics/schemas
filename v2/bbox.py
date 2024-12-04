from pydantic import BaseModel

class BBox(BaseModel):
    xmin: float
    xmax: float
    ymin: float
    ymax: float
    conf: float
    

