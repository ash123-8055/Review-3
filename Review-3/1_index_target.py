
def find_index(num_list,target):
    """
    Description: To get index of the Numbers which add upto target
    
    Parameter: num_list: The array of integer
               target: The target number
               
    Return: Returns the index
    """
    
    for counter1 in range(len(num_list)):
        for counter2 in range(counter1+1,len(num_list)):
            if num_list[counter1]+num_list[counter2]==target:
                return(f"[{counter1},{counter2}]")

list_len=int(input("Enter the number of elements in list: "))    
num_list=[int(input("Enter the number: ")) for counter in range(list_len)]
target=int(input("Enter the target number: "))

print(find_index(num_list,target))
            
            