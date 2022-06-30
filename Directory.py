import os

f = r'D: storagetable.csv'
if os.path.exists(f):
    print('file already exists')
else:
    # create a file
    with open(f, 'w') as fp:
        # uncomment if you want empty file
        fp.write('This is first line')