# Write code to remove duplicates from an unsorted linked list.

def take_unique_values(arr):
  unique_dict = {}
  for val in arr:
    unique_dict[val] = True
  
  len(unique_dict)
  
  print("unique_dict, orig_len", len(unique_dict), len(arr))
  print(unique_dict)
  

def no_temp_buffers(arr):
  inner_counter = 0
  outer_counter = 0
  len_array = len(arr)
  while outer_counter < len_array:
    while inner_counter < len_array:
      if arr[outer_counter] == arr[inner_counter] and outer_counter != inner_counter:
        print('inside if:', outer_counter, inner_counter)
        arr.pop(inner_counter)
        len_array -= 1
      else:
        print('inside else:', arr[outer_counter], arr[inner_counter])
        inner_counter += 1
        
    inner_counter = 0   
    outer_counter += 1 
    print('length array', len(arr), 'outer counter', outer_counter)
  return arr


short = [0,1,1]
ex = [1,0,1]
arr = [0,1,2,3,3,4,5,6,7,7]
print(no_temp_buffers(arr))
