# importing beautiful soup and requests
from bs4 import BeautifulSoup
import requests
import time

# Occupation code
def occupation():
    occupation = pres_soup.find_all('div', class_='hlist hlist-separated')
    for job in occupation:
        job = job.text

    return job

# None Check
def birth_name():
    birth_name = pres_soup.find('div', class_='nickname')
    nulval = str(birth_name)
    if nulval != 'None':
        birth_name = birth_name.text


    return birth_name

#Checks whose born in november
def NovemberBorn():
    birthyear = int(birthday[0:4])
    birthmonth = (birthday[5:7])
    birthdate = (birthday[8:10])

    if birthmonth == "11":
        NovName.append(name)

#Checks who was a lawyer before becoming a politician
def lawyerOrNot():
    if "lawyer" in job or "journalist":
        lawyerName.append(name)

# Initialisng the file and other variables
f = open('Politicians.csv', 'w')
NovName = []
lawyerName = []

# requesting data from the chosen website and using beautiful soup to extract the data
main_website = requests.get("https://en.wikipedia.org/wiki/Category:20th-century_presidents_of_the_United_States").text
soup = BeautifulSoup(main_website, 'lxml')

#finding the president link
president_link_grp = soup.find('div', class_='mw-category')
for president_link in president_link_grp:
    link = president_link.ul.li.a['href']
    link = f"https://en.wikipedia.org{link}"

    # requesting data from a series of links
    html_text = requests.get(link).text
    pres_soup = BeautifulSoup(html_text, 'lxml')
    president = pres_soup.find('div', class_='mw-parser-output')

    # Finding specific data
    name = pres_soup.find('div', class_='fn').text
    birthname = birth_name()
    birthday = pres_soup.find('span', class_='bday').text
    job = occupation()

    print(f"Politician Name: {name}\n")
    print(f"Birth Name: {birthname}\n")
    print(f"Birthday: {birthday}\n")
    print(f"Occupation: {job}\n")
    print(f"Link: {link}\n")
    print("\n")

    time.sleep(1)

    NovemberBorn()
    lawyerOrNot()


print(f"These people we born in the same month as me:")
for those in NovName:
    print(those)
print(" ")

print(f"These people were lawyers or journalists before politicians:")
lawCount = 0
for them in lawyerName:
    lawCount = lawCount + 1
    print(them)
print(" ")
print(f"{lawCount} presidents were lawyers or journalists before politicians.")
print("Suggesting that being a lawyer or a journalist was an important and common characteristic to have among politicians")
print(" ")

print("CSV file updated")