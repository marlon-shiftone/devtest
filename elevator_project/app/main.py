#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 16:18:02 2025

@author: marlon
"""

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas import ElevatorEventRead, ElevatorEventQuery
from . import models, schemas, crud
from .database import SessionLocal, engine

# Automatically create database tables based on models (only for local/dev)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST endpoint to create elevator events
@app.post("/events/", response_model=schemas.ElevatorEventRead)
def create_event(event: schemas.ElevatorEventCreate, db: Session = Depends(get_db)):
    return crud.create_event(db=db, event=event)

# GET endpoint to read elevator events
@app.get("/events/", response_model=list[schemas.ElevatorEventRead])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_events(db, skip=skip, limit=limit)

@app.post("/events/query/", response_model=List[ElevatorEventRead])
def query_events(event_query: ElevatorEventQuery, db: Session = Depends(get_db)):
    events = crud.get_events_by_interval(
        db, 
        start_datetime=event_query.start_datetime, 
        end_datetime=event_query.end_datetime, 
        elevator_id=event_query.elevator_id
    )
    return events
