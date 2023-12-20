#important programs 
# global_var=4
# def local_func():
#     global_var=3
#     print(global_var)
# local_func()
# print(global_var)

var1=10
def func_1():
    var1=3
    print(var1)
    def func_2():
        nonlocal var1
        var1=4
        print(var1)
    func_2()
    print(var1)
func_1()
print(var1)