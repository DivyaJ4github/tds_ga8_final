import streamlit as st
st.title("22f1001356's app 1")
st.header("Finding Largest of Three Given Numbers")
def largestnum(a,b,c):
  if a>b:
    if a>c:
      return a
  elif b>c:
      return b
  else:
    return c
a=st.number_input("Enter first number")
b = st.number_input("Enter second number")
c=st.number_input("Enter third number")
st.write("The First Number is:",a)
st.write("The Second Number is:",b)
st.write("The Third Number is:",c)
st.write("The Largest number is :", largestnum(a,b,c))
