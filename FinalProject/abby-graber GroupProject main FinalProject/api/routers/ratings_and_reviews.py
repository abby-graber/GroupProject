# In routers/ratings_and_reviews.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..controllers import ratings_and_reviews as controller
from ..schemas import ratings_and_reviews as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Ratings and Reviews"],
    prefix="/reviews"
)

# Add Review
@router.post("/", response_model=schema.RatingAndReview, tags=["Ratings and Reviews"])
def add_review(review: schema.RatingAndReviewCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, review=review)

# Get All Reviews
@router.get("/", response_model=List[schema.RatingAndReview], tags=["Ratings and Reviews"])
def get_reviews(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Get Review by ID
@router.get("/{review_id}", response_model=schema.RatingAndReview, tags=["Ratings and Reviews"])
def get_review(review_id: int, db: Session = Depends(get_db)):
    review = controller.read_one(db=db, review_id=review_id)
    if review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

# Update Review
@router.put("/{review_id}", response_model=schema.RatingAndReview, tags=["Ratings and Reviews"])
def update_review(review_id: int, review: schema.RatingAndReviewUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, review_id=review_id, review=review)

# Delete Review
@router.delete("/{review_id}", tags=["Ratings and Reviews"])
def delete_review(review_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, review_id=review_id)

