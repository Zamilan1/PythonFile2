def get_input():
    """Gets user input for 5 scores and returns them as a list."""
    scores = []
    for i in range(1, 6):
        score = float(input(f'Enter score{i}: '))
        scores.append(score)
    return scores

def calculate_average(scores):
    """Calculates the average score of the given list of scores."""
    return sum(scores) / len(scores)

def determine_grade(score):
    """Determines the letter grade based on the given score."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def print_grades(scores, letter_grades):
    """Prints the scores, numeric grades, and letter grades in a formatted table."""
    print('Score\t\tNumeric Grade\tLetter Grade')
    print('------------------------------------')
    for score, letter_grade in zip(scores, letter_grades):
        print(f'{score:10.2f}\t{score:12.2f}\t{letter_grade}')

def main():
    """Gets user input, calculates the average score, determines the letter grades, and prints them in a formatted table."""
    scores = get_input()
    average = calculate_average(scores)
    letter_grades = [determine_grade(score) for score in scores + [average]]
    print_grades(scores, letter_grades[:-1])
    print(f'Average score: {average:.2f}\t{letter_grades[-1]}')

if __name__ == '__main__':
    main()