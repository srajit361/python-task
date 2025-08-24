file=open('output.txt','w')
writing_mode=file.write(input('enter text to write the file : ' + "\n"))
print("Data succesfully written to output.txt")
file.close()

file=open('output.txt','a')
appending_mode=file.write(input('Enter additional text to append  : ' + "\n"))
print("data successfully appended"  )
file.close()

file=open('output.txt','r')
print("\nfinal content of output.txt" )
reading_mode=file.read()
print(reading_mode)
file.close()

