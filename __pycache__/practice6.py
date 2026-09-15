def NA_list():
    names = []
    ages = []
    while True:
        name = input("이름을 입력하세요(종료할려면 '끝' 입력):")
        age = input("나이를 입력하세요:")
        if name == '끝':
           break
        names.append(name)
        ages.append(age)

    return(names,ages)
result = NA_list()
print(result)