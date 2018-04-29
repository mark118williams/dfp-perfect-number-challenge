# Import module
from perfect_numbers import classify
def function_test():
	# Ensure 6 is classified as a perfect numbe 
    assert classify(6) == 'perfect'
    assert classify(12) == 'abundant'
    assert classify(8) == 'deficient'

function_test()