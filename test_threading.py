from threading import Thread
from time import perf_counter,sleep
from files.filename import filenames
from files.list2 import List2
from files.List import List

#Function to read file content and also put arguments in out list that we will use as oldsting in replace function
def readcontent(filename):
    print(f'processing with the file {filename} reading contents')

    with open(filename, 'r') as f:
        content = f.read()
        List.append(content)
        
#Replace function that will be used to replace old function by new one.
def replace(filename, substr, newstr):
    print(f'processing with the file {filename} replacing')
    with open(filename, 'r') as f:
        content = f.read()
        content = content.replace(substr, newstr)
    with open(filename, 'w') as f:
        f.write(content)        

#function used to run add content on 3 element in the same time.
def threading_function_add_content(arg1):
    threads = [Thread(target=readcontent, args=(filename,)) for filename in arg1]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

#function used to run replace content on 3 element in the same time.
def threading_function_replace(arg1, arg2, arg3):
    threads = [Thread(target=replace, args=(filename, oldstring,newstring)) for filename,oldstring,newstring in zip(arg1,arg2,arg3)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

#Execute the main function

def main():
    threading_function_add_content(filenames)
    sleep(1)
    threading_function_replace(filenames,List, List2)


#Main prgram python, also we calculte time of execution of our program
if __name__ == '__main__':
    start_time = perf_counter()
    main()
    end_time = perf_counter()
    print(f'programme exectution was {start_time - end_time:0.2f} seconds to be done')