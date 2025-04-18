import os

file_path = 'Cars_List.txt'

def load_data():
    if not os.path.exists(file_path):
        return [] 
    
    file = open(file_path, 'r')  
    lines = file.readlines() 
    file.close()  
    vehicles = []
    for line in lines:
        vehicles.append(line.strip())  
    
    return vehicles

def save_data(vehicles):
    with open(file_path, 'w') as file:
        for vehicle in vehicles:
            file.write(vehicle + '\n')

allowedVehiclesList = load_data()

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
        print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
        for vehicles in allowedVehiclesList:
            print(vehicles)
    elif numberEntered == '2':
        print('*******************************')
        carName = input('Please Enter the full Vehicle name:')
        if carName in allowedVehiclesList:
            print(carName + ' is an authorized vehicle')
        else:    
            print(carName + ' is not an authorized vehicle, if you received this in error please check the spelling and try again')
    elif numberEntered == '3':
        addCar = input('Please Enter the full Vehicle name you would like to add:')
        allowedVehiclesList.append(addCar)
        save_data(allowedVehiclesList)  
        print('You have added "'  + addCar + '" as an authorized vehicle')
    elif numberEntered == '4':
        deleteCar = input('Please Enter the full Vehicle name you would like to REMOVE: ' )
        if deleteCar in allowedVehiclesList:
            allowedVehiclesList.remove(deleteCar)
            while True:
                confirmRemove = input(f'Are you sure you want to remove "{deleteCar}" from the Authorized Vehicles List? (yes/no): ')
                if confirmRemove.lower() == 'no':
                    allowedVehiclesList.append(deleteCar)  
                    break
                elif confirmRemove.lower() == 'yes':
                    save_data(allowedVehiclesList)  
                    print('You have REMOVED "' + deleteCar + '" as an authorized vehicle')
                    break
                else:
                    print('Entry is out of bounds, please try again')
        else:
            print(f'"{deleteCar}" not found in the authorized vehicles list.')
    
    elif numberEntered == '5':
        print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
        break
    else:
        print('Entry is out of bounds, please try again')
