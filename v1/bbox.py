from typing import ClassVar

from pydantic import Field , BaseModel


class Bbox(BaseModel):
    person_id: int = Field(default_factory=lambda: Bbox.generate_id())
    xmin: float
    ymin: float
    xmax: float
    ymax: float
    conf: float

    _id_counter: ClassVar[int] = 0


    @classmethod
    def generate_id(cls):
        result = cls._id_counter
        cls._id_counter += 1
        return result