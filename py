pip install openai

import openai
openai.api_key = "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"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

# Example usage
prompt = "What is the meaning of life?"
response = generate_response(prompt)
print(response)
