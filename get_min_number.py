#coding=utf8

# describe
'获取输入数字组成的最小数'
'example: 输入 3个0，1个1， 2个9， 3个2'
'组成的最小数为： 100022299'

def main():
    input_number_list = [3, 1, 3, 0, 0, 0, 0, 0, 0, 2]  #输入 3个0，1个1， 2个9， 3个2
    result_list = []
    for i in range(1, len(input_number_list)):
        if input_number_list[i] != 0:
            result_list.append(i)
            input_number_list[i] -= 1
            break
    
    for i in range(0, len(input_number_list)):
        if input_number_list[i] != 0:
            result_list.extend([i] * input_number_list[i])
    print(result_list)

if __name__ == "__main__":
    main()