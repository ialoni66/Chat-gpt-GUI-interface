import openai

class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self,user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5,
        ).choices[0].text
        return response



