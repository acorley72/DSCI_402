from first_module import *
import first_module 
import first_module as fm 

print(add_2(8,10))
print(first_module.add_2(5,6))
print(fm.add_2(5,6))
print(add_2(10, 15, mult_by = 3))
print(add_2(10, 15, 3))
optional_args_test(1,2,3,4,5)
data = [1, 3]
print(add_2(*data))

def trace(x,y):
	print((x,y))
	return x+ y 

nums = range(-10,11)
print(my_filter_1(lambda x: x >0, nums))
# print(reduce(trace,range(1,11)))
print("Hello")
print(my_filter_2(lambda x: x >0, nums))

print("Test sum range:------")
print(sum_range(1,10)) 

# print("Test Fib. Solver------")
# print(fib(1,1,5))
# print(fib(4,9,8))
# print(fib(1,3,100))

print("Test Cartesion Product---")
print(cart_prod([1,2],[3,4],[5,6],[7,8]))

print("Test all combs---")
print(all_combs([1,2,3,4,5,6],2))