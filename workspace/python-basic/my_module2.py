PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)

def sum(a, b):
    return a+b

# print(PI)
# a = Math()
# print(a.solv(2))
# print(sum(PI, 4.4))  

print(__name__)
if __name__ == "__main__": # python my_moduel2.py로 실행한 경우 True
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI , 4.4))