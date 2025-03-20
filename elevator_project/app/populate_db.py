#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 16:10:29 2025

@author: marlon
"""

from .database import SessionLocal
from .crud import create_event
from .schemas import ElevatorEventCreate
from .synthetic_data import generate_synthetic_elevator_data  

def populate_db():
    db = SessionLocal()
    df = generate_synthetic_elevator_data(num_steps=100, floors=4, reset_floor=0, seed=42)

    for _, row in df.iterrows():
        event = ElevatorEventCreate(
            timestamp=row['timestamp'],
            elevator_id=row['elevator_id'],
            transition=row['transition'],
            floor=row['floor']
        )
        create_event(db, event)

    db.close()

if __name__ == "__main__":
    populate_db()
