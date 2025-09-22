#main.py

from fastapi import FastAPI
from models import Point, Weather, create_db_and_tables, SessionDep
from config import geo

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/geo")
async def get_geo(point: Point, weather: Weather, session: SessionDep):
    s = geo(point, weather)
    session.add(point)
    session.commit()
    session.refresh(point)

    return {
        "point": point,
        "geo": {"lat": s["lat"], "lon": s["lon"]},
        "weather": s["weather"]
    }