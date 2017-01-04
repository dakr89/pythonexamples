
#  if you define variable as global you can access  outside the function also

val = 10
print('val from outside', val)
def fun1():
	global val
	val = 12

	print("from one ",val)

def fun2():
	val = 20
	print("from two ",val)

fun1()
fun2()