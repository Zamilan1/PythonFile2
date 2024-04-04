def main():
    average = 0.0
    score1 = 0.0
    score2 = 0.0
    score3 = 0.0
    score4 = 0.0
    score5 = 0.0
    score1 = float(input('Enter score1:'))
    score2 = float(input('Enter score2:'))
    score3 = float(input('Enter score3:'))
    score4 = float(input('Enter score4:'))
    score5 = float(input('Enter score5'))
    average = calc_average(score1,score2,score3,score4,score5)
    print('Score\t\tNumeric Grade\tLetter Grade')
    print('------------------------------------')
    print('score1:\t',score1,  '\t\t',determine_grade(score1))
    print('score2:\t',score2,  '\t\t',determine_grade(score2))
    print('score3:\t',score3,  '\t\t',determine_grade(score3))
    print('score4:\t',score4,  '\t\t',determine_grade(score4))
    print('score5:\t',score5,  '\t\t',determine_grade(score5))
    print('Average score:',average, '\t\t', determine_grade(average))

def calc_average(s1,s2,s3,s4,s5):
    return(s1+s2+s3+s4+s5)/5.0

def determine_grade(score):
    if score >=90:
       return 'A'
    elif score >=80:
        return 'B'
    elif score >=70:
        return 'C'
    elif score >=60:
        return 'D'
    else:
        return 'F'

main()