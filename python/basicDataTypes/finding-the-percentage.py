if __name__ == '__main__':
    student_marks = {}

    for _ in range(int(raw_input())):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name.strip()] = scores

    marks = student_marks[raw_input().strip()]
    print format(sum(marks) / len(marks), '.2f')

