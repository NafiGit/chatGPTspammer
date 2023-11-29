import json
from datetime import datetime
from openai import OpenAI

OPENAI_API_KEY=abcd

# Assuming you have your API key stored in a variable named OPENAI_API_KEY
client = OpenAI(api_key=OPENAI_API_KEY)

# Define a list of user prompts
user_prompts = [
    "Compose a poem that explains the concept of recursion in programming.",
    "Explain the principles of object-oriented programming in a creative way.",
    "Discuss the importance of algorithms in solving real-world problems."
]

# Loop through the prompts
for user_prompt in user_prompts:
    # Define the prompt for GPT-3.5-turbo
    prompt = [
        {"role": "user", "content": user_prompt}
    ]

    # Make an API call to generate a completion based on the prompt
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=prompt
    )

    # Extract GPT-3.5-turbo response
    gpt_response = completion.choices[0].message.content

    # Save GPT-3.5-turbo response as JSON in a new file for each prompt
    file_name = f'gpt_response_{datetime.utcnow().strftime("%Y%m%d%H%M%S")}_{user_prompt.replace(" ", "_")}.json'
    response_data = {
        "sender-name": "nafi",
        "prompt-name": user_prompt,
        "gpt-v": "3.5 turbo",
        "timestamp": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC'),
        "prompt-resp": gpt_response,
        "link": "",
    }

    with open(file_name, 'w') as json_file:
        json.dump(response_data, json_file, indent=2)

    print(f"GPT response for prompt '{user_prompt}' saved to file: {file_name}")
