from threading import Thread
from time import perf_counter,sleep


def readcontent(filename):
    print(f'processing with the file {filename} reading contents')

    with open(filename, 'r') as f:
        content = f.read()
        List.append(content)
        


def replace(filename, substr, newstr):
    print(f'processing with the file {filename} replacing')
    with open(filename, 'r') as f:
        content = f.read()
        content = content.replace(substr, newstr)
    with open(filename, 'w') as f:
        f.write(content)        

def threading_function_add_content(arg1):
    threads = [Thread(target=readcontent, args=(filename,)) for filename in arg1]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

def threading_function_replace(arg1, arg2, arg3):
    threads = [Thread(target=replace, args=(filename, oldstring,newstring)) for filename,oldstring,newstring in zip(arg1,arg2,arg3)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()




start_time = perf_counter()

filenames = [
        'Desktop/test/test1.txt',
        'Desktop/test/test2.txt',
        'Desktop/test/test3.txt',
]
List = []
List2 = ['rambo','kiko','Schweine']
threading_function_add_content(filenames)
sleep(1)

threading_function_replace(filenames,List, List2)


end_time = perf_counter()

print(f'programme exectution was {start_time - end_time:0.2f} seconds to be done')