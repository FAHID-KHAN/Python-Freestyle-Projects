import random 


def computer_move(current_total):
    if current_total % 4 != 0:
        return current_total % 4
    else:
        return random.randint(1,3)
    

def person_move(current_total):
   pass
