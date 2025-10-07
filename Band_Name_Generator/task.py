import streamlit as st
from transformers import pipeline
import time

generator = pipeline("text-generation", model="gpt2")

st.title("🥁 Band Name Generator AI")

language = st.text_input("Which language do you speak?")
city = st.text_input("Which city did you grow up in?")
pet = st.text_input("What is your pet’s name?")
word = st.text_input("Your most valuable word?")

if st.button("Generate Band Name"):
    prompt = (
        f"Generate one short creative phrase using language={language}, city={city}, "
        f"pet={pet}, and word={word}. Only the phrase."
    )
    result = generator(prompt, max_length=20, num_return_sequences=1)[0]['generated_text']

    st.write("Your band name is...")
    time.sleep(2)
    st.success(f"🥁 {result.strip()} 🥁")




