#################
# Getting Started
#################
# pip install beautifulsoup4

from bs4 import BeautifulSoup

html = """
        <!DOCTYPE html><html><head><title>Example HTML</title></head><body><h1>Hello, World!</h1><p>A simple HTML page for testing web scraping with BeautifulSoup.</p>
                <a class='link' href='www.miuul.com' target='blank' aria-label='Miuul (Opens Miuul Page)'>Click</a>
                <li>Outsider</li>
                <ul>
                    <li>Item 1</li>
                    <li>Item 2</li>
                </ul>
            </body>
            </html>

"""

# soup nesnesi oluşturup attiributeleri girmemiz gerekiyor
# 1 - beautiful soup hangi değişkende çalışıcak
# 2 - xml ve html işleyebilen bu kütüphaneden hangisini işlemek istiyoruz
soup = BeautifulSoup(html, "html.parser")

title = soup.title
print(title)
print(type(title))

# title değişkeni obje türünde ve string değil
ttext = title.text # title.string olarak da kullanılabilir
print(ttext)
print(type(ttext))

print(soup.prettify()) # dağınık html kodunu düzenler

# ul listesinin içinden li yi çekiyoruz
ul = soup.ul
print(ul)
print(type(ul))

print(ul.li)