def palindrom(string):
    if string == string[::-1]:
        print('True')
    else:
        print('False')

palindrom('шалаш')