#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 17:34:17 2021

@author: administrator
"""

from pydantic import BaseModel


class BankNotes(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float
