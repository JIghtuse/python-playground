from survey import AnonymousSurvey

QUIT_VALUE = 'q'

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
survey.show_question()
print(f"Enter '{QUIT_VALUE}' at any time to quit.\n")
while True:
    response = input("Language:")
    if response == QUIT_VALUE:
        break
    survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
survey.show_results()