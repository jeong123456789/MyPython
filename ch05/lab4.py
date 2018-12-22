import random

options =["왼쪽","중앙","오른쪽"]

pos = input("어느 쪽으로 차시겠습니까?[왼쪽, 오른쪽, 중앙]")

com_pos = random.choice(options)

print(com_pos)

if pos == com_pos:
    print("페널티킥을 막아냈습니다.")
else :
    print("골인입니다.")
    
