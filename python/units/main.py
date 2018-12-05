#!/usr/bin/env python2
# coding=utf-8
"""
Toy example for 
"""

import numericalunits as nu
d1 = 2500 * nu.m
d2 = 2 * nu.mile
total_distance = (d1+d2) / nu.foot  # Result will be in foot

import pint
# units = pint.UnitRegistry(auto_reduce_dimensions=True)
units = pint.UnitRegistry()
3 * units.meter + 4 * units.cm

import numpy as np
[3, 4] * units.meter + [4, 3] * units.cm

units.meter
type(units.meter)
units.cm
type(units.cm)
units.meter/units.cm
type(units.meter/units.cm)
d = units.meter
d = units.m

from math import pi
ang_rad = pi * units.rad
print(ang_rad)
ang_deg = 180 * units.deg
rel = ang_rad / ang_deg
rel.magnitude
rel.units
rel.dimensionality
rel.to_base_units()
rel.to(units.dimensionless)
# rel.ito(units.dimensionless)  # Makes this dimensionless as it should
# rel.to_reduced_units()  # Fails!?
# TODO: How to reduce/simplify product of units

units.m + units.rad

d = 1.0 * units.meter
d.magnitude
d.units
d.dimensionality
d.to(units.cm)
d.to('cm')
try:
    d.to('Hz')
except pint.DimensionalityError:
    print("Catched error: Cannot convert distance to Hz")

# Serialize quantity via json
import json
with open('test.json', 'w') as f:
    json.dump(d.to_tuple(), f, indent=4, sort_keys=True)
with open('test.json') as f:
    d_tuple = json.load(f)
    d_loaded = units.Quantity.from_tuple(d_tuple)
