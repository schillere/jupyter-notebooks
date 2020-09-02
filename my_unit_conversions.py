# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:36:30 2020

@author: ean.schiller


Unit Conversion Convenience Functions
"""


def funFtoK(fTempF):
    """converts F to K"""
    fTempK = (fTempF + 459.67)*5/9
    return fTempK


def funKtoF(fTempK):
    """converts K to F"""
    fTempF = fTempK*9/5 - 459.67
    return fTempF


def funCtoK(fTempC):
    """converts C to K"""
    fTempK = fTempC + 273.15
    return fTempK


def funMtoIN(fLengthM):
    """converts M to in"""
    fLengthIN = fLengthM / 0.0254
    return fLengthIN


def funINtoM(fLengthIN):
    """converts in to M"""
    fLengthM = fLengthIN * 0.0254
    return fLengthM
