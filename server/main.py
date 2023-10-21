from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

import create_examples
from routers import recipes_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recipes_router.router)

@app.get("/")
async def health_check():
    return "it's ok!"

if __name__=="__main__":
    uvicorn.run("main:app",host="0.0.0.0", port=8000, reload=True)