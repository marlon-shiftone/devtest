#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 16:06:46 2025

@author: marlon
"""

from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime
from typing import Optional 

def create_event(db: Session, event: schemas.ElevatorEventCreate):
    db_event = models.ElevatorEvent(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ElevatorEvent).offset(skip).limit(limit).all()

def get_events_by_interval(
    db: Session, 
    start_datetime: datetime, 
    end_datetime: datetime, 
    elevator_id: Optional[int] = None
):
    query = db.query(models.ElevatorEvent).filter(
        models.ElevatorEvent.timestamp.between(start_datetime, end_datetime)
    )
    
    if elevator_id:
        query = query.filter(models.ElevatorEvent.elevator_id == elevator_id)

    return query.order_by(models.ElevatorEvent.timestamp).all()

