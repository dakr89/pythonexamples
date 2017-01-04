#  this is about how to do multiple  works in parallel

#  with out multithreading
# import time

# class multi_threading:
# 	def test1(self,numbers):
# 		for x in numbers:
# 			time.sleep(0.2)
# 			print('square of the number: ',x*x)

# 	def test2(self,numbers):
# 		for x in numbers:
# 			time.sleep(0.2)
# 			print('cube of the number: ',x*x*x)

	
# a = [1,2,3,4,5]	
# t = time.time()
# ml = multi_threading()
# ml.test1(a)
# ml.test2(a)

# print('took time: ',time.time()-t)

#  with threading concept
import time
import threading

class multi_threading:
	def test1(self,numbers):
		for x in numbers:
			time.sleep(0.2)
			print('square of the number: ',x*x)

	def test2(self,numbers):
		for x in numbers:
			time.sleep(0.2)
			print('cube of the number: ',x*x*x)

	
a = [1,2,3,4,5]	
t = time.time()
ml = multi_threading()
th1 = threading.Thread(target=ml.test1,args=(a,))
th2 = threading.Thread(target=ml.test2,args=(a,))
th1.start()
th2.start()
th1.join()
th2.join()
print('took time: ',time.time()-t)