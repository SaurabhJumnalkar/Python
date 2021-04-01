'''
Code To find Weight Of Human Tower With The input of no. of People at the base are 35 and 2 people get removed on upper layer.
'''

def human_tower(no_of_people):
    if(no_of_people==1):
        return 1*(50)
    else:
        return no_of_people*(50)+human_tower(no_of_people-2)
print("Total weight of human tower: ",human_tower(35))