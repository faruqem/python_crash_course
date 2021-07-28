import unittest
from chapter11_names_func_module import get_formatted_name
'''
class NamesTestCase(unittest.TestCase):
    """unit test for chapter11_func_module"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name("mo", "faruqe")
        self.assertEqual(formatted_name, "Mo Faruqe")

if __name__ == "__main__":
    unittest.main()
'''

'''First, we import unittest and the function we want to test, get_formatted_name(). 
At we create a class called NamesTestCase, which will contain a series of unit tests 
for get_formatted_name(). You can name the class anything you want, but it’s best to 
call it something related to the function you’re about to test and to use the word 
Test in the class name. This class must inherit from the class unittest.TestCase so 
Python knows how to run the tests you write.'''

'''Any method that starts with test_ will be run automatically when we run 
chapeter11_test_name_function.py. Within this test method, we call the function 
we want to test. '''

'''We’re going to run this file directly, but it’s important to note that many testing 
frameworks import your test files before running them. When a file is imported, 
the interpreter executes the file as it’s being imported. The if block at looks 
at a special variable, __name__, which is set when the program is executed. 
If this file is being run as the main program, the value of __name__ is set 
to '__main__'. In this case, we call unittest.main(), which runs the test case. 
When a testing framework imports this file, the value of __name__ won’t be '__main__' 
and this block will not be executed.'''

'''
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''

'''After excuting this file in the output (see above) the dot on the first line of output 
tells us that a single test passed. The next line tells us that Python ran one test, 
and it took less than 0.001 seconds to run. The final OK tells us that all unit 
tests in the test case passed.'''

#If fails:
"""
E
======================================================================
ERROR: test_first_last_name (__main__.NamesTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/faruqe/Faruqe/Books, Tutorials, and Videos/Python Crash Course by Eric Matthes OReilly/python_work/chapeter11_test_name_function.py", line 8, in test_first_last_name
    formatted_name = get_formatted_name("mo", "faruqe")
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
"""

class NamesTestCase(unittest.TestCase):
    """unit test for chapter11_func_module"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name("mo", "faruqe")
        self.assertEqual(formatted_name, "Mo Faruqe")

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name("mo", "faruqe", "uddin")
        self.assertEqual(formatted_name, "Mo Uddin Faruqe")

if __name__ == "__main__":
    unittest.main()

#Now if both test pass:
'''
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
'''

#If one fails out of two
'''
F.
======================================================================
FAIL: test_first_last_middle_name (__main__.NamesTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/faruqe/Faruqe/Books, Tutorials, and Videos/Python Crash Course by Eric Matthes OReilly/python_work/chapeter11_test_name_function.py", line 74, in test_first_last_middle_name
    self.assertEqual(formatted_name, "Mo Uddin Faruqe")
AssertionError: 'Mo Uddin Faruq' != 'Mo Uddin Faruqe'
- Mo Uddin Faruq
+ Mo Uddin Faruqe
?               +


----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
'''