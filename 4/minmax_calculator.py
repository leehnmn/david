def main():
    try:
        num_input = input("숫자(들)를(을) 입력하시오: ") #숫자입력부분
        list_nums = num_input.split() #숫자입력을 해주며 이를 리스트형태로 꿔줌
        numbers = [float(t) for t in list_nums] #for 이용으로 문자형인 리스트 숫자들을 하나씩 실수형으로 바꿈
        if not list_nums:
            raise ValueError
    except ValueError:
        print("Invalid input.")
        return

    minimum = numbers[0]  #만들어진 리스트에서 0번째를 최소 최대로 넣고 초기화, 0을기준으로 설정함.
    maximum = numbers[0]

    for num in numbers[1:]:  #리스트 1번부터 하나씩 리스트에서 꺼내고 반복
        if num <= minimum:
            minimum = num
        if num >= maximum:
            maximum = num

    print("Min:", minimum)
    print("Max:", maximum)

if __name__ == "__main__":
    main()