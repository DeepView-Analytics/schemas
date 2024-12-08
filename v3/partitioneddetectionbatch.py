from typing import List
from v3.bbox import BBox
from pydantic import BaseModel

class PartitionedDetectionBatch(BaseModel):
    frame_key: str 
    person_keys: List[str] 
    person_bbox: List[BBox] 
    partition_number: int  
    total_partitions: int 
