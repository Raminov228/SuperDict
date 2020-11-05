#---------------------------------#
# Аминов Ренат, СуперСловарь      #
#                                 #
# 5ое Ноября 2020                 #
#                                 #
# v 0.0.3                         #
#---------------------------------#
import json


class SuperDict():
	def __init__(self, dict_data):
		''' 
		Создаем супер словарь
		Для этого надо добавить аттрибут для каждого элемента словаря

		@ in  : dict
		@ out : SuperDict object
		'''
		self.data = dict_data

		for key in dict_data:
			if isinstance(dict_data[key], type(dict_data)):
				#если нам попался словарь, то его надо превратить в SuperDict 
				object.__setattr__(self, key, SuperDict(dict_data[key]))
				
			elif isinstance(dict_data[key], type([])):
				# если нам попался список, то надо его "запарсить"
				object.__setattr__(self, key, self.parse_list(dict_data[key]))
			
			else:
				# создаем аттрибут
				object.__setattr__(self, key, dict_data[key])		
		
	def parse_list(self, lst):
		'''
		Здесь парсим список 
			
		@ in  : list
		@ out : list
		'''
		parsed_lst = []
		
		for elem in lst:	
			# если попался словарь, то делаем из него SuperDict()
			if isinstance(elem, type(dict())):
				parsed_lst.append(SuperDict(elem))

			# если попался список, то парсим его 
			elif isinstance(elem, type([])):
				parsed_lst.append(self.parse_list(elem))

			#иначе оставляем без изменений
			else:
				parsed_lst.append(elem)

		return parsed_lst

	def __getitem__(self, key):
		'''
		Здесь обрабатываем обращение как к словарю 
			
		@ in  : key
		@ out : dict[key]
		'''
		return object.__getattribute__(self, key)

	def __str__(self):
		return str(self.data)

	def clear(self):
		self.data.clear()
		self = SuperDict(self.data)

	def copy(self):
		return SuperDict(self.data.copy())

	def get(self, key, deafult=None):
		return self.data.get(key, deafult)

	def items(self):
		return self.data.items()

	def keys(self):
		return self.data.keys()
	
	def update(self, other):
		self.data.update(other)
		self = SuperDict(self.data)

	def pop(self, key, deafult=None):
		out = self.data.pop(key, deafult)
		self = SuperDict(self.data)
		return out

	def values():
		return self.data.values()


def make_super_dict(name_of_json):
	'''
	Название json -> словарь -> SuperDict

	@ in  : name_of_json
	@ out : SuperDict object
	'''
	with open(name_of_json, "r") as read_file:
		data = json.load(read_file)

	return SuperDict(data)