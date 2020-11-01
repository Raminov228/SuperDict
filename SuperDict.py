#---------------------------------#
# Аминов Ренат, СуперСловарь      #
#                                 #
# 2ое Ноября 2020                 #
#                                 #
# v 0.0.1                         #
#---------------------------------#

''' Вот как выглядит test.json
{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
'''
import json


'''tip: название вдохновлено группой СУПЕРКОЗЛЫ'''
class SuperDict():
	def __init__(self, dict_data):
		''' 
		Создаем супер словарь
		Для этого надо добавить аттрибут для каждого элемента словаря

		@ in  : dict
		@ out : SuperDict object
		'''
		for key in dict_data:
			if type(dict_data[key]) == type(dict_data):
				#если нам попался словарь, то его надо превратить в SuperDict 
				object.__setattr__(self, key, SuperDict(dict_data[key]))
			
			elif type(dict_data[key]) == type([]):
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
			if type(elem) == type(elem):
				parsed_lst.append(SuperDict(elem))

			# если попался список, то парсим его 
			elif type(elem) == type(elem):
				parsed_lst.append(self.parse(elem))

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


with open("test.json", "r") as read_file:
    data = json.load(read_file)

person = SuperDict(data)

#можно обращаться по разному
print(person.hobbies)
print(person['hobbies'])

#можно делать неограниченное количество вложений
print(person.children[1].firstName)
print(person['children'][1]['firstName'])



'''
TODO:

- __str__()
- написать тесты

'''