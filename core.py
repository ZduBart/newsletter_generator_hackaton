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
            {"role": "system", "content": 'You are an AI assistant specialized in writing summaries and generating DALL-E prompts based on provided information. Your responses should always be in JSON format, structured as follows: {"summary": "{your summary}", "prompt": "{your prompt for DALL-E}"}. Emphasize clarity and conciseness in summaries, and ensure that DALL-E prompts are creatively aligned with the summarys content. Summary must be always in Polish language and not longer than 75 words, while the prompt for DALL-E must be in English.'},
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
            {"role": "system", "content": 'Translate given title into polish, if the title is already in polish language then dont make any changes.'},
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

def generate_opening(all_articles):
    deployment_name = 'gpt4-deployment'
    
    # Create a chat completion request to generate a summary and DALL-E prompt
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": 'In around 50 words, given below summaries of newsletter articles write short general introducton and invite to read newsletter. Write in polish language'},
            {"role": "user", "content": all_articles}
        ],
        max_tokens=1000)
    return response.choices[0].message.content

def generate_summary_line():
    deployment_name = 'gpt4-deployment'
    
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": 'Write one short inspiring, motivational sentence about future of artificial inteligence and its use cases in everyday lives to use as newsletter summary. Write in polish language'}
        ],
        max_tokens=1000)
    return response.choices[0].message.content


def main():
    # all_articles = 'Brazylijski rynek bankowości cyfrowej dynamicznie się rozwija. Nubank o wartości 30 miliardów dolarów ekspansywnie rośnie w całej Ameryce Łacińskiej. Inne cyfrowe banki, takie jak PicPay i Mercado Pago również zyskują popularność, a tradycyjne banki, takie jak Iti i Next wprowadzają swoje cyfrowe odpowiedniki. PagBank, cyfrowy oddział procesora płatności PagSeguro, zgłosił niemal 30 milionów klientów w Brazylii, co stawia go wśród pięciu największych neobanków w Ameryce Łacińskiej pod względem liczby klientów. Rynek cyfrowych banków w kraju zaczął wykazywać oznaki nasycenia, co skłoniło banki do zmiany strategii z szybkiego zdobywania klientów na zwiększanie rentowności. Revolut wprowadził do swojej oferty Inwestycje Pro (Trading Pro) dla zaawansowanych inwestorów w krajach Europejskiego Obszaru Gospodarczego, w tym w Polsce. Dzięki temu klienci mogą korzystać z niższych prowizji. Usługa kosztuje 15 euro miesięcznie, z wyjątkiem planu Ultra, gdzie jest bezpłatna. Inwestycje Pro umożliwiają wyżej limit zleceń kupna lub sprzedaży akcji i funduszy indeksowych ETF. Revolut zapewnił również klientom wydłużone godziny handlu na amerykańskim rynku.'
    print(generate_summary_line())

if __name__ == "__main__":
    main()