import math

def equeationSolver():
     a=int(input('solve the equeation: \n ax^2  + bx + c = 0 \n Enter the Value Of a : '))
     b= int(input('solve the equeation: \n'+ str(a)+'x^2  + bx + c = 0 \n Enter the Value Of b : '))
     c= int(input('solve the equeation: \n'+ str(a)+'x^2  +'+str(b)+'x + c = 0 \n Enter the Value Of c : '))
     print('The Equestrian is : \n'+str(a)+'x^2 + '+str(b)+'x + '+str(c)+' = 0')
     dis = ((b*b)-4*a*c) 
     print('dis = ' + str(dis))

     if(dis==0):
       root1= root2= (-b/(2*a))
       print('Root 1 : '+str(root1)+ '\n' + 'Root 2 : ' + str(root2))
     elif(dis>1) :
       root1=(-b + math.sqrt(dis))/(2*a)
       root2=(-b - math.sqrt(dis))/(2*a)
       print('Root 1 : '+str(root1)+ '\n' + 'Root 2 : ' + str(root2))
     else:
       realPart= (-b/(2*a))
       imPart = ((math.sqrt(-dis))/(2*a))
       print('Root 1 : '+ str(realPart)+'+'+str(imPart)+'i \n' +'Root 2 : '+str(realPart)+'-'+str(imPart)+'i')

while True:
    user_input = input("Do you want to continue? (Y/N): ").upper()
    if user_input == "Y":
        equeationSolver()
    elif user_input == "N":
        # Do something if the user says no
        print("You chose no.")
        break
    else:
        print("Invalid input. Please enter Y or N.")
