#coding:utf-8

import sys

def part_1_of_challenge():
	'''
		Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.
		Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
		Here's an easy puzzle to warm you up.
		Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.
		An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.
		The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.
	'''
	with open(sys.argv[1], 'r') as f:
		i = 0
		for j_file in f.readlines():
			for p_parathensis in j_file:
				if(p_parathensis == '('):
					i += 1
				elif(p_parathensis == ')'):
					i -= 1
			print(i)

def part_2_of_challenge():
	'''
		Now, given the same instructions, find the position of the first character that causes him 
		to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.
	'''
	with open(sys.argv[1], 'r') as f:
		i = 0
		j = 0
		for j_file in f.readlines():
			for p_parathensis in j_file:
				if(p_parathensis == '('):
					i += 1
				elif(p_parathensis == ')'):
					i -= 1
				j += 1
				if(i == -1):
					print(j)
					sys.exit(0)
