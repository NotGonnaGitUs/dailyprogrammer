# -*- coding: utf-8 -*-
#Challenge # 241 [easy] Unicode Chess
def load_board():
	for x in range(1,9):
		for y in range(1,9):
			if (x%2==y%2):
				print  u"\u25a1",
				
			else:
				print  	u"\u25a0",
				
		print 
	print "   a b c d e f g h"

def import_fen(fen):
	rows = fen.split('/')
	for each_row in rows:
		for each in each_row:
			if each.isdigit():
				for i in range(0,int(each)):
					print " ",
			else:
				print each,
		print ""

load_board()
import_fen('snbqkbns/pppppppp/8/8/4P3/8/PPPP1PPP/SNBQKBNS')