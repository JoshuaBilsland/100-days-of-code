from bs4 import BeautifulSoup

with open("day-045/day-045_lesson_code_&_notes/bs4_start/website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.prettify())
