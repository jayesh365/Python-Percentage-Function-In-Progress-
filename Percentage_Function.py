# Prompt the user with a welcome
print('\nWelcome to the Percentage Calculator!\n\n')
# ask the user which service they would like to use
print('Which Calculator would you like to use?\n')
# display all services
print('1) What do I need to get for my final? \n2) What is my average now? \n ')
choice = input()
if(choice is '1'):
    # ask the weight of the final
    weight = input('How much is you final worth as a %? ')
    weight = float(weight)
    x = 100 - float(weight)
    # ask what they have on the completed weight
    have = input('What is your % mark for the completed ' + str(x) + '%? ')
    have = float(have)
    # ask what final mark they want
    mark_want = input('What final mark do you want? ')
    mark_want = float(mark_want)
    # now the math bit
    # take what they have and multiply it with the total completed %
    acc_completed = have*(x/100)
    # now we need to calculate what they need on the exam to get their
    # desired final mark
    need_exam = (mark_want-acc_completed)
    need_exam = (need_exam/weight)*100
    print('You need ' + str(need_exam) + '% on the final exam in order to get '
          + str(mark_want) + '% as the final mark!')
   
elif(choice is '2'):
    # ask how many grades need to be averaged
    how_many = input('How many grades do you need averaged? ')
    how_many = int(how_many)
    # create a counter fo the while-loop
    count = 0
    # create an empty list to store the grades
    grades = []
    # create an empty list to store the weights
    grade_weight = []
    #create an empty list to store the averaged grade for calculator #2
    ave_grade = []
    # create a while-loop
    while(count < how_many):
        # enter mark, and weight, and convert it to an int
        mark = input('Enter mark which is a percent: ')
        mark = float(mark)
        weight = input('Enter weight which is a percentage <= 100: ')
        weight = int(weight)
        # add the marks and weights to the empty lists for each type
        grades.append(mark)
        grade_weight.append(weight)
        # increase the counter for each loop
        count = count + 1
    # take all the inputed weights and add them togather
    if len(grade_weight) <= 0:
        print('Not enough Information')
    elif len(grade_weight) > 0:
        # sum all of the weights
        total_weight = sum(grade_weight)
        # get the average achieved per grade entered respectively        
        for i in range(len(grades)):
            # get the sum of the average of each grade
            mark_ave = grade_weight[i]*(grades[i]/100)
            ave_grade.append(mark_ave)
        # now sum all the averaged grades and divide by the total weight and
        # multiply by a 100
        final_ave = (sum(ave_grade)/total_weight)*100
        print('Your average now is: ', final_ave, '%', ', on the ',
              total_weight, '% of work that you have completed.')
