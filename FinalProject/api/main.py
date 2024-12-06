import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import index as index_route
from .routers import ratings_and_reviews as reviews_router  # Added import for the reviews router
from .models import model_loader
from .dependencies.config import conf


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader.index()
index_route.load_routes(app)

# Include the ratings and reviews router
app.include_router(reviews_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)
