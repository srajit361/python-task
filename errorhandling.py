try:
    file=open('sampl.txt','r')
    reading_mode=file.read()
    print(reading_mode)
    file.close()
except FileNotFoundError:
    print('Error: The file "sample.txt" was not found')
finally:
    print()
