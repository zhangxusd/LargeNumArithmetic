import random

#Design add for large numbers,
#大数加法

def big_add(x, y):
    (x_digits, y_digits) = convert_to_arr_for_add(x,y)
    #print(x_digits, y_digits)
    result = add_arr(x_digits, y_digits)
    return result
    #print("long_add", result)
    
def convert_to_arr_for_add(x,y):
    x_digits = []
    y_digits = []

    x_len = len(str(x))
    y_len = len(str(y))

    for i in range(x_len):
        x_digits.append(x//10**(x_len - 1 - i))
        x %= 10**(x_len - 1 - i)

    for i in range(y_len):
        y_digits.append(y//10**(y_len - 1 - i))
        y %= 10**(y_len - 1 - i)

    if(len(x_digits) > len(y_digits)):
        for i in range(len(x_digits) - len(y_digits)):
            y_digits.insert(0, 0)
    elif (len(y_digits) > len(x_digits)): 
        for i in range(len(y_digits) - len(x_digits)):
            x_digits.insert(0,0)
    else:
        x_digits.insert(0,0)
        y_digits.insert(0,0)
    
    return(x_digits, y_digits)
        
def add_arr(arr1, arr2):
    if len(arr1) != len(arr2):
        print ("error at converting arrays")
    else:
        length = len(arr1)
        result_arr = []
        for i in range(length-1,-1,-1):
            sum = arr1[i] + arr2[i]
            #print(i, sum)
            if(sum >= 10):
                inc = sum//10
                #print("when sum is bigger than 10 inc is", inc)
                sum %= 10
                #print("when sum is bigger than 10 sum becomes" , sum)
                arr1[i-1] += inc
            result_arr.insert(0,sum)
        
        result = 0
        for i in range(len(result_arr)):
            result += result_arr[i] * (10 ** (len(result_arr)-i-1))

        return result
        
def unit_test_big_add():
    #使用大随机数测试大数加法
    big_x = 2**random.randint(32,40)
    big_y = 2**random.randint(32,50)

    big_sum = big_x + big_y
    big_add_result = big_add(big_x, big_y)

    print("Performing test using", big_x, "and", big_y)
    print("Python built-in add for adding big numbers result", big_sum)
    print("Big_Add adding big numbers result", big_add_result)
    if(big_sum == big_add_result):
        print(big_sum, "Equal to", big_add_result, "Big_Add test Passed")
    else:
        print("Big_Add test Failed")


#Design Multiply for Large Numbers
#大数乘法
def big_multiply(x,y):
    (x_digits, y_digits) = convert_to_arr_for_multiply(x,y)
    #print(x_digits, y_digits)
    result = multiply_arr(x_digits, y_digits)
    return result
    #print (result)

def convert_to_arr_for_multiply(x,y):
    x_digits = []
    y_digits = []

    x_len = len(str(x))
    y_len = len(str(y))

    for i in range(x_len):
        x_digits.append(x//10**(x_len - 1 - i) * 10**(x_len - 1 - i))
        x %= 10**(x_len - 1 - i)

    for i in range(y_len):
        y_digits.append(y//10**(y_len - 1 - i) * 10**(y_len - 1 - i))
        y %= 10**(y_len - 1 - i)
    
    return(x_digits, y_digits)

def multiply_arr(arr1, arr2):
    result = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            tmp = arr1[i] * arr2[j]
            #print(tmp)
            result += tmp
            #print(result)
    return result

def unit_test_big_multiply():
    #使用大随机数测试大数乘法
    big_x = 2**random.randint(32,40)
    big_y = 2**random.randint(32,50)

    big_result = big_x * big_y
    big_mul_result = big_multiply(big_x, big_y)

    print("Performing big multiply test using", big_x, "and", big_y)
    print("Python built-in add for multiplying big numbers result", big_result)
    print("Big_Multiply multiplying big numbers result", big_mul_result)
    if(big_result == big_mul_result):
        print(big_result, "Equal to", big_mul_result, "Big_Mul test Passed")
    else:
        print("Big_Mul test Failed")

unit_test_big_add()
unit_test_big_multiply()


