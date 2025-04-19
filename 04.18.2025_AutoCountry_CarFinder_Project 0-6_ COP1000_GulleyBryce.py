import os

filePath = 'Cars_List.txt'

# function for reading file
def loadData():
    if not os.path.exists(filePath):
        return [] 
    
    file = open(filePath, 'r')  
    lines = file.readlines() 
    file.close()  
    vehicles = []
    for line in lines:
        vehicles.append(line.strip())  
    
    return vehicles

# function for opening and writing to file
def saveData(vehicles):
    with open(filePath, 'w') as file:
        for vehicle in vehicles:
            file.write(vehicle + '\n')

allowedVehiclesList = loadData()

# function to print all authorized vehicles
def displayAllowedVehicles():
    print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
    for vehicle in allowedVehiclesList:
        print(vehicle)

# function to search authorized vehicles
def checkVehicleAuthorized():
    print('*******************************')
    carName = input('Please Enter the full Vehicle name: ')
    if carName in allowedVehiclesList:
        print(f'{carName} is an authorized dealer')
    else:
        print(f'{carName} is not an authorized dealer, if you received this in erros please check the spelling and try again')

# function to add authorized vehicle
def addCar():
    addCar = input('Please Enter the full Vehicle name you would like to add:')
    allowedVehiclesList.append(addCar)
    saveData(allowedVehiclesList)  
    print('You have added "'  + addCar + '" as an authorized vehicle')

# function to delete authorized vehicle
def deleteCar():
    deleteCar = input('Please Enter the full Vehicle name you would like to REMOVE: ' )
    if deleteCar in allowedVehiclesList:
        allowedVehiclesList.remove(deleteCar)
        while True:
            confirmRemove = input(f'Are you sure you want to remove "{deleteCar}" from the Authorized Vehicles List? (yes/no): ')
            if confirmRemove.lower() == 'no':
                allowedVehiclesList.append(deleteCar)  
                break
            elif confirmRemove.lower() == 'yes':
                saveData(allowedVehiclesList)  
                print('You have REMOVED "' + deleteCar + '" as an authorized vehicle')
                break
            else:
                print('Entry is out of bounds, please try again')
    else:
        print(f'"{deleteCar}" not found in the authorized vehicles list.')

# prints instructions for user
while True:
    print('*******************************')
    print('AutoCountry Vehicle Finder v0.1')
    print('*******************************')
    print('Please Enter the following number below from the following menu:')
    print('1. PRINT all Authorized Vehicles')
    print('2. SEARCH for Authorized Vehicle')
    print('3. ADD Authorized Vehicle')
    print('4. DELETE Authorized Vehicle')
    print('5. Exit')
    numberEntered = input()


    if numberEntered == '1':
        displayAllowedVehicles()
    elif numberEntered == '2':
        checkVehicleAuthorized()
    elif numberEntered == '3':
        addCar()
    elif numberEntered == '4':
        deleteCar()
    elif numberEntered == '5':
        print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
        break
    else:
        print('Entry is out of bounds, please try again')