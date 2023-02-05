from recipe_scrapers import scrape_me
import openai
import json

# Open AI Key
openai.api_key = "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"


async def parse_menu(url):
    # Grabbing link for recipe
    scraper = scrape_me(url)

    # First part of prompt
    pre_question = "\n\nI am a recipe ingredient scraping bot. My purpose is to convert natural-language ingredients " \
                   "list into formatted JSON output. Given the following input: \n"
    # List reference
    reference = ['2 large eggs', 'Pinch fine sea salt', '1/2 Tbsp unsalted butter', '3 sweet potatoes',
                 '1/4 cup shredded mozzarella (low moisture, part-skim)', '6 chives']
    ref_formatted = "\n".join([f' \'{thing}\',' for thing in reference])
    print("FORMATTED JSON --> \n" + ref_formatted)
    scraper_formatted = "\n".join([f' \'{thing}\',' for thing in scraper.ingredients()])

    # Opening json reference
    with open("./extract_correct.json") as file:
        extract_correct = json.load(file)
        print("CORRECT JSON --> \n" + json.dumps(extract_correct))

    # Forming question
    interlude = "\n and I will produce the following JSON output: \n"
    new_output = "\n and my new input is: \n"
    question = f"{pre_question} ```\n{ref_formatted}\n``` {interlude} ```\n{json.dumps(extract_correct)}\n``` " \
               f"{new_output} ```\n{scraper_formatted}\n```"
    print(question)

    # Asking question
    response = await openai.Completion.acreate(model="text-davinci-003", prompt=question, temperature=0, max_tokens=3000)
    # Printing question
    print(response["choices"][0]["text"])
    return response["choices"][0]["text"]


parse_menu('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')
