POLL_RESULTS_FILENAME = 'programming_poll.txt'

QUIT_VALUE = 'quit'

PROMPT = f"""
Why do you like programming?
(Enter '{QUIT_VALUE}' when you are finished.)
> """

responses = []
while True:
    response = input(PROMPT)

    if response == QUIT_VALUE:
        break

    responses.append(response)

with open(POLL_RESULTS_FILENAME, 'a') as output_file:
    for response in responses:
        output_file.write(response)
        output_file.write('\n')
