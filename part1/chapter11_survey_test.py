import unittest
from chapter11_survey import AnonymousSurvey

'''
class TestAnonymusSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "What language you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")
        self.assertIn("English", my_survey.responses)
    
    def test_store_three_responses(self):
        question = "What language you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ["Bangla", "English", "French"]

        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == "__main__":
    unittest.main()
'''

#Result:
"""
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
"""

#After adding the second method:
"""
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
"""

"""
The setUp() Method
On top created a new instance of AnonymousSurvey in each test method, and we 
created new responses in each method. The unittest.TestCase class has a setUp() 
method that allows you to create these objects once and then use them in each 
of your test methods. When you include a setUp() method in a TestCase class, 
Python runs the setUp() method before running each method starting with test_. A
ny objects created in the setUp() method are then available in each 
test method you write.
"""

class TestAnonymusSurvey(unittest.TestCase):

    def setUp(self):
        question = "What language you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["Bangla", "English", "French"]

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn("Bangla", self.my_survey.responses)
    
    def test_store_three_responses(self):
        self.my_survey.store_response(self.responses)
        responses = ["Bangla", "English", "French"]

        for response in self.responses:
            self.my_survey.store_response(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == "__main__":
    unittest.main()

'''
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
'''

'''
When a test case is running, Python prints one character for each unit test as 
it is completed. A passing test prints a dot, a test that results in an error 
prints an E, and a test that results in a failed assertion prints an F. This is 
why you’ll see a different number of dots and characters on the first line of 
output when you run your test cases. If a test case takes a long time to run 
because it contains many unit tests, you can watch these results to get a sense 
of how many tests are passing.
'''