import json

file_input = open('data.json', 'rb')
file_output = open('data_new.json', 'wb')

data = file_input.read()

decode = data.decode('unicode_escape').encode('utf8')
# file_output.write(decode)
a = decode.decode('utf8')
decode = str(decode)
(type(decode))


with open('data_new_with.json', 'w') as save:
    save.writelines(a) 
    