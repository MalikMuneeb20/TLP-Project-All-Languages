import os
from Physics import Kinematics as k
from PhysicsConditions import PhysicsFunction as ps

# print(k.velocity_using_initialVelocity_displacement_acceleration(8, 18, 1))

os.system('CLS')

while(True):
    os.system('CLS')
    choice=input("Please Choose the following Liabrary\n1. Physics Liabrary\n2. Math Liabrary\n3. Exit\nYour Choice : ")
    

    if choice == '1':
        print("\nPhysics Liabrary")
        ps.PhysicsFormulae()
    elif choice == '2':
        print("\nMaths Liabrary")
        input()
    elif choice == '3':
        print("\nExit")
        quit()
    else:
        print("Wrong Input")
        input()    

