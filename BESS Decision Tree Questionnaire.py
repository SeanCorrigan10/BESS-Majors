import math
import pandas as pd
import numpy as np

# base variables
# strength and conditioning
# exercise physiology
# sport coaching
# physical activity and health
# applied sport science 

Course_options = np.array([['Exercise Physiology','', 0],
                            ['Applied Sport Science', '', 0],
                            ['Strength and Conditioning','', 0],
                            ['Sports Coaching', '', 0],
                            ['Physical Activity and Health', '', 0],
                            ['Applied Sport Science', 'Exercise Physiology', 0],
                            ['Applied Sport Science', 'Strength and Conditioning', 0],
                            ['Applied Sport Science', 'Physical Activity and Health', 0],
                            ['Exercise Physiology', 'Strength and Conditioning', 0],
                            ['Exercise Physiology', 'Physical Activity and Health', 0],
                            ['Strength and Conditioning', 'Physical Activity and Health', 0]])

Possible_course_options = pd.DataFrame(Course_options, columns=['Major 1', 'Major 2', 'Score'])

major_weighting = {'s_c' : 0, 
                   'e_p' : 0, 
                   'sp_c' : 0, 
                   'p_a_h' : 0, 
                   'app_ss' : 0}

role_rank_options = [   "Monitor and assess physical activity and sedentary behaviour in relation to current policy",
                        "Develop and implement projects working in a team environment and evaluate program effectiveness",
                        "Monitor and interpret individual responses during exercise and to training programs",
                        "Design, deliver and evaulate exericse programs to improve specific paramaters of health, wellbeing and performance capacity",
                        "Utilise technology to conduct exercise testing",
                        "Identify performance enhancement statergies to be implemented during training and performances",
                        "Effectively lead a team or group to a common outcome through teaching and collaboration"
                    ]

sorted_role_rank_options = sorted(role_rank_options)

role_rank_quest = {"Rank the top 3 roles that interest you for your future career? eg. 3, 5, 1" : sorted_role_rank_options}

rank_list = ['first', 'second', 'third']

for question, option in role_rank_quest.items():
    print(f'\n ----------------------------DECISION TREE QUIZ START---------------------------- \n{question} \n')

    sorted_options = sorted(option)
    for label, options in enumerate(sorted_options):
        labels = label +1
        print(f'{labels}) {options}')

for number in rank_list:
    answer = int(input(f'Which would be ranked {number}? \n'))
    if number == 'first':
        value_add = 0.50
        if answer == 1:
            major_weighting['p_a_h'] +=    value_add * 1
            major_weighting['e_p'] +=      value_add * 1
            major_weighting['s_c'] +=      value_add * 1
            major_weighting['sp_c'] +=     value_add * 1
        elif answer == 2:
            major_weighting['p_a_h'] +=    value_add * 1
            major_weighting['e_p'] +=      value_add * 0.5
            major_weighting['app_ss'] +=   value_add * 0.5
            major_weighting['sp_c'] +=     value_add * 0.5
        elif answer == 3:
            major_weighting['p_a_h'] +=    value_add * 0.5
            major_weighting['s_c'] +=      value_add * 1
            major_weighting['sp_c'] +=     value_add * 1
        elif answer == 4:
            major_weighting['s_c'] +=      value_add * 0.5
            major_weighting['app_ss'] +=   value_add * 1
            major_weighting['sp_c'] +=     value_add * 1
        elif answer == 5:
            major_weighting['p_a_h'] +=    value_add * 1
        elif answer == 6:
            major_weighting['e_p'] +=      value_add * 1
            major_weighting['s_c'] +=      value_add * 1
            major_weighting['app_ss'] +=   value_add * 1
        elif answer == 7:
            major_weighting['e_p'] +=      value_add * 1
            major_weighting['app_ss'] +=   value_add * 1

    if number == 'second':
        value_add = 0.30
        if answer == 1:
            major_weighting['p_a_h'] +=    value_add * 1
            major_weighting['e_p'] +=      value_add * 1
            major_weighting['s_c'] +=      value_add * 1
            major_weighting['sp_c'] +=     value_add * 1
        elif answer == 2:
            major_weighting['p_a_h'] +=    value_add * 1
            major_weighting['e_p'] +=      value_add * 0.5
            major_weighting['app_ss'] +=   value_add * 0.5
            major_weighting['sp_c'] +=     value_add * 0.5
        elif answer == 3:
            major_weighting['p_a_h'] +=    value_add * 0.5
            major_weighting['s_c'] +=      value_add * 1
            major_weighting['sp_c'] +=     value_add * 1
        elif answer == 4:
            major_weighting['s_c'] +=      value_add * 0.5
            major_weighting['app_ss'] +=   value_add * 1
            major_weighting['sp_c'] +=     value_add * 1
        elif answer == 5:
            major_weighting['p_a_h'] +=    value_add * 1
        elif answer == 6:
            major_weighting['e_p'] +=      value_add * 1
            major_weighting['s_c'] +=      value_add * 1
            major_weighting['app_ss'] +=   value_add * 1
        elif answer == 7:
            major_weighting['e_p'] +=      value_add * 1
            major_weighting['app_ss'] +=   value_add * 1

    if number == 'third':
        value_add = 0.20
        if answer == 1:
            major_weighting['p_a_h'] +=    value_add * 1
            major_weighting['e_p'] +=      value_add * 1
            major_weighting['s_c'] +=      value_add * 1
            major_weighting['sp_c'] +=     value_add * 1
        elif answer == 2:
            major_weighting['p_a_h'] +=    value_add * 1
            major_weighting['e_p'] +=      value_add * 0.5
            major_weighting['app_ss'] +=   value_add * 0.5
            major_weighting['sp_c'] +=     value_add * 0.5
        elif answer == 3:
            major_weighting['p_a_h'] +=    value_add * 0.5
            major_weighting['s_c'] +=      value_add * 1
            major_weighting['sp_c'] +=     value_add * 1
        elif answer == 4:
            major_weighting['s_c'] +=      value_add * 0.5
            major_weighting['app_ss'] +=   value_add * 1
            major_weighting['sp_c'] +=     value_add * 1
        elif answer == 5:
            major_weighting['p_a_h'] +=    value_add * 1
        elif answer == 6:
            major_weighting['e_p'] +=      value_add * 1
            major_weighting['s_c'] +=      value_add * 1
            major_weighting['app_ss'] +=   value_add * 1
        elif answer == 7:
            major_weighting['e_p'] +=      value_add * 1
            major_weighting['app_ss'] +=   value_add * 1

    #print(f'{answer}')
#def ranked_q()

remainder_questions = {'At what level do you want to work with people?' : ["Any",
                                                                           "One on one",
                                                                           "Populations and large groups",
                                                                           "Teams and small groups"],
                        'Do you want to work with one of the specific populations?' : ["Athletes and sports teams",
                                                                                       "Communities, organisations and government",
                                                                                       "General population",
                                                                                       "Individuals with medical conditions",
                                                                                       "Not specifically"],
                        'What do you enjoy/are best at?' : ['Developing relationships',
                                                        'Working with data',
                                                        'Written communication']}


q1_total = 0
for key, value in major_weighting.items():
    #print(value)
    q1_total += value

for key, value in major_weighting.items():
    major_weighting[key] = value / q1_total
    #print(f'{key} : {major_weighting[key]}')


for question, alternatives in remainder_questions.items():
    print(f'\n {question}')
    for label, option in enumerate(alternatives):
        number_label = label + 1
        print(f'{number_label}) {option}')
    
    response = int(input(' \n Answer (eg. 2): \n'))

    if question == 'At what level do you want to work with people?':
        value_multiplier = 0.1
        if response == 2:
            major_weighting['p_a_h'] *=    1 + value_multiplier * 0.5
            major_weighting['e_p'] *=      1 + value_multiplier * 1
            major_weighting['s_c'] *=      1 + value_multiplier * 0.5
            major_weighting['app_ss'] *=      1 + value_multiplier * 0.5
            major_weighting['sp_c'] *=     1 + value_multiplier * 0.5
        elif response == 3:
            major_weighting['p_a_h'] *=    1 + value_multiplier * 1
        elif response == 4:
            major_weighting['e_p'] *=      1 + value_multiplier * 0.5
            major_weighting['s_c'] *=      1 + value_multiplier * 1
            major_weighting['app_ss'] *=      1 + value_multiplier * 1
            major_weighting['sp_c'] *=     1 + value_multiplier * 1

    elif question == 'Do you want to work with one of the specific populations?':
        value_multiplier = 0.1
        if response == 1:
            major_weighting['s_c'] *=      1 + value_multiplier * 1
            major_weighting['app_ss'] *=      1 + value_multiplier * 1
            major_weighting['sp_c'] *=     1 + value_multiplier * 1
        elif response == 2:
            major_weighting['p_a_h'] *=    1 + value_multiplier * 1
        elif response == 3:
            major_weighting['p_a_h'] *=    1 + value_multiplier * 0.5
            major_weighting['e_p'] *=      1 + value_multiplier * 0.5
            major_weighting['s_c'] *=      1 + value_multiplier * 0.5
            major_weighting['app_ss'] *=      1 + value_multiplier * 0.5
            major_weighting['sp_c'] *=     1 + value_multiplier * 0.5
        elif response == 4:
            major_weighting['e_p'] *=    1 + value_multiplier * 1

    elif question == 'What do you enjoy/are best at?':
        if response == 1:    
            major_weighting['e_p'] *=      1 + value_multiplier * 1
            major_weighting['s_c'] *=      1 + value_multiplier * 1
            major_weighting['app_ss'] *=      1 + value_multiplier * 0.5
            major_weighting['sp_c'] *=     1 + value_multiplier * 1
        elif response == 2:
            major_weighting['p_a_h'] *=    1 + value_multiplier * 0.5
            major_weighting['e_p'] *=      1 + value_multiplier * 0.5
            major_weighting['s_c'] *=      1 + value_multiplier * 0.5
            major_weighting['app_ss'] *=      1 + value_multiplier * 1
            major_weighting['sp_c'] *=     1 + value_multiplier * 0.5
        elif response == 3:
            major_weighting['p_a_h'] *=    1 + value_multiplier * 1

q1_total = 0
for key, value in major_weighting.items():
    #print(value)
    q1_total += value

majors = ['Strength and Conditioning', 'Exercise Physiology', 'Sport Coaching', 'Physical Activity and Health', 'Applied Sport Science']
q_result = []
results_df = pd.DataFrame(columns= ['Field', 'Fit %'])
results_df['Field'] = majors

for key, value in major_weighting.items():
    major_weighting[key] = value / q1_total
    q_result.append(major_weighting[key])
    #print(f'\n{key} : {major_weighting[key]}')

results_df['Fit %'] = q_result

results_df = results_df.sort_values(by=['Fit %'], ascending=False, ignore_index=True)
print(results_df)

top_3 = []
for field in results_df['Field'][0:3]:
    top_3.append(field)
print(f'\n Your top three results were: \n 1) {top_3[0]} \n 2) {top_3[1]} \n 3) {top_3[2]}')

for index in Possible_course_options.index:
    Possible_course_options['Score'][index] = int(Possible_course_options['Score'][index])

field_count = 0
for field in top_3:
    field_count += 1
    field_score = 4 - field_count
    for index in Possible_course_options.index:
        if Possible_course_options['Major 1'][index] == field:
            Possible_course_options['Score'][index] = int(Possible_course_options['Score'][index]) + field_score
        if Possible_course_options['Major 2'][index] == field:
            Possible_course_options['Score'][index] = int(Possible_course_options['Score'][index]) + field_score


Possible_course_options = Possible_course_options.sort_values(by=['Score'], ascending=False, ignore_index=True)

print(Possible_course_options)

final_list = []

for index in Possible_course_options.index[0:5]:
    if Possible_course_options['Major 1'][index] != '' and Possible_course_options['Major 2'][index] != '':
        output = Possible_course_options['Major 1'][index] + ' + ' + Possible_course_options['Major 2'][index] + ' - Double Major'
        final_list.append(output)
    elif Possible_course_options['Major 1'][index] != '' and Possible_course_options['Major 2'][index] == '':
        output = Possible_course_options['Major 1'][index] + ' - Single Major'
        final_list.append(output)

print(f'\n Your top 5 suggested course options are: \n 1) {final_list[0]} \n 2) {final_list[1]} \n 3) {final_list[2]} \n 4) {final_list[3]} \n 5) {final_list[4]}\n')
