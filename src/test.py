




constant_class = {"hello" : "aaa"}

def constant_method(x): return 2

def test(var_s):
    print(constant_class[var_s])

def calculate(x):
    return x*2


if __name__ == "__main__":
    #test('hello')
    mylist = [1,2,3,4]
    #print(list(map(calculate, mylist)))
    print(list(map(lambda x: constant_method(x), mylist)))