import random
game_list = ["rock","paper","scissor"]
computer = random.choice(game_list)
i = 0
while True:
	user_input =raw_input("enter your choice rock paper scissor ")
	if user_input not in game_list:
		print "invalid input"
	
