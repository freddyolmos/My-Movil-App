from pydantic import BaseModel, Field
from typing import Optional


class Movie(BaseModel):
    id : Optional[int] = None
    title : str = Field(min_length= 5, max_length= 30)
    overview: str = Field(min_length=5, max_length= 100)
    year: int = Field(le=2023)
    rating: float = Field(le= 9.9)
    category: str = Field(min_length= 5, max_length= 15)

    class Config:
        json_schema_extra = {
            "example" : {
                "id" : 1,
                "title" : 'TituloPeli',
                "overview" : 'Descripción',
                "year" : 2022,
                "rating" : 7.0,
                "category" : "accion"
            }
        }
