#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:16:50 2023

@author: markwin
"""

class BMI:
    def __init__(self, height_value, weight_value):

      self.height_value = height_value
      self.weight_value = weight_value

    def calculate_BMI(self):

      BMI_value = self.weight_value / self.height_value ** 2
      return BMI_value

    def displayweightstatus(self):

      BMI_value = self.weight_value / self.height_value ** 2

      if BMI_value < 18.5:
        print('You are underweight, skinny.')
      elif BMI_value >= 18.5 and BMI_value <= 22.9:
        print('You have normal weight.')
      elif BMI_value > 22.9 and BMI_value <= 29.9:
        print('You are overweight, fatso.')
      else:
        print('You are obese, fatty bom bom.')
