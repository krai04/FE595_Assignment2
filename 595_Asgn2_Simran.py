import requests
import pandas as pd
from bs4 import BeautifulSoup

# create an empty dictionary to store output later
data = {}

def get_data():
    # request access to the given url
    result = requests.get("http://3.95.249.159:8000/random_company")

    # ensure to get 200 which means I have access to the page
    # print(result.status_code)
    # print(result.headers)

    # extract content of the page
    source = result.content
    # print(source)

    # pass source variable in beautifulsoup class
    soup = BeautifulSoup(source, 'html.parser')

    # find all lists in the url
    lists = soup.find_all("li")
    # print(lists)

    # extract name and purpose from the list
    for list in lists:
        if "Name" in list.text:
            name = list.string[6:]

        elif "Purpose" in list.text:
            purpose = list.string[8:]

    return name,purpose

# to print the result 50 times and store output in a csv
i = 0
sr_no=1

# to call function 50 times to get different values
while i < 50:
    Name, Purpose = get_data()
    i += 1

    data[sr_no] = [Name,Purpose]
    sr_no += 1

# create a dataframe to store Name and Purpose
df = pd.DataFrame.from_dict(data, orient = 'index', columns = ["Name", "Purpose"])
# export the dataframe to csv
df.to_csv('Simran_results_Assignment2.csv')
##### Review : Good Code 5/5  ( Reviewed by Kshitij Rai )
