
# class A():
#     bar={
#         'os':'os',
#         'osb':'system'
#     }
# a=A()
# print(getattr(a,'bar'))
# print(getattr(a,'bar')['osb'])

#getattr(object, name[, default])
#https://www.runoob.com/python/python-func-getattr.html

# for i in range(1,10):
#     for j in range(1,i+1):
#         if i==j:
#             print("{}*{}={}".format(j,i,i*j))
#         else:
#             print("{}*{}={}".format(j,i,i*j),end=" ")

# out=[]
# for i in range(10):
#     out.append(i)

# out= [f"{number}+sd" for number in range(10)]
# print(out)

# num=[[f"{j}*{i}={i*j}" for i in range(1,10)] for j in range(1,10)]

# a=10
# print(f"{a.__class__}+{a.__class__.__class__}+{a.__class__.__class__.__class__}")

# print(type("234"))
Word=type('Word',(str,),{
    'mutated': 1,
    'startswith': lambda self, x: False,
    '__eq__': lambda self, x: self.mutate()
    and self.mutated < 0
    and str(self) == x,
    'mutate': lambda self: {setattr(self, 'mutated', self.mutated - 1)},
    '__hash__': lambda self: hash(str(self)),
})

# print((str))
# yly=Word('__yly__')
# print(yly)
# print(type(yly))
# print(yly=='__yly__') # False
# #后面都是True，嘶，什么意思
# print(yly=='__yly__')
# print(yly=='__yly__')
# print(yly=='__yly__')

# print(yly.startswith('__')) #False
# class A():
#     pass
# class B(A):
#     pass
# print(isinstance(B(),A))
# print(type(A()),A,A())
# print(B,B())
# print(type(B()))
# print(type(B())==B)
# print(type(B())==A)



# class B(str):
#     pass
# class A(int):
#     pass
# class C():
#     pass
# wd=B('1231')
# print(wd)
# print(type(wd))
# print(type(A(1)))
# print(C())
#lambda函数，即匿名函数
# def x(a):
# 	print(a+10)
# x(5)

# s=lambda a:print(a+10)
# s(6)

# s=lambda self,x: x==2
# # a,b=1,2
# # print(s(x==2)) #true

# class myclass:
#     def __eq__(self,x):
#         return x==2
#     pass
# obj=myclass()
# print(obj==2) #一般只接受两个参数

# class myclass:
#     def __eq__(self,x,y=2):
#         return x==y
#     pass
# obj=myclass()
# print(obj==2)

def xxx(a):
    return "hello"

fu=type(type(1))
x=fu('Yly',(str,),{
    'sd':1
})
# print(dir(x('__globals__')))

#y=getattr(pow,x('__globals__'))
# print(x('__globals__'))
# getattr(pow,x('__globals__'))
# print(Word('__globals__'))
# getattr(pow,xxx.__globals__)

# def xx():
#     return "hello"
# print(dir(xx))
# print(dir(xx()))
print(dir(x.__class__))
