import os
import uvicorn
from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select
from dotenv import load_dotenv

# run backend with this code in terminal
# python.exe -m uvicorn app.main:app --reload --app-dir Backend

##### SETUP #####
app = FastAPI()

# import and our env variables here
load_dotenv("Backend/.env")
database_url = os.getenv("DATABASE_URL")

# tables to make on launch
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password_hash: str

# opens our apps connection handle to Postgres
# echo=true logs sql to terminal, can set to false later
engine = create_engine(database_url, echo=True)

#on running the app if tables dont exist, then make them
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

##### API ROUTES #####
@app.get("/")
def home():
    return {"Hello": "World"}

##### ON RUN #####
if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)