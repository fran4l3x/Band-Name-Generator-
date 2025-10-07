import time
from transformers import pipeline
from pyexpat import model
# AI generator
generator = pipeline("text-generation", model="distilgpt2")  # smaller, faster

print("🎸 Welcome to the Band Name Generator 🎸")

# User inputs
city = input("Which city did you grow up in?\n").strip()
pet = input("What is the name of your pet?\n").strip()
language = input("Which language do you speak?\n").strip()
word = input("Your most valuable word?\n").strip()

# Basic deterministic band name
basic_name = f"{city} {pet} {word}"
print("\nYour basic band name:", basic_name)