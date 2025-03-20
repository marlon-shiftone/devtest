#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 16:16:35 2025

@author: marlon
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.crud import create_event, get_events
from app.schemas import ElevatorEventCreate
import datetime

def test_create_read_event():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()

    event = ElevatorEventCreate(
        timestamp=datetime.datetime.now(),
        elevator_id=1,
        transition="resting",
        floor=0
    )

    create_event(db, event)
    events = get_events(db)
    assert len(events) == 1
    assert events[0].transition == "resting"
