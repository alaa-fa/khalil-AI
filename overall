import streamlit as st

# Import the individual pages
import khalil_chatbot
import mood_tracker
import house_price_prediction

# Create a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["GPA Prediction", "Bullying Prediction", "House Price Prediction"])

# Show the selected page
if page == "تحدث مع خليل":
    khalil_chatbot.show()
elif page == "متابعة المشاعر":
    mood_tracker.show()
else:
    house_price_prediction.show()
