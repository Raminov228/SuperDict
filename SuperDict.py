import json

with open("test.json", "r") as read_file:
    data = json.load(read_file)

class SuperDict():
	"""Superdict"""
	
	def __init__(self, dict_data):
		for key in dict_data:
			if type(dict_data[key]) == type(dict_data): 
				object.__setattr__(self, key, SuperDict(dict_data[key]))
			elif type(dict_data[key]) == type([]):
				object.__setattr__(self, key, self.parse(dict_data[key]))
			else:
				object.__setattr__(self, key, dict_data[key])


	def parse(self, lst):
		for i in range(len(lst)):
			if type(lst[i]) == type(dict()):
				lst[i] = SuperDict(lst[i])
			elif type(lst[i]) == type([]):
				lst[i] = self.parse(lst[i])
		
		return lst


	def __getitem__(self, key):
            return object.__getattribute__(self, key)


chel = SuperDict(data)
print(chel.hobbies)
