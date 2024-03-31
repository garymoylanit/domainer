from openai import OpenAI
client = OpenAI()

wordOne = "power"
wordTwo = "growth"

numberOfNames = 3

# Updated prompt to focus on .com domain name suitability
messageToAI = f"List {numberOfNames} business name suggestions that are suitable for a business that does web development, and digital marketing to help businesses grow and thrive. Each should be catchy, easy to remember, and suitable as a .com domain name. The names should be memorable, linguistically clean, scalable, authentic, emotional, unique. Separate each name with a newline. Ensure the names do not include spaces or special characters."

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a business name creation expert focusing on .com domain names."},
    {"role": "user", "content": messageToAI}
  ]
)

# Assuming the response is formatted with each name on a new line
# Split the response by newline to create an array of names
business_names = response.choices[0].message.content.strip().split('\n')

# Print the array to verify the output
print(business_names)
