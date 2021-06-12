import os


def execute(cmd):
    
    try:
        out = os.system(cmd).readlines()
        return out
            
    
    except:
        print("Something went wrong")