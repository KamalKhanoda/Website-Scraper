import requests
from bs4 import BeautifulSoup
import  datetime

def get_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all(class_='title')
    
    file = open("headlines.txt", "w",encoding='UTF-8') 
    date = f"Date : {datetime.datetime.now().strftime('%d-%m-%Y')}\n"
    file.write(date)
    file.write(f"\t\t\t\t\tTOP HEADLINES\n")
    file.write("----------------------------------------------------------\n\n")
    for i, headlines in enumerate(headlines, start=1):
        news = f"{i}.    {headlines.get_text(strip=True)}\n" 
        file.write(news)


url = 'https://www.thehindu.com/news/'
get_headlines(url)