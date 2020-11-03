from SuperDict import make_super_dict


person = make_super_dict('test.json')

#можно обращаться по разному
print(person.hobbies)
print(person['hobbies'])

#можно делать неограниченное количество вложений
print(person.children[1].firstName)
print(person['children'][1]['firstName'])

#можно вывести все сразу (просто словарь)
print(person)

tbl = make_super_dict('table.json')
print(tbl.table[0].spare.name)
