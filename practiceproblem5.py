def next_palindrome(n):
   n = n+1
   while not is_palindrome(n):
      n += 1
   return n

def is_palindrome(n):
   return str(n) == str(n)[::-1]

if __name__ == '__main__':
    new_list = [1, 3, ]
    for element in new_list:
       if element >10:
          n = next_palindrome(element)
          new_list.append(n)
       else:
          new_list.append(element)
print(f"output list: {new_list}")
