import os

headername = ['num1','num2','operation','finalresult']

f = r'D: storagetable.csv'
if os.path.exists(f):
    print('file already exists')
else:
    # create a file
    with open(f, 'w') as fp:
        fp.write(headername)