import random
game_list = ["rock","paper","scissor"]
computer = random.choice(game_list)
i = 0
while True:
	user_input =raw_input("enter your choice rock paper scissor ")
	if user_input not in game_list:
		print "invalid input"
	elif user_input == coputer:
		print "game draw"
	elif user_input == "paper" and computer == "rock":
		print "you win"
	elif user_input == "scissor" and computer == "paper":
		print "you win"
	elif user_input == "rock" and computer == "scissor":
		print "you win"
	else:
		print "you los"
