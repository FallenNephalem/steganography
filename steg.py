import codecs
mode = input('хотите ввести сообщение в файл или вывезти из файла?(нажмите 1 ,чтобы ввести, или же 2, чтобы вывести)\n')
name_pic = input('Введите название файла с расширением:')


#Скрытие сообщения в файле
if mode == '1':
    encoding_world = 'hash ' + input('Внимание! Cообщение обязательно должно быть на английском языке! \nвведите сообщение:')
    pic = open(name_pic, 'rb')
    img1 = pic.read()
    pic.close()
    pic = open(name_pic, 'ab')
    pic.write(codecs.encode(encoding_world,'cp1251'))
    pic.close()


# извлечение сообщения из картинки
if mode == '2':
    pic = open(name_pic, 'rb')
    img2 = pic.read()
    img2 = str(img2)
    found = img2.rfind('hash ')
    lenth = len(img2)
    print(img2[found+5:-1])
