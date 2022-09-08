if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    names = list(student_marks)
    student_avarage = {}
    for i in names:
        avarage = sum(student_marks[i]) /  len(student_marks[i])
        student_avarage[i] = round(avarage,2)
        
    sorted_avarages = sorted(student_avarage.items(), key=lambda item: item[1])
    print(sorted_avarages)
