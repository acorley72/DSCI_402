###FLATTEN###	

def flatten(list):
	if list == []:
		return list
	if type(list[0]) != type([]):
		return [list[0]] + flatten(list[1:])
	return flatten(list[0]) + flatten(list[1:])
	


#----------------------------------------------------------------------------------------------------
####POWERSET#####

def PS(list):
	if list == []:
		return [[]]
	rest = PS(list[1:])
	return map(lambda x: [list[0]] + x, rest) + rest 

#---------------------------------------------------------------------------------------------------
###PERMS###

def add_pos(lst, elem, pos):
	c= list(lst)
	c.insert(pos,elem)
	return c

def il(new_elem,list):
	return map(lambda x: add_pos(list,new_elem,x),range(len(list) + 1))

def all_perms(list):
	if(list) == []:
		return [[]]
	else: 
		rest = all_perms(list[1:])
		first_added = map(lambda x: il(list[0],x),rest)
		return reduce(lambda x,y: x+y, first_added)

#------------------------------------------------------------------------------------------------------


