a = "This is a test sentence                 where           i-will-put  __aLOTof   different!     type of TEXT"

print(a.split())

a = 3
b = 5

def modify_a():
    global a,b
    a = 5
    b = 9
    print(a)


modify_a()
print (a, b)