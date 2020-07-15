def listtGenerator():
    lst1 = []
    for i in range(10,100):
        lst1.append(i)
        i += 1
        return lst1
def Generate_table(number):
    n = 1
    lst = []
    for i in range(10):
        i = n*number
        n = n+1
        lst.append(i)
    return lst

def WrongTable(table):
    import random
    rand = random.choice(lst)
    for item in table:
        if item > 10:
            item = rand
        else:
            pass
    return table
if __name__ == '__main__':
  import random
  table_of_no = int(input("Please enter the number you want to get the table\n"))
  table = Generate_table(table_of_no)
  lst = listtGenerator()
  tableW = WrongTable(table)
  print(tableW)
