if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    for _ in range(n):
        
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for name, scores in student_marks.items():
        if name == query_name:
            print("%.2f"%(sum(scores)/len(scores)))

"""
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
"""