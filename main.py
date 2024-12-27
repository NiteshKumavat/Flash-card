from tkinter import *
from question import Question
import random
import time
import html

count = 0
score = 0
q = Question()

def next_question() :
	global count
	canvas.itemconfig(title, text=f"Question {count+1}")
	canvas.itemconfig(word, text=html.unescape(q.question[count]))
	all_options = q.give_all_options()
	current_options = all_options[count]
	random.shuffle(current_options)
	answer1.set(f"1. {html.unescape(current_options[0])}")
	answer2.set(f"2. {html.unescape(current_options[1])}")
	answer3.set(f"3. {html.unescape(current_options[2])}")
	answer4.set(f"4. {html.unescape(current_options[3])}")


def check_answer(event) :
	global score
	global count
	text = event.widget.cget("text")
	actual_answers = q.correct_options
	new_text = "You got it right"
	if text[3:] in actual_answers :
		score += 1
	else :
		new_text = f"The correct answer is '{actual_answers[count]}'"

	canvas.itemconfig(canvas_img, image=back_photo)
	canvas.itemconfig(title, text=f"Score : {score}/10")
	canvas.itemconfig(word, text=new_text)
	count += 1
	window.update()
	time.sleep(6)
	canvas.itemconfig(canvas_img, image=front_photo)
	next_question()




window = Tk()
window.title("Flash Card App")

canvas = Canvas(width=800, height=526)
front_photo = PhotoImage(file="card_front.png")
back_photo = PhotoImage(file="card_back.png")
canvas_img = canvas.create_image(400,263, image=front_photo)
title = canvas.create_text(400, 63, text="", font=("Arial", 15, "bold"), width=300)
word = canvas.create_text(400, 263, text="", font=("Arial", 25, "bold"), width=600)
canvas.config(highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


answer1 = StringVar()
answer2 = StringVar()
answer3 = StringVar()
answer4 = StringVar()


option1 = Button(window, text="", width=30, height=2, bg="lightblue", textvariable=answer1, wraplength=100)
option2 = Button(window, text="", width=30, height=2, bg="lightblue", textvariable=answer2, wraplength=100)
option3 = Button(window, text="", width=30, height=2, bg="lightblue", textvariable=answer3, wraplength=100)
option4 = Button(window, text="", width=30, height=2, bg="lightblue", textvariable=answer4, wraplength=100)

option1.grid(row=1, column=0, padx=20, pady=10)
option2.grid(row=1, column=1, padx=20, pady=10)
option3.grid(row=2, column=0, padx=20, pady=10)
option4.grid(row=2, column=1, padx=20, pady=10)

option1.bind("<Button-1>", check_answer)
option2.bind("<Button-1>", check_answer)
option3.bind("<Button-1>", check_answer)
option4.bind("<Button-1>", check_answer)

next_question()

window.mainloop()
