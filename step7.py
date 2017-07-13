#-*- coding: utf-8 -*-

# Welcome 이라고 출력
print("Welcome!")

# g라는 변수를 입력
g = input("Guess the number: ")

# int(정수) g라는 변수를 guess로 선언
guess = int(g)

# guess의 값이 만약에 5이면 밑의 구문을 출력
if guess == 5:
    print("You win!")
# 5가 아니면 밑의 구문을 출력
else: 
    print("You lose!")

# Game Over를 출력
print("Game over!")
