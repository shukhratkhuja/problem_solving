if __name__ == '__main__':
    
    records = []
    
    second_min_score = 100
    min_score = 100
        
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
        if score < min_score:
            second_min_score = min_score
            min_score = score
        elif score < second_min_score and score != min_score:
            second_min_score = score
        
    snames = [student[0] for student in records if second_min_score == student[1]]
    
    for name in sorted(snames):
        print(name)
    

            
            