import random
import tkinter as tk

def get_reason(choice):
    choice = choice.lower()

    if "study" in choice:
        return "Studying now will reduce your stress later."
    
    elif "sleep" in choice:
        return "Your body needs rest to perform better."
    elif "gym" in choice:
        return "Consistency builds strength and discipline."
    elif "eat" in choice or "food" in choice:
        return "Good food fuels your energy."
    elif "game" in choice:
        return "Relaxation is also important sometimes."
    
    else:
        return "This seems like a good choice for now."
    

def make_decision():

    user_input = entry.get()
    if user_input=="":
        result_label.config(text="enter the right choice ")
        return




    choices = user_input.split(",")

    cleaned_choices = []
    for c in choices:
        cleaned_choices.append(c.strip())

    selected = random.choice(cleaned_choices)

    result_label.config(text="Decision: " + selected)
    reason_label.config(text="Reason: " + get_reason(selected))

root = tk.Tk()
root.title("Decision Justifier")
root.geometry("400x300")

title = tk.Label(root, text="Decision Justifier", font=("Arial", 16))
title.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

button = tk.Button(root, text="Decide", command=make_decision)
button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

reason_label = tk.Label(root, text="")
reason_label.pack(pady=10)

root.mainloop()