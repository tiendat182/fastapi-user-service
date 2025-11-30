from pydantic import BaseModel
from math import ceil
from typing import List, Generic, TypeVar

T = TypeVar("T")

class Page(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int
    total_pages: int

    @staticmethod
    def build(items, total, page, size):
        total_pages = ceil(total / size) if size > 0 else 1
        return Page(items=items, total=total, page=page, size=size, total_pages=total_pages)
