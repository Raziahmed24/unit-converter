import streamlit as st 

st.set_page_config(page_title="📁 File Converter & Cleaner", page_icon="🌎")
st.title("🌎 Unit Converter App")
st.markdown("### Converts Length, Weight, and Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

# Category selection
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462       

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

    return 0
        
# Unit selection based on category
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Miles to Kilometers", "Kilometers to Miles"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏱ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

# User input for value
value = st.number_input("Enter a value to convert", min_value=0.0, format="%.2f")

# Convert button
if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
