import json
import random

with open('tossups.json',encoding='utf8') as tossup_file:
    question_lines = tossup_file.readlines()

tossups = []
for question_line in question_lines:
    tossups.append(json.loads(question_line))

history_tossups = []
literature_tossups = []
science_tossups = []
fine_arts_tossups = []
religion_tossups = []
mythology_tossups = []
philosophy_tossups = []
social_science_tossups = []
current_events_tossups = []
geography_tossups = []
other_academic_tossups = []
trash_tossups = []
for tossup in tossups:
    category = tossup['category']
    if category == 'History':
        history_tossups.append(tossup)
    if category == 'Literature':
        literature_tossups.append(tossup)
    if category == 'Science':
        science_tossups.append(tossup)
    if category == 'Fine Arts':
        fine_arts_tossups.append(tossup)
    if category == 'Religion':
        religion_tossups.append(tossup)
    if category == 'Mythology':
        mythology_tossups.append(tossup)
    if category == 'Philosophy':
        philosophy_tossups.append(tossup)
    if category == 'Social Science':
        social_science_tossups.append(tossup)
    if category == 'Current Events':
        current_events_tossups.append(tossup)
    if category == 'Geography':
        geography_tossups.append(tossup)
    if category == 'Other Academic':
        other_academic_tossups.append(tossup)
    if category == 'Trash':
        trash_tossups.append(tossup)
    
print(len(history_tossups), 'History tossups')
print(len(literature_tossups), 'Literature tossups')
print(len(science_tossups), 'Science tossups')
print(len(fine_arts_tossups), 'Fine Arts tossups')
print(len(religion_tossups), 'Religion tossups')
print(len(mythology_tossups), 'Mythology tossups')
print(len(philosophy_tossups), 'Philosophy tossups')
print(len(social_science_tossups), 'Social Science tossups')
print(len(current_events_tossups), 'Current Events tossups')
print(len(geography_tossups), 'Geography tossups')
print(len(other_academic_tossups), 'Other Academic tossups')
print(len(trash_tossups), 'Trash tossups')

history_count = int(input('How many people want History questions? '))
literature_count = int(input('How many people want Literature questions? '))
science_count = int(input('How many people want Science questions? '))
fine_arts_count = int(input('How many people want Fine Arts questions? '))
religion_count = int(input('How many people want Religion questions? '))
mythology_count = int(input('How many people want Mythology questions? '))
philosophy_count = int(input('How many people want Philosophy questions? '))
social_science_count = int(input('How many people want Social Science questions? '))
current_events_count = int(input('How many people want Current Events questions? '))
geography_count = int(input('How many people want Geography questions? '))
other_academic_count = int(input('How many people want Other Academic questions? '))
trash_count = int(input('How many people want Trash questions? '))
categories = ['History', 'Literature', 'Science', 'Fine Arts', 'Religion', 'Mythology', \
    'Philosophy', 'Social Science', 'Current Events', 'Geography', 'Other Academic', 'Trash']

def ask_random_question_from_list(list):
    tossup = random.choice(list)
    print(tossup['question_sanitized'])
    print('ANSWER: ', tossup['answer'])

while True:
    random_category = random.choices(categories, weights=(history_count, literature_count, science_count, fine_arts_count, religion_count,\
        mythology_count, philosophy_count, social_science_count, current_events_count, geography_count,\
        other_academic_count, trash_count))[0]
    print('Category: ', random_category)
    if random_category == 'History':
        ask_random_question_from_list(history_tossups)
    if random_category == 'Literature':
        ask_random_question_from_list(literature_tossups)
    if random_category == 'Science':
        ask_random_question_from_list(science_tossups)
    if random_category == 'Fine Arts':
        ask_random_question_from_list(fine_arts_tossups)
    if random_category == 'Religion':
        ask_random_question_from_list(religion_tossups)
    if random_category == 'Mythology':
        ask_random_question_from_list(mythology_tossups)
    if random_category == 'Philosophy':
        ask_random_question_from_list(philosophy_tossups)
    if random_category == 'Social Science':
        ask_random_question_from_list(social_science_tossups)
    if random_category == 'Current Events':
        ask_random_question_from_list(current_events_tossups)
    if random_category == 'Geography':
        ask_random_question_from_list(geography_tossups)
    if random_category == 'Other Academic':
        ask_random_question_from_list(other_academic_tossups)
    if random_category == 'Trash':
        ask_random_question_from_list(trash_tossups)
    input()