#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK11 warmup task 01 - instantiate classes."""


import produce

TOMATO = produce.Produce()

EGGPLANT = produce.Produce(1311210802)

TOMATO_ARRIVAL = TOMATO.arrival

EGGPLANT_EXPIRES = EGGPLANT.get_expiration()