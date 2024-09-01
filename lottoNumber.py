import random

# 로또 번호 생성
lotto_num=random.sample(range(1,46),7)
print("정답", lotto_num)

# 사용자 로또 입력 받기
print("로또 번호 6개를 입력하세요 (1~45): ")
user_input = list(map(int, input().split()))
print("입력된 번호: ", user_input)
