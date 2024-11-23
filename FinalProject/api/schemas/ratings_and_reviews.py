from pydantic import BaseModel
from typing import Optional

class RatingAndReviewBase(BaseModel):
    review_text: Optional[str]
    score: int
    customer_id: int
    order_id: int

class RatingAndReviewCreate(RatingAndReviewBase):
    pass

class RatingAndReview(RatingAndReviewBase):
    id: int

    class Config:
        orm_mode = True