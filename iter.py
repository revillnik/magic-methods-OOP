class Frange:
	def __init__(self, start, stop, step):
		self.start = start
		self.stop = stop
		self.step = step
	def __iter__(self):
		self.value = self.start - self.step
		return self
	def __next__(self):
		if self.value + self.step < self.stop:
			self.value += self.step
			return self.value
		else:
			raise StopIteration
a = Frange(0, 3, 0.5)
for i in a:
	print(i)

class Frangestr:
	def __init__(self, st, start, stop, step):
		self.st = st
		self.frd = Frange(start, stop, step)
	def __iter__(self):
		self.value = 0
		return self
	def __next__(self):
		if self.value < self.st:
			self.value += 1	
			return self.frd
		else:
			raise StopIteration

z = Frangestr(3,0,2,0.5)
for i in z:
	for j in i:
		print(j, end = ' ')
	print()