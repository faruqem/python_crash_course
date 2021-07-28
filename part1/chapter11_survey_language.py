from chapter11_survey import AnonymousSurvey

question = "What language you learned first?"

my_survey = AnonymousSurvey(question)

"""display the question"""
my_survey.show_question()
print("Enter q to exit\n")
while True:    
    response = input("Language: ")
    if (response == "q"):
        break
    my_survey.store_response(response)

#Show survey results
my_survey.show_results()