def swap_pair(num_list):
    """
    Description: This function swaps the alternate pairs in the list

    Parameter: num_list: Array of integers

    Return: Returns the swapped new list
    """
    
    for counter in range(0,len(num_list)-2,4):
    num_list[counter],num_list[counter+2]=num_list[counter+2],num_list[counter]
    num_list[counter+1],num_list[counter+3]=num_list[counter+3],num_list[counter+1]
    return num_list

list_len=int(input("Enter the number of elements in list: "))    
num_list=[int(input("Enter the number: ")) for counter in range(list_len)]
print(num_list)
    
swap_pair(num_list)