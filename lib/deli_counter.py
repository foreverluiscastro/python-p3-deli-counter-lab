def line(katz_deli):
    pass
    if len(katz_deli) == 0:
        pass
        print("The line is currently empty.")
    else:
        pass
        callout = "The line is currently:"
        for idx, name in enumerate(katz_deli):
            pass
            callout += f" {idx + 1}. {name}"
        
        print(callout)

def take_a_number(katz_deli, new_person):
    pass
    katz_deli.append(new_person)
    position = len(katz_deli)
    print(f"Welcome, {new_person}. You are number {position} in line.")
    

def now_serving(katz_deli):
    pass
    if len(katz_deli) == 0:
        pass
        print(f"There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)
    