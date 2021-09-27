scores = []  # 3명의 학생의 3과목 점수 3*3
titles = ["국어", "영어", "수학"]


for stu_idx in range(1, 4):
    indiv_score = []
    print(f"<< {stu_idx}번 학생:>>")
    for score_idx in range(0, 3):
        indiv_score.append(int(input(f"{titles[score_idx]} 과목: ")))
    scores.append(indiv_score)

stu_idx = 0
for indiv_score in scores:
    stu_idx += 1
    print(f" << {stu_idx}번 학생 >>")
    class_idx = 0
    for score in indiv_score:
        print(f"{titles[class_idx]} 점수: ", score)
        class_idx += 1
    avg = sum(indiv_score) / len(indiv_score)
    print("평균: ", avg)

