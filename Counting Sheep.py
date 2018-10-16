'''
Codewars: Counting sheep
'''
def count_sheeps(arrayOfSheeps):
    sheep = 0    
    for curly_sheep in arrayOfSheeps:
        if curly_sheep == True:
            sheep += 1
    return sheep

 