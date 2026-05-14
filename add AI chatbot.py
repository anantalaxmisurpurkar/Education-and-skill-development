from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role":"user",
         "content":"Suggest career path for Python student"}
    ]
)

print(response.choices[0].message.content)
