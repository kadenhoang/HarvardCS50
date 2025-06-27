from calculator import square

#use "pytest" in the terminal to test the code
#it is easier to use it than writing long code to test the function

# seperate the negative and positive so that every assertion can be tested
# when every assertion is in a function, pytest test until there is an error then stop
# it does not go for every line in that fucntion

# when using pytest, the name of the function must start wth test_
def test_positive_square():
    #use "assert" to determine the varialbe
    assert square(2) == 4
    assert square(3) == 9

def test_negative_square():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0



