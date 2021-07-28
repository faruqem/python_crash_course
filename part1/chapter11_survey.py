class AnonymousSurvey:
    """Collect anonymus answers to a survey question"""

    def __init__(self, question):
        """store question and response"""
        self.question = question
        self.responses = []

    def show_question(self):
        """display the question"""
        print(f"\n{self.question}")

    def store_response(self, new_response):
        """store new response"""
        self.responses.append(new_response)

    def show_results(self):
        """display all survey results"""
        print("\nSurvey results: ")
        for response in self.responses:
            print(f"- {response.title()}")