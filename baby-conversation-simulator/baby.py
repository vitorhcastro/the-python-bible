from random import choice

questions = [
    "Why is the sky blue?",
    "Why is there a face on the moon?",
    "Where are all the dinosaurs?"
]

question = choice(questions)
answer = input("{}\n".format(question)).strip().lower()

while not answer == "just because":
    answer = input("\nWhy?\n").strip().lower()

print("\nOhh... Okay.")
