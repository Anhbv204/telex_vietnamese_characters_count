def count_vietnamese_characters(input_string):
    vietnamese_characters = ['aw', 'aa', 'dd', 'ee', 'oo', 'ow', 'w']
    count = 0
    i = 0
    while i < len(input_string) - 1:
        if input_string[i:i+2] in vietnamese_characters:
            count += 1
            i += 2
        else:
            i += 1
    return count

if __name__ == "__main__":
    input_string = input("Nhập chuỗi chữ cái latin: ")
    result = count_vietnamese_characters(input_string)
    print("Số lượng chữ cái Tiếng Việt có thể tạo ra là:", result)