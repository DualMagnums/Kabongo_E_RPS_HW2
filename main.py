from random import randint

# an array is a container. It holds multiple values in a 0-based index
# you can store anything in an array 
# and retrieve it later. Arrays have square bracket notation

choices = ["rock", "paper", "scissors"]

# save the player as a variable called player
# the value of player will be one of three choices to type (input)


# boolean valuesare true or False
player = False

print()
print("(o_o) Let's play Roshambo (o_o)")

# player will be the weapon the player chooses via input

# these lives are deducted when a player loses the round

playerLives = 5
computerLives = 5

# create an infinite loop so we can keep playing
while player is False:
	print()
	print("==============================")
	print()
	player = input("Choose your weapon! rock, paper or scissors: ")
	computer = choices[randint(0,2)]

	print()
	print("==============================")
	print()
	print("Player chose: " + player)
	print()
	print("Computer chose: " + computer)
	print()
	print("==============================")
	print()
	if (computer == player):
		print("Tie! Try Again")

	elif (player == "rock"):
		if (computer == "paper"):
			print("Paper covers rock! YOU LOSE!")
			playerLives = playerLives - 1
		else:
			print("Rock smashes scissors! YOU WIN!")
			computerLives = computerLives - 1

	elif (player == "paper"):
		if (computer == "scissors"):
			print("Scissors cut paper! YOU LOSE!")
			playerLives = playerLives - 1
		else:
			print("Paper covers rock! YOU WIN!")
			computerLives = computerLives - 1

	elif (player == "scissors"):
		if (computer == "rock"):
			print("Rock smashes scissors! YOU LOSE!")
			playerLives = playerLives - 1
		else:
			print("Scissors cut paper! YOU WIN!")
			computerLives = computerLives - 1
	print()
	print("==============================")
	print()
	print("Player lives: " + str(playerLives))
	print("Computer lives: " + str(computerLives))

	if playerLives == 0:
		print()
		print("==============================")
		print()
		print("ROSHAMBO! YOU LOST! Would you like to play again?")
		choice = input("y / n: ")

		if choice == "n":
			print()
			print("You got Roshambo'd! Better luck next time!")
			exit()

		else:
			# this resets the game and gives everyone 5 lives again
			playerLives = 5
			computerLives = 5
			player = False

	elif computerLives == 0:
		print()
		print("==============================")
		print()
		print("ROSHAMBO! YOU WIN! Would you like to play again?")
		choice = input("y / n: ")

		if choice == "n":
			print()
			print("Roshambo! See you next time!")
			exit()

		else:
			# this also resets the game and gives everyone 5 lives again
			playerLives = 5
			computerLives = 5
			player = False
		


	player = False