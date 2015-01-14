import os
import sys

def test01(data, **kwarg):
	#print argv
	print "-"*90
	print kwarg['start']

test01("boa",start="North")