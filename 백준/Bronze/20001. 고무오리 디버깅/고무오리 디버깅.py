gomu_start = input()
prob = 0

while True:
    gomu = input()

    if gomu == "고무오리 디버깅 끝":
        break
    else:
        if gomu == "문제":
            prob += 1
        
        elif gomu == "고무오리":
            
            if prob == 0:
                prob += 2
            else:
                prob -= 1

if prob == 0:
    print("고무오리야 사랑해") 
else:
    print("힝구")