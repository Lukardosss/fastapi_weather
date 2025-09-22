#models.py
from pydantic import BaseModel
from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Field, create_engine, Session

class Point(SQLModel, table=True):
    name: str = Field(primary_key=True)


class Weather(BaseModel):
    temperature: bool | None = False
    relative_Humidity: bool | None = False
    apparent_Temperature: bool | None = False
    is_Day_or_Night: bool | None = False
    precipitation: bool | None = False
    rain: bool | None = False
    showers: bool | None = False
    snowfall: bool | None = False
    weather_code: bool | None = False
    cloud_cover_Total: bool | None = False
    sealevel_Pressure: bool | None = False
    surface_Pressure: bool | None = False
    wind_Speed: bool | None = False
    wind_Direction: bool | None = False
    wind_Gusts: bool | None = False


sql_url = f"sqlite:///database.db"

connect_args = {"check_same_thread": False}
engine = create_engine(sql_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]