dict1 =  {'Student1':
             {'name': 'Shamim Ahmed',
              'Section': 'DB',
               'ID':'201902067'
                 },
          'Student2':
              {'name':'Shamim Ahmed',
               'Section': 'DB',
               'ID': '201902067'
             },
         'Student3':
            {'name': 'SK Nahid',
             'Section': 'DA',
             'ID':'201902073'
             },
        'Student4':
              {'name': 'Hamad',
              'Section': 'DC',
              'ID':'201902046'
             },
        }
temp = []
res = dict()
for key, val in dict1.items():
    if val not in temp:
        temp.append(val)
        res[key] = val

print(res)