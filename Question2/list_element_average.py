def list_average(my_list):
    if my_list == []:
        raise(SyntaxError) #This avoids a divide by zero issue and the empty list
    else:
        sum = 0
        for element in my_list:
            try:    #Check if the element is a number. If not, then it should raise a type error to avoid weird string output
                int(element)
            except:
                rasie(TypeError)

            sum += element
        return sum/len(my_list)