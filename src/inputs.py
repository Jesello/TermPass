from color import c, Color
import crypt
import re 
import getpass

def print_list(x):
    
    for i in enumerate(x):
        print(f"{i[0]}: {i[1]}")
    
    print()

def get_struct():

    component = []
    struct = {}
    
    color = Color()

    print(c("\nEnter the components you want to store in the file.\nIt will move in a loop.\nWhen you want to stop, type exit or q and enter\n",color.info_color))
    print(c("For example:\n\tusername\n\temail\n\tpassword\n",color.info_color))
    
    while True:
        a = str(input(c(": ",color.input_color)))
        
        if (a in ["exit","q"]):
            break

        if a and (not a.isspace()):
            component.append(a)
            
    
    while True:
        print(c("\nIs it all true?\n",color.warning_color))
        
        print_list(component)
        
        check = input(c("[A]dd [E]dit [D]elete [O]kay: ",color.input_color))
    
        if (check in ["A","a"]):
    
            while True:
                a = input(c(": ",color.input_color))
                
                if a and (not a.isspace()):
                    component.append(a)
                    break
                
                
        if (check in ["E","e"]):
            try:
                index = int(input(c("\nindex: ",color.input_color)))
                nw = str(input(c("new value: ",color.input_color)))
                component[index] = nw
                    
            except:
                pass

        if (check in ["D","d"]):
            try:
                index = int(input(c("\nindex: ",color.input_color)))
                del component[index]
                    
            except:
                pass

        if (check in ["O","o"]):
            break
            
    print("\nStart filling\n")
    
    for i in component:
        a = input(c(f"{i}: ",color.input_color))
        struct[f'{i}'] = a

    print(c("\nIs it all true?\n",color.warning_color))

    for i in struct:
        print(f"{i} : {struct[i]}")
        
    print()
    
    while True:
        check = input(c("[E]dit [O]kay: ",color.input_color))

        if (check in ["E","e"]):
            try:
                index = str(input(c("\ncomponent: ",color.input_color)))
                nw = str(input(c("new value: ",color.input_color)))
                struct[index] = nw
                
                print()
                for i in struct:
                    print(f"{i} : {struct[i]}")
                print()
            except:
                pass
            

        if (check in ["O","o"]):
            break
            
    return struct

def get_key():
    
    color = Color()
    keys = crypt.Crypt().get_keys()
    
    
    print(c("\nAll available keys:\n",color.info_color))
    
    for i in enumerate(keys):
        
        print(f"- {i[0]} - {i[1]} -")
        
    print()
    
    while True:
        try:
            index = int(input(c("index: ",color.input_color)))
            key = keys[index].split(" ")[0]
            return key
        except:
            pass

def ask_password():
    
    color = Color()
    
    return getpass.getpass(c("\nPassword: ",color.input_color))