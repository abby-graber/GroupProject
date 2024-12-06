from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import ratings_and_reviews as model
from ..schemas import ratings_and_reviews as schema


def create(db: Session, review: schema.RatingAndReviewCreate):
    db_review = model.RatingAndReview(
        review_text=review.review_text,
        score=review.score,
        customer_id=review.customer_id,
        order_id=review.order_id,
        menu_item_id=review.menu_item_id
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def read_all(db: Session):
    return db.query(model.RatingAndReview).all()


def read_one(db: Session, review_id: int):
    return db.query(model.RatingAndReview).filter(model.RatingAndReview.id == review_id).first()


def update(db: Session, review_id: int, review: schema.RatingAndReviewUpdate):
    db_review = db.query(model.RatingAndReview).filter(model.RatingAndReview.id == review_id)
    if db_review.first() is None:
        raise HTTPException(status_code=404, detail="Review not found")

    update_data = review.dict(exclude_unset=True)
    db_review.update(update_data, synchronize_session=False)
    db.commit()
    return db_review.first()


def delete(db: Session, review_id: int):
    db_review = db.query(model.RatingAndReview).filter(model.RatingAndReview.id == review_id)
    if db_review.first() is None:
        raise HTTPException(status_code=404, detail="Review not found")

    db_review.delete(synchronize_session=False)
    db.commit()
    return {"message": "Review deleted successfully"}
