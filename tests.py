# Import module
from perfect_numbers import classify
def function_test():
	# Ensure 6 is classified as a perfect numbe 
    assert classify(6) == 'perfect'
    # Ensure 12 is classified as an abundant number
    assert classify(12) == 'abundant'
    # Ensure 8 in classified as a deficient number
    assert classify(8) == 'deficient'

function_test()