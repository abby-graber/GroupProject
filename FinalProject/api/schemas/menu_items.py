from pydantic import BaseModel
from typing import Optional

class MenuItemBase(BaseModel):
    dish: str
    ingredients: str
    price: float
    calories: int
    food_category: str
    food_type: Optional[str] = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    dish: Optional[str] = None
    ingredients: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    food_category: Optional[str] = None
    food_type: Optional[str] = None

class MenuItem(MenuItemBase):
    id: int

    class ConfigDict:
        from_attributes = True
