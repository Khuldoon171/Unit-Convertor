import streamlit as st

# Custom CSS
st.markdown(
    """
    <style>
        .stApp {
            background-color: #e8daef;
        }

        /* Title Styling */
        .title {
            color: #1E40AF;
            font-size: 2.5rem;
            font-weight: bold;
            text-align: center;
            padding: 10px;
        }

        /* Styled Box */
        .custom-box {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        /* Convert Button */
        .stButton>button {
            background-color: #1E40AF !important;
            color: white !important;
            font-size: 18px !important;
            border-radius: 8px !important;
            padding: 10px 20px !important;
            border: none !important;
        }

        /* Convert Button Hover */
        .stButton>button:hover {
            background-color: #1B2A4E;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.balloons()
st.info("App made by: [Khuldoon Ahmed]")
st.markdown('<h1 class="title">🌍 Unit Converter App</h1>', unsafe_allow_html=True)
st.markdown("### Converts Length, Weight, Time, Temperature, and Currency Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

# Category Selection
category = st.selectbox("Choose a category", ["Length", "Weight", "Time", "Temperature", "Currency"])

# Conversion Logic
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371
    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24
    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
    elif category == "Currency":
        if unit == "USD to PKR":
            return value * 275.5
        elif unit == "PKR to USD":
            return value / 275.5

# Unit Selection
if category == "Length":
    unit = st.selectbox("🚐 Select Conversion", ["Kilometers to miles", "Miles to kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("⏰ Select Conversion", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])
elif category == "Temperature":
    unit = st.selectbox("🌡️ Select Conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
elif category == "Currency":
    unit = st.selectbox("💵 Select Conversion", ["USD to PKR", "PKR to USD"])

# Input Field
value = st.number_input("Enter Value to Convert")

# Convert Button
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result:
        st.success(f"This result is: {result:.2f}")
    else:
        st.error("Invalid conversion. Please check the inputs.")
