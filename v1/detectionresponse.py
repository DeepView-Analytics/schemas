from typing import List
from v1.partitioneddetectionbatch import PartitionedDetectionBatch
from pydantic import BaseModel

class DetectionResponse(BaseModel):
    request_id: int
    detection: List[PartitionedDetectionBatch]

