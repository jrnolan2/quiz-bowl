import json
import random

# Read in tossups from tossups.json file
print('Reading in database.')
with open('tossups.json',encoding='utf8') as tossup_file:
    question_lines = tossup_file.readlines()

tossups = []
for question_line in question_lines:
    tossups.append(json.loads(question_line))

# Split tossups based on their category
categories = ['History','Literature','Science','Fine Arts','Religion','Mythology','Philosophy','Social Science','Current Events','Geography','Other Academic','Trash']
tossups_per_category = [[] for _ in range(len(categories))]
for tossup in tossups:
    category = tossup['category']
    tossups_per_category[categories.index(category)].append(tossup)
    
# Print out number of questions in each category
for category_name, tossups in zip(categories,tossups_per_category):
    print(len(tossups), category_name, 'tossups')

# Get number of people interested in each category
popularity_of_categories = []
for category in categories:
    popularity = int(input('How many people want ' + category + ' questions? '))
    popularity_of_categories.append(popularity)

# Function: asks a random question out of list of tossups
def ask_random_question_from_list(list):
    tossup = random.choice(list)
    print(tossup['question_sanitized'])
    print('ANSWER:', tossup['answer_sanitized'])

# Infinitely ask tossups in the categories weighted by the number of people interested in each category
while True:
    random_category = random.choices(categories, weights=popularity_of_categories)[0]
    print('Category:', random_category)
    ask_random_question_from_list(tossups_per_category[categories.index(random_category)])
    input()