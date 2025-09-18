import streamlit as st

st.title("BMI Calculator")

height = st.slider("Enter Your Height (in cm): ", 100, 250, 175)
weight = st.slider("Enter Your Weight (in kg): ", 40, 200, 70)

bmi = weight / ((height/100) ** 2) # convert height to meters

st.html("<br>")

# st.write(f"Your BMI is {bmi:.2f}")
st.html(f"<span style='background-color: yellow; font-size: 30px; '>Your BMI is {bmi:.2f}</span>")


st.html("<br>")

st.write("### BMI Categories ###")
st.write("- Under Weight: BMI less than 18.5")
st.write("- Normal Weight : BMI between 18.5 and 24.9")
st.write("- Over Weight : BMI between 25 and 29.9")
st.write("- Obesity : BMI 30 or greater")