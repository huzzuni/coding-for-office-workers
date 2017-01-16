# 과제 2 - 회사 조직도 만들기
#
# 구현 내용
# •사람 클래스를 하나 만듭니다. 사람의 기본 요소는 이름, 나이, 성별로 합시다.
# •직장 동료 클래스를 사람 클래스를 이용해서 만듭시다. 사람 기본 요소 외 별도의 추가 사항은 직급입니다.
#
# 힌트
# •클래스와 상속을 활용합니다.
# •사람의 기본 요소인 이름, 나이, 성별은 각각 새로운 사람을 만들 때, 입력을 받을 수 있도록 합시다.
# •직장 동료의 기본 직급은 "대리"로 지정합니다.
# •(고급) 사람 클래스에서 새로운 사람을 만들 때 입력은 그대로 유지하면서, 직급도 처음 만들어질 때 입력하도록 변경을 도전해봅시다.

# 1) 사람 클래스 만들기

class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

people1 = People("한현수","31","남")
people2 = People("오바마","56","남")
people3 = People("메릴 스트립","67","여")

print(people1.name)
print(people1.age)
print(people1.gender)


# 2) 직장동료 클래스 추가하기
class Organization(People):
    position = "대리"

position1 = Organization("한현수","31","남")
position2 = Organization("오바마","56","남")
position3 = Organization("메릴 스트립","67","여")


print(position2.name)
print(position2.age)
print(position2.gender)
print(position2.position)
