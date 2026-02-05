import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from auth import router as auth_router
from tasks import router as tasks_router

app = FastAPI(title="Scalable REST API", version="v1")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

# ...routes for auth, tasks, etc. will be added here

# API versioning
app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(tasks_router, prefix="/api/v1/tasks", tags=["tasks"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
