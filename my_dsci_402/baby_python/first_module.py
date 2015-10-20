def add_2(x,y, mult_by = 1):
	return mult_by * (x + y) 

def optional_args_test(a,b,*rest):
	print("A: " + str(a))
	print("B: " + str(b))
	print("Rest: " + str(rest))

	
def my_filter_1(criteria_f, elements):
	return [x for x in elements if criteria_f(x)] 
	

def my_filter_2(criteria_f, elements): 
	#takes a list and a single elements then combines them if the criteria_f is true on singe element
	combiner = lambda elts, elt: elts + [elt] if criteria_f(elt) else elts
	return reduce(combiner, [[]] + elements) 

#Recursively-defined sum range 	
def sum_range(begin,end):
	if begin == end:
		return begin
	else:
		return sum_range(begin, end - 1) + end
		
def fac(n):
	if n == 0:
		return 1
	else:
		fac(n-1) * n
		
#Fibonacci term finder (slow)
# def fib(first, second, n):
	# if n == 1:
		# return first 
	# elif n == 2:
		# return second
	# else:
		# return fib(first,second, n - 1) + fib(first,second, n - 2)

#Fibonacci term finder (dynamic programming)		
def fib(first, second, n, cache = {}):
	if n == 1:
		return first 
	if n == 2:
		return second
	if not (cache.has_key(n)):
		cache[n] = fib(first,second, n - 1, cache) + fib(first,second, n - 2, cache)
	return cache[n]
		
#Cartesian Product for two lists using for loop
# def cart_prod(A,B):
	# pairs = []
	# for i in A:
		# for j in B:
			# pairs.append((i,j))
	# return pairs 
		
#Cartesian Product for three lists using fro loop
# def cart_prod(A,B,C):
	# pairs = []
	# for i in A:
		# for j in B:
			# for k in C:
			# pairs.append((i,j,k))
	# return pairs 
	
#Cartesian Product for any number of lists using fro loop
def cart_prod(*sets):
	if len(sets) == 0:
		return []
	if len(sets) == 1:
		return map(lambda x: [x], sets[0]) 
	rest = cart_prod(*sets[1:])
	add_front = lambda x: map(lambda y: [x] + y, rest)
	return reduce(lambda x, y: x + y, map(add_front, sets[0]))

#Get all combinations from items, taken k at a time.
def all_combs(items,k):
	if k == len(items):
		return [items]
	if k == 1:
		return map(lambda x: [x], items)
	rest = all_combs(items[1:], k - 1) 
	return map(lambda x: [items[0]] + x, rest) + all_combs(items[1:],k)
	