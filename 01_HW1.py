# 과제 1 - 맛집 고르기
#
# 구현 내용
# •처음 파이썬 파일을 실행 시키면, 한식, 중식, 일식 중 한 가지를 고르라는 내용이 나옵니다.
# •그 중에서 한 가지를 고르면 식당 이름을 하나 임의로 추천해 줍니다.
#
# 힌트
# •리스트를 여러 개 사용하고 사용자의 입력을 받아야 합니다.

# 1) 음식 고르기
choice_1 = input("당신이 좋아하는 음식은 무엇입니까? (한식/중식/일식)")

# 2) 각 나라별 음식지정
import random
korean_food = ['삼겹살', '불고기', '김밥', '비빔밥']
chinese_food = ['짜장면', '볶음밥', '탕수육', '팔보채', '샥스핀', '깐쇼새우']
japanese_food = ['우동', '가츠동', '규동', '와규', '스시']

# 3) 함수 생성
if choice_1 == "한식":
    print(random.choice(korean_food))
elif choice_1 == "중식" :
    print(random.choice(chinese_food))
elif choice_1 == "일식" :
    print(random.choice(japanese_food))
else:
    print("해당되지 않습니다. 다시 실행해주세요.")
