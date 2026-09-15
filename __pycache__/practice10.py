def 계산(a,b):
    if (a+b) <10:
        return "기준 미만입니다"
    else:
        return "기준 이상입니다"
num1=int(input("첫 번째 숫자를 입력하세요"))
num2=int(input("두 번째 숫자를 입력하세요"))
result = 계산(num1,num2)
print(result)