"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	Function: The program can do coin flipping game. First ask the user to insert a number, which represent the the
	number of time the result of flipping appearing same side in a row.
	Principle: "random" need to be imported to create two sides of coin result while flipping. After the user inserted
	certain round number, for looped is used to create continuous same side result of flipping coin.
	"""
	print("Let's flips a coin!")
	run = int(input("Number of runs:"))
	ans = ''
	for i in range(2):  # first round
		ans += str(random_coin())

	ch_1 = ans[int(len(ans)) - 1]
	ch_2 = ans[int(len(ans)) - 2]
	while ch_1 != ch_2:
		ans += str(random_coin())
		ch_1 = ans[int(len(ans)) - 1]
		ch_2 = ans[int(len(ans)) - 2]

	for i in range(run-1):  # The round number is fixed, so for loop is used
		ans += str(random_coin())
		ch_1 = ans[int(len(ans)) - 1]  # The flipping result needs to be again and again updated every time flipping
		ch_2 = ans[int(len(ans)) - 2]
		ch_3 = ans[int(len(ans)) - 3]
		while ch_1 != ch_2:  # in the case that next round start to develop
			ans += str(random_coin())
			ch_1 = ans[int(len(ans)) - 1]
			ch_2 = ans[int(len(ans)) - 2]
			ch_3 = ans[int(len(ans)) - 3]
		else:
			if ch_1 == ch_3:  # in the case that second round start to develop
				ans += str(random_coin())
				ch_1 = ans[int(len(ans)) - 1]
				ch_2 = ans[int(len(ans)) - 2]
				while ch_1 == ch_2:
					ans += str(random_coin())
					ch_1 = ans[int(len(ans)) - 1]
					ch_2 = ans[int(len(ans)) - 2]
				else:
					ans += str(random_coin())
					ch_1 = ans[int(len(ans)) - 1]
					ch_2 = ans[int(len(ans)) - 2]
					while ch_1 != ch_2:
						ans += str(random_coin())
						ch_1 = ans[int(len(ans)) - 1]
						ch_2 = ans[int(len(ans)) - 2]

	print(str(ans))


def random_coin():
	"""
	:return "T" or "H": "T" or "H" which represent two sides of a coin
	Function: Can randomly produced "T" or "H"
	"""
	two = r.choice(range(2))
	if two == 0:
		return "T"
	if two == 1:
		return "H"

# Time spent: 3 hours





# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
