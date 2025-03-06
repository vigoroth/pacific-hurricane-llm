from bs4 import BeautifulSoup

with open('../html/test.txt', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

text = soup.get_text()
with open('../html/test_parsed.txt', 'w', encoding='utf-8') as file:
    file.write(text)