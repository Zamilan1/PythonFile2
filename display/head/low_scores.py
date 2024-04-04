def main():
    scores = get_scores()
    total = get_total(scores)
    lowest = min(scores)
    total = total - lowest
    average = total / len(scores)
    
    print("Lowest score:", lowest)
    print("Total Score: ", total)
    print("Average Score: ", average)

def get_scores():  
    num_players = int(input("Enter the number of players: "))
    scores  = []
    for i in range(num_players):
        score = int(input("Enter score for player " + str(i+1) + ": "))
        scores.append(score)
    return scores

def get_total(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum

if __name__ == '__main__':
    main()