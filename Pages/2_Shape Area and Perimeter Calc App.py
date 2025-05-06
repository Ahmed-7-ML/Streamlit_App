import streamlit as st
import math
import time

st.header("Hello Ahmed Akram & Ibrahim Hashish !") 
 # Display text in header formatting.
st.header("Shape Area Calculation")
st.sidebar.title("Configuration")

with st.sidebar:
    shape = st.selectbox("Select Shape ", ["Circle", "Rectangle", "Square"])

# print(shape)

# area = None
# perimeter = None 

if shape == "Circle":
    # StreamlitMixedNumericTypesError: All numerical arguments must be of the same type.
    radius = st.number_input("Radius", min_value=0.0, max_value=100.0, step=0.01)
    area = math.pi * radius**2
    perimeter = 2 * math.pi * radius
elif shape == "Rectangle":
    width = st.number_input("Width", min_value=0.0, max_value=200.0, step=0.1)
    length = st.number_input("Length", min_value=0.0, max_value=200.0, step=0.1)
    area = width * length
    perimeter = 2 * (length + width)
else:
     side_length = st.number_input("The Side Length", min_value=0.0, max_value=100.0, step=0.1)
     area = side_length** 2
     perimeter = 4 * side_length

compute_pattern = st.button("Compute Area and Perimeter")
if compute_pattern:
    # Display a loading spinner while executing a block of code.
    with st.spinner("Computing...."):
        time.sleep(1)
        st.write("Area = ", area)
        st.write("Perimeter = ", perimeter)
