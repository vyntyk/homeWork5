# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE# in
# Enter the name of the file with the text:# 'text_words.txt'
# Enter the file name to record:# 'text_code_words.txt'
# Enter the name of the file to decode:# 'text_code_words.txt'
# # out# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ#
# out in file 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ  'text_code_words.txt' 5a29v4s3D3d2F4g2O3i2a1 1v2b2w2P3u2T1Y1y2W2Q

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


path = 'text_code_words.txt'
RLE_file = open(path, 'r', encoding="utf-8")
res_RLE = RLE_file.read()
print('Первоначальные данные: ' + res_RLE)
RLE_file.close()

encoded = rle_encode(res_RLE)
print('Данные после обработки: ' + encoded)


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


path = 'text_words.txt'
RLE_file = open(path, 'r', encoding="utf-8")
res_RLE1 = RLE_file.read()
print('Первоначальные данные: ' + res_RLE1)
RLE_file.close()

decoded = rle_decode(res_RLE1)
print('Восстановленные данные: ' + decoded)

with open('text_code_words.txt', 'a+', encoding="utf-8") as file:
    file.write('\n' + 'Первоначальные данные: ' + encoded)

with open('text_words.txt', 'a+', encoding="utf-8") as file:
    file.write('\n' + 'Восстановленные данные: ' + decoded)
