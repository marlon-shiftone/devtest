#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 16:06:21 2025

@author: marlon
"""

from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class ElevatorEvent(Base):
    __tablename__ = "elevator_events"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, index=True, nullable=False)
    elevator_id = Column(Integer, nullable=False)
    transition = Column(String(20), nullable=False)
    floor = Column(Integer, nullable=False)
