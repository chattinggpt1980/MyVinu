
import streamlit as st

# Set page title and icon
st.set_page_config(page_title=" ", page_icon="🎨")

# Set background color and text color using CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f4;
        color: #333;
        font-family: 'Helvetica Neue', 'Arial', sans-serif;
    }
    .stButton {
        background-color: #d8bfd8;  /* Lavender color */
        color: white;
        border: none;
        border-radius: 5px;
        padding: 12px 24px;
        margin: 10px 10px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s ease;
    }
    .stButton:hover {
        background-color: #b090b0;  /* Darker lavender on hover */
    }
    .message {
        padding: 15px;
        background-color: #ffffff;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add a title with improved styling
st.title("I love you Vinu!")

# Add buttons for message redirection
col1, col2 = st.columns(2)
with col1:
    if st.button("Still angry baby..?", key="button1"):
        st.info("I am so so so sorry Vinu. I know you are tired of hearing sorry. I hurt you a lot. I cannot bring yesterday's day back but I can assure you that you will never see yesterday's day in the future again. You did point out once that I let my anger take over everything and you are right. Whatever feeling it was this time, I did let it over power me. But abse pakka kabhi bhi nahi hone dungi aisa mai Vinu. I am also sorry for not being understanding enough. I know that you are going through a lot right now (healthwise) and even then I was fighting with you. I love you a lot Vinu and I know I have not been showing much from my actions. But I will try everyday till we get old, to improve myself and show or express as much love as possible through my actions. Please Please Please forgive me baby....")
with col2:
    if st.button("You forgave me?? Yayyyy!!!", key="button2"):
        st.info("Thank you, Thank you, Thank youuuuuu so much Vinu. My little baby, I will pakka not make you regret forgiving me for this. I LOVE YOUUUUUU. <3<3<3 XOXOXOXOXO Your Dikshuu. (I don't know how to add emojis in this isliye i had to type XO for hugs and kisses)")

# Run the app
if __name__ == "__main__":
    st.write("My Vinu is the best. And Dikshu loves you a lot.")

