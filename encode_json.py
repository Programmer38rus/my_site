
with open('data.json', 'rb') as file_input:

    data = file_input.read()

decode = data.decode('unicode_escape').encode('utf8')


with open('data_utf8.json', 'wb') as save:
   save.write(decode)

