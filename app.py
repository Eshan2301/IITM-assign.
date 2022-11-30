import numpy as np
import pandas as pd
import streamlit as st


def main():
  


  st.title("Greater Of Three Numbers")
  a=st.number_input("Enter First Number a")
  b=st.number_input("Enter Second Number b")
  c=st.number_input("Enter Third Number c")

  if(a>b) and (a>c):
    st.write("a is greater")
  elif(b>a) and (b>c):
    st.write("b is greater")
  else:
    st.write("c is greater")
  

  
if __name__=='__main__':
  main()
