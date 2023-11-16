from newspaper import Article
from openai import AzureOpenAI
import json
import os
import dotenv

# Load environment variables from the .env file
dotenv.load_dotenv()

# Initialize the AzureOpenAI client
client = AzureOpenAI(
    api_key=os.getenv("API_KEY"),
    api_version="2023-12-01-preview",
    azure_endpoint=os.getenv("AZURE_ENDPOINT")
)

def get_article_url():
    # url = input("Podaj url artykułu ")
    url = "https://www.bbc.co.uk/news/uk-politics-67403223"
    return url

def extract_article(url):
    # Download and parse the article
    article = Article(url)
    article.download()
    article.parse()
    return article.title, article.text

def generate_summary(article_text):
    deployment_name = 'gpt4-deployment'
    
    # Create a chat completion request to generate a summary and DALL-E prompt
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": 'You are an AI assistant specialized in writing summaries and generating DALL-E prompts based on provided information. Your responses should always be in JSON format, structured as follows: {"summary": "{your summary}", "prompt": "{your prompt for DALL-E}"}. Emphasize clarity and conciseness in summaries, and ensure that DALL-E prompts are creatively aligned with the summarys content. Summary must be always in Polish language, while the prompt for DALL-E must be in English.'},
            {"role": "user", "content": article_text}
        ],
        max_tokens=1000
    )
    
    # Parse the response and retrieve summary and prompt
    response_data = json.loads(response.choices[0].message.content)
    summary = response_data.get('summary', '')
    prompt = response_data.get('prompt', '')
    return summary, prompt

def translate_title(article_title):
    deployment_name = 'gpt4-deployment'
    
    # Create a chat completion request to generate a summary and DALL-E prompt
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": 'Translate given title into polish'},
            {"role": "user", "content": article_title}
        ],
        max_tokens=1000
    )
    return response.choices[0].message.content
    # Parse the response and retrieve summary and prompt
    # response_data = json.loads(response.choices[0].message.content)
    # summary = response_data.get('summary', '')
    # prompt = response_data.get('prompt', '')
    # return summary, prompt

def generate_image(prompt):
    deployment_name = 'dall-e'
    
    # Generate an image based on the DALL-E prompt
    response = client.images.generate(model=deployment_name, prompt=prompt, n=1, response_format="url")
    return response.data[0].url



def main():
    url = get_article_url()
    article_title, article_text = extract_article(url)
    summary, prompt = generate_summary_prompt(article_text)
    print(prompt)
    print('\nText:', text)
    print("\nTitle:", title)
    print("\nSummary:", summary)
    image = generate_image(prompt)
    print(image)


if __name__ == "__main__":
   print(client)
   print(generate_image('plaza'))