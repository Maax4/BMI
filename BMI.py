#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:16:50 2023

@author: markwin
"""

import streamlit as st

st.title("Welocme to BMI calculator")

#Input

weight = st.number_input("Enter your weight in KG", step = 0.1)

height = st.number_input("Enter your height in Meters", step = 0.01)

def calculate_BMI_and_display_weight_status():

  BMI_value = weight / height ** 2

  if BMI_value < 18.5:
    print('You are underweight, skinny.')
  elif BMI_value >= 18.5 and BMI_value <= 22.9:
    print('You have normal weight.')
  elif BMI_value > 22.9 and BMI_value <= 29.9:
    print('You are overweight, fatso.')
  else:
    print('You are obese, fatty bom bom.')

button = st.button("Calculate BMI")
if button:
    calculate_BMI_and_display_weight_status()
