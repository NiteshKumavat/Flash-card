from data import all_questions
import html

class Question :
	def __init__(self) :
		self.question = [value['question'] for value in all_questions]
		self.correct_options = [html.unescape(value["correct_answer"]) for value in all_questions]

	def give_all_options(self):
		all_options = []
		for value in all_questions :
			option_list = value["incorrect_answers"]
			option_list.append(value["correct_answer"])
			all_options.append(option_list)
		return all_options