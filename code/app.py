from pages.quotes_page import QuotesPage, InvalidTagForAuthorError
from selenium import webdriver

# chrome = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
# chrome.get('http://quotes.toscrape.com/search.aspx')
# page = QuotesPage(chrome)

# author = input("Enter the author you'd like quotes from: ")
# page.select_author(author)

# tags = page.get_available_tags()
# print("Select one of these tags: [{}]".format(" | ".join(tags)))
# selected_tag = input("Enter your tag: ")

# page.select_tag(selected_tag)
# page.search_button.click()
# print(page.quotes)

# --

try:

    author = input("Enter the author you'd like quotes from: ")
    chrome = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
    chrome.get('http://quotes.toscrape.com/search.aspx')
    page = QuotesPage(chrome)
    page.select_author(author)
    tags = page.get_available_tags()
    print("Select one of these tags: [{}]".format(" | ".join(tags)))

    tag = input("Enter your tag: ")

    # chrome = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
    # chrome.get('http://quotes.toscrape.com/search.aspx')
    page = QuotesPage(chrome)

    print(page.search_for_quotes(author, tag))
#     daca autorul e ok dar tagul nu il gaseste da
#     InvalidTagForAuthorError f"Author '{author_name}' does not have any quotes tagged with '{tag_name}'."
#     daca nu gaseste autorul da exception(An unknown error ...) .
except InvalidTagForAuthorError as e:
    print(e)
#     daca nu prinde nici o exceptie pana aici atunci va prinde Exception - pt ca Exception is the base class for every exception
except Exception:
    print("An unknown error occurred. Please try again.")