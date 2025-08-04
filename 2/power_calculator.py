def power_calculator():
    try:
        n_i = input("숫자를 입력하세요:")
        n = float(n_i)
    except ValueError:
        print("Invaild number input")
        return
    
    try:
        e_i = input("지수를 입력하세요:")
        e = int(e_i)
        if e < 0:
            print("Invaild exponet input")
            return
    except ValueError:
        print("Invaild exponet input")
        return
    
    result = 1
    for i in range(e):
        result *= n


    print("Result =",result)

if __name__ == "__main__":
    power_calculator()