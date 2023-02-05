import openai
import requests
from bs4 import BeautifulSoup

url = "https://www.allrecipes.com/recipe/257206/ultimate-banana-muffins/"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()

openai.api_key = ""

question = "Extract only the ingredients from the following text: \n" + text

response = openai.Completion.create(model="text-davinci-003", prompt=question, temperature=0, max_tokens=100)

print(response)