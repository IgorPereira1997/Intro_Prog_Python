# -*- coding: utf-8 -*-

#open teste.txt
arquivo = open("teste.txt")

# complete text
print(arquivo.read())

# readjust the first line text
print(arquivo.readline())

# brake teste.txt line per line
print(arquivo.readlines())

#create arquive

new_test = open('new_test.txt', "w")
new_test.write("This is my new file")

new_test.close()
arquivo.close()

