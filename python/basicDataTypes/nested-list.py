min_score = None
second_score = None

names = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())

    if min_score is None:
        min_score = second_score = score

    if score < min_score:
        min_score = score

    if score > min_score and (score < second_score or second_score == min_score):
        second_score = score
        names = []

    if score == second_score:
        names.append(name)

for name in sorted(names):
    print name

