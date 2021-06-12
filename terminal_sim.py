import os


def execute(cmd):
    
    try:
        out = os.system(cmd).readlines()
        for o in out:
            print(o)
            
    
    except:
        print("Something went wrong")