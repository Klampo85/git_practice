def lucas_quiz():
	score = 0
	q1 = input("What is the color of the sun?: ")
	print("Welcome to Lucas' quiz. Please get ready to answer some really tricky questions!!")
	print(q1)
	if q1 == "yellow":
		print("That is correct!")
		score += 1
	else:
		print("Sorry, that is incorrect!")
	print("How did you find the first question? Time to get a little bit harder!")
	print("Next question: ")
	q2 = input("Where is Lucas from? : ")
	print(q2)
	if q2 == "New Zealand":
		print("That is correct!")
		score += 1
	else:
		print("Sorry, that is incorrect")
	print("Feeling good after two questions? Lets keep going!")
	print("Next question: ")
	q3 = input("Where does Lucas study Computer Science?: ")
	if q3 == "PJATK":
		print("That is correct!")
		score += 1
	else:
		print("Sorry, that is incorrect!")
	print("I hope your not getting bored! Now for the final question...")
	q4 = input("What is the answer to this mathmatical equasion? 2+2=...")
	if q4 == str(4):
		print("That is correct! You are a genius!")
		score += 1
	else:
		print("Sorry, you are incorrect... and stupid!")
	print("Now that you have finished my quiz, how do you feel?")
	print("Please see your total score printed below!")
	print("Totalscore : " + str(score))
	print("Max possible score : 4")
	return


lucas_quiz()



