
try:
    with open('myfile.txt') as fh:
        file_data = fh.read()
        
    print(file_data)
    
except Exception as err:
    print('some other error: ', str(err))
