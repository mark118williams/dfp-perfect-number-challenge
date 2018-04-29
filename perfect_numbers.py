# Define exceptions 
class InvalidInputException(Exception):
  pass
class NumberException(Exception):
    pass

def classify(number):
    '''
    Classifies a number as:
    -perfect if the sum of the number's factors equal the number
    -abundant if the sum of the number's factors is greater than the number
    -deficient if the sum of the number's factors if less than the number 

    The number must be a positive integer
    '''

    # Cast the input to an integer and raise an error if this is not possible 
    try:
        int(number)
        number = int(number)
    except:
        raise InvalidInputException('Input %s not an integer' %number)

    # The number 0 cannot be perfect, abundant or deficient
    if number == 0:
        raise NumberException('classifcation is not relevent to 0')

    # Negative numbers cannot be perfect, abumdant or deficient 
    if number < 0:
        raise NumberException('%s is a negative number. Classifcation is not relevent to negative numbers' %number)

    # Create an empty list and populate it with the factors of the input excluding the input itself 
    factors = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    
    # The input is perfect if the sum of the factors is equal to the input
    if sum(factors) == number:
        return 'perfect'
    # The input is abundant if the sum of the factors is greater than the input     
    if sum(factors) > number:
        return 'abundant'
    # The input is deficient if the sum of the factors if less than the input 
    if sum(factors) <number:
        return 'deficient'