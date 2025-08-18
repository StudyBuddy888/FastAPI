from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# - FastAPI auto-generates docs, but this lets you override metadata like title, version, etc
from fastapi.openapi.utils import get_openapi 
#import router
#create a core config and import
from app.core.config import Settings
app = FastAPI() #enable debug, docs, etc  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #allow_origins=["https://myfrontend.com"]
 # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
    )

app.include_router( )

#custom schema
app.openapi_schema  = get_openapi(
    title="Practice API",
    version="1.0.0",
    description="This is a practice API for learning purposes.",
    contact={
        "name": "PADMACHARAN M", "email": "charangowda.m9141@gmail.com"},
    routes=app.routes,
    servers=[
        {"url": "/api"}] # Add server URL if needed
)

