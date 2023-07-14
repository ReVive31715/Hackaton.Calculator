print("노광민의 고교 내신 계산기 입니다.")
print("1. 해당 학기 내신 계산")
print("2. 고교 총 평균 내신 계산")
print("3. 종료")

while True:
    choice = input(" \n 원하는 작업을 선택하세요. (1-3): ")
    if choice == "1":
        s1 = int(input("과목수를 입력해 주세요.:"))
        times = []
        for i in range(s1):
            print("과목별 단위수를 차례대로 입력해 주세요.")
            a = int(input())
            times.append(a)

        grade = []
        for i in range(s1):
            print("과목별 내신등급을 ***단위수 입력한 순서*** 대로 입력해 주세요.")
            b = int(input())
            grade.append(b)
        (grade)

        s3 = 0
        for i in range(s1):
            ( times[i] * grade[i])
            s3 = s3 + (times[i] * grade[i])
        (s3)

        s4 = 0 
        for i in range(s1):
            (times[i])
            s4 = s4 + (times[i])
        (s4)
        print ("당신의 해당 학기 평균 내신등급입니다.\n \n" , s3 / s4)

    elif choice == "2":
        k1 = list(map(float, input("당신의 학기별 내신을 차례대로 입력해 주세요.(원하는 갯수 만큼):").split()))
        semester = []
        s5 = 0
        (k1)
        for i in range(len(k1)):
            s5 = s5 + k1[i]
            (s5)
        print("당신의 고교 평균 내신등급입니다.\n \n", s5 / len(k1))

    elif choice == "3":
        print("계산기를 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 선택해 주세요.")