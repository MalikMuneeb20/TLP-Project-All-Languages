import os
from KinematicsFunctions import KinematicsFunction as ks
class PhysicsFunction :
    def PhysicsFormulae():
        while(True):
            os.system("cls")
            choice=input("Please Choose the following Formulae\n1. Speed\n2. Velocity\n3. Acceleration\n4. Time\n5. Displacement\n6. Back\nYour Choice : ")
            if choice == '1':
                print("\nSpeed")
                ks.Speed()
                input()
            elif choice == '2':
                print("\nVelocity")
                ks.Velocity()
                input()
            elif choice == '3':
                print("\nAcceleration")
                ks.Acceleration()
                input()
            elif choice == '4':
                print("\nTime")
                ks.Time()
                input()
            elif choice == '5':
                print("\nDisplacement")
                ks.Displacement()
                input()
            elif choice == '6':
                print("\nBack")
                break
            else:
                print("Wrong Input")
                input()  

                        