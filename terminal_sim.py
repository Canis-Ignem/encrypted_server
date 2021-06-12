import os


def execute(cmd):
    
    try:
        out = os.popen(cmd).readlines()
        return out
            
    
    except:
        print("Something went wrong")
        
        
print(execute("echo hello"))