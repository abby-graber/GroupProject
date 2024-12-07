from pydantic import BaseModel
from typing import Optional

class RatingAndReviewBase(BaseModel):
    review_text: Optional[str] = None
    score: int
    customer_id: int
    order_id: int
    menu_item_id: int  # Linking reviews to menu items

class RatingAndReviewCreate(RatingAndReviewBase):
    pass

class RatingAndReviewUpdate(RatingAndReviewBase):
    review_text: Optional[str] = None

class RatingAndReview(RatingAndReviewBase):
    id: int

    class Config:
        orm_mode = True
