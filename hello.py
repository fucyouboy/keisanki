print("Hello world!")
print("1+1'=", 2)
def submit(name):
    if name = 0 or 1 :
        return 1 
    else:
        return submit(name-1) + submit(name-2)

submit(10)
