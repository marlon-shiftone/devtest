#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 16:13:25 2025

@author: marlon
"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ElevatorEventBase(BaseModel):
    timestamp: datetime
    elevator_id: int
    transition: str
    floor: int

class ElevatorEventCreate(ElevatorEventBase):
    pass

class ElevatorEventRead(ElevatorEventBase):
    id: int

    class Config:
        from_attributes = True

class ElevatorEventQuery(BaseModel):
    start_datetime: datetime
    end_datetime: datetime
    elevator_id: Optional[int] = None

