# Workong with files
# read files

# f = open('file1.txt')

# print(f.tell())  # find cursor position
# print(f.read())
# print(f.tell())
# print(f.seek(0)) # change cursor position
# print(f.read())

# print(f.readline(), end='')
# print(f.readline())
# print(f.readline())

# lines = f.readlines()
# print(lines)
# print(len(lines))
# for line in lines:
#     print(line)

# print(f.name)
# print(f.closed)
# f.close()
# print(f.closed)

# f = open(r"F:\Al-Nafi\file1.txt")
# print(f.read())
# for line in f:
#     print(line)
# f.close()

# with block or context manager

# with open('file1.txt') as f:  # dont need to close
#     data = f.read ()
#     print(data)
# print(f.closed)

# read an write files (w, a, r+)

# with open('file1.txt','w') as f:  # over_write existing file
#     f.write('hello dear')

# with open('file2.txt','w') as f:  # create new file
#     f.write('hello dear')

# with open('file2.txt','a') as f:  # add in existing file
#     f.write('\nplease add this line')

# with open('file1.txt','r+') as f:  # read and write the file
#     f.write('please do this')

# with open('file1.txt','r+') as f:  
#     f.seek(len(f.read()))
#     f.write('\nplease add this line in last')

# with open('file2.txt','r') as rf:
#     with open('file1.txt','w') as wf:
#         wf.write(rf.read())

# with open('file1.txt','r') as rf:
#     with open('file2.txt','a') as wf:
#         for line in rf.readlines():
#             name,salary = line.split(',')
#             wf.write(f'{name}\'s salary is {salary}' )

# working with CSV files

# from csv import reader
# with open('file1.csv','r') as f:
#     csv_reader = reader(f)
#     # print(csv_reader)
#     for row in csv_reader:
#         print(row)

# from csv import DictReader
# with open('file1.csv','r') as f:
#     csv_reader = DictReader(f,delimiter = '|')
#     for row in csv_reader:
#         print(row['email'])

# from csv import writer
# with open('file2.csv','w',newline='') as f:
#     csv_writer = writer(f)
#     # csv_writer.writerow(['name','country'])
#     # csv_writer.writerow(['zahid','pakistan'])
#     # csv_writer.writerow(['rahol','india'])
#     # csv_writer.writerow(['john','england'])
#     csv_writer.writerows([['name','country'],['zahid','pakistan'],['john','england']])

# from csv import DictWriter
# with open('file3.csv','w') as f:
#     csv_writer = DictWriter(f,fieldnames=['first_name','last_name','age'])
#     csv_writer.writeheader()
#     # csv_writer.writerow({
#         # 'first_name' : 'zahid',
#         # 'last_name' : 'riaz',
#         # 'age' : 31
#     # })
#     # csv_writer.writerow({
#         # 'first_name' : 'Amjad',
#         # 'last_name' : 'hussain',
#         # 'age' : 32
#     # })

#     csv_writer.writerows([
#         {'first_name' : 'zahid','last_name' : 'riaz','age' : 31},
#         {'first_name' : 'Amjad','last_name' : 'hussain','age' : 32}
#     ])

# from csv import DictWriter, DictReader
# with open('file3.csv') as rf:
#     with open('file4.csv','w') as wf:
#         csv_reader = DictReader(rf)
#         csv_writer = DictWriter(wf,fieldnames=['first_name','last_name','age'])
#         csv_writer.writeheader()
#         for row in csv_reader:
#             fname,lname,age = row['first_name'],row['last_name'],row['age']
#             csv_writer.writerow({
#                 'first_name':fname.upper(),
#                 'last_name':lname.upper(),
#                 'age':age
#             })
