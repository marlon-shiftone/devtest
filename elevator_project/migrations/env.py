#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 17:19:58 2025

@author: marlon
"""

import sys, os
sys.path.append(os.getcwd())

from app.models import Base
target_metadata = Base.metadata
