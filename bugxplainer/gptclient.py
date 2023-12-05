from openai import OpenAI


class ChatGPTClient:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def generate_response(self, issue_content: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are helpful at reviewing Java code and explaining bugs in GitHub issues.",
                },
                {"role": "user", "content": issue_content},
            ],
        )
        return response.choices[0].message.content
