import os
from together import Together
import apikey as apikey
import base64
# Initialize the API client
client = Together(api_key=apikey.yourapi)
def print_welcome_message():
    border = "=" * 60
    welcome_text = "𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕥𝕠 𝕡𝕪𝕔𝕙𝕒𝕥!!"
    spacing = " " * ((60 - len(welcome_text)) // 2)

    print(border)
    print(f"{spacing}{welcome_text}{spacing}")
    print(border)
def chatbot():
   
    
    while True:
        user_input = input("Would you like to (1) chat or (2) generate an image? (type 'quit' to exit): ")
        
        if user_input == "1":
            chat()
        elif user_input == "2":
            image_generation()
        elif user_input.lower() == "quit":
            break
        else:
            print("Invalid input. Please try again.")

def chat():
    while True:
        user_input = input("YOU: ")
        
        if user_input.lower() == 'quit':
            break
        
        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
            messages=[
                {
                    "role": "user",
                    "content": user_input
                },
            ],
            max_tokens=512,
            temperature=0.7,
            top_p=0.7,
            top_k=50,
            repetition_penalty=1,
            stop=[""],
        )
        
        print(f"PYCHAT: {response.choices[0].message.content}")

def image_generation():
    prompt = input("Enter a prompt for image generation: ")
    
    response = client.images.generate(
        prompt=prompt,
        model="stabilityai/stable-diffusion-xl-base-1.0",
        width=1024,
        height=1024,
        steps=40,
        n=1,
        seed=7821
    )
    
    for i, image in enumerate(response.data):
        # Decode the base64 image data
        image_data = base64.b64decode(image.b64_json)
        
        # Write the decoded data to a PNG file
        with open(f"generated_image_{i}.png", "wb") as f:
            f.write(image_data)

    print("Images generated and saved as PNG files.")

# Start the chatbot application
print_welcome_message()
chatbot()
