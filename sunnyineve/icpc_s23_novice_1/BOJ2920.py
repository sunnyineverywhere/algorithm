melodies = list(map(int, input().split()))

ascending_flag = True
descending_flag = True

for i in range(len(melodies)):
    if i + 1 != melodies[i]:
        ascending_flag = False
    if i + 1 != melodies[len(melodies) - 1 - i]:
        descending_flag = False

if ascending_flag:
    print("ascending")
elif descending_flag:
    print("descending")
else:
    print("mixed")
