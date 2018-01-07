#Function Create Table
def createBoard():
    lst_1=['7','8','9']
    lst_2=['4','5','6']
    lst_3=['1','2','3']
    global matrix 
    matrix = [lst_1,lst_2,lst_3]

    return matrix

def PrintBoard():
    for num in matrix:
        print(num)

def Input():
    global position
    global marker
    position = input("Please enter a number for the borad code:")
    marker = input("Please enter a X or O for the borad:")
    return position,marker
    
createBoard()
PrintBoard()
Input()
