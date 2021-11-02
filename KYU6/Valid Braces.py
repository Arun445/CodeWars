def validBraces(string):
    
    list_of_strings = [i for i in string]
    closing_braces = [']', '}', ')']
    closing_dict = {']': '[', '}': '{', ')': '('}
    index=0
    check=0
    previous=''
    while len(list_of_strings) > 0:
        bracket = list_of_strings[index]
        
        if bracket in closing_braces:
            check=0
            if closing_dict[bracket] != previous:
                return False
            else:
                list_of_strings.pop(index)
                list_of_strings.pop(index-1)
                index=0
                previous=''
        else:
            previous = bracket
            index +=1
            check+=1
        if index >= len(list_of_strings):
            index=0
            previous=''
        if check > len(string):
            return False
            
    return True