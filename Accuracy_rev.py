import re

def load_txt():
    t = open('Revisi 0.3.txt')
    return t.readlines()

def load_txt_Validasi():
    r = open('Hasil Revisi Validasi.txt')
    return r.readlines()

def load_preprocess(data):
    # Input: -
    # Output: load data dan mengembalikan data yang sudah dipreprocessing


    baca = data
    # text = load_file()
    # print(text)
    a = []
    b = []
    # c = []
    kata = []

    # print("-------------------------------------------------------------------------------------------")
    # print("Baca : ", baca)
    # print("Panjang baca : ", len(baca))
    # print("-------------------------------------------------------------------------------------------")

    for i in range(len(baca)):
        baca[i] = baca[i].rstrip()
        if len(baca[i]) > 1:
            a.append(baca[i])
    # print("Baca a : ", a)
    # print("Panjang a : ", len(a))
    # print("-------------------------------------------------------------------------------------------")

    for i in range(len(a)):
        string = a[i]
        while i < len(a) and a[i][len(a[i]) - 1] == ',':
            i += 1
            string += ' ' + a[i]
        b.append(string)

    # for i in range(len(b)):
    #     # for j in range(len(b[i])):
    #     print("Baca b : ", b[i])
    # print("Panjang b : ", len(b))
    # print("-------------------------------------------------------------------------------------------")
    # for i in range(len(a)):
    # for i in range(len(data)):
    #     print(data[i])
    #
    for i in range(0, len(b)):
        # menghapus karakter "[", "/" dalam b
        string = re.sub('\ |\'|\[|\]', '', b[i])
        # memisahkan setiap b[i] menggunakan ","
        string = string.split(",")
        kata.append(string)
    text = kata

    # for i in range(len(text)):
    #     # for j in range(len(text[i])):
    #     print("Text : ", text[i])
    # print("Panjang text : ", len(text))
    # print("-------------------------------------------------------------------------------------------")
    # for i in range(len(text[i])):
    #     print(text[i])
    # print(text[1][0])

    # mengembalikan text yang sudah dilakukan preprocessing
    return text

read_program = load_preprocess(load_txt())
read_validasi = load_preprocess(load_txt_Validasi())

# print(len(read_program))
# print(len(read_validasi))

word = []
vWord = []
for i in range(0, len(read_program)):
    for j in range(0, len(read_validasi)):
        rp = read_program[i][0]
        rv = read_validasi[j][0]

        if rp == rv :
            checked = 0
            for k in range(0, len(read_program[i])):
                rpc = read_program[i][k]
                if rpc in read_validasi[j]:
                    checked = checked + 1

            if checked == len(read_program[i]):
                word.append(i)
                vWord.append(1)

tesa = []
for i in range(0, len(word)):
    tesa.append([word[i], vWord[i]])

sameWord = len(tesa)
data_validasi = len(read_validasi)
data_program = len(read_program)
precission = (sameWord / data_program) * 100
recall = (sameWord / data_validasi) * 100
Fmeasure = 2*((precission*recall)/(precission+recall))
print(tesa)
print("Precission : ", precission)
print("Recall : ", recall)
print("F measure : ", Fmeasure)