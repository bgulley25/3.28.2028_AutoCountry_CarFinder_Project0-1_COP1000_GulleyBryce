# Car Finder for AutoCountry

allowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla Cybertruck', 'Toyota Tundra', 'Nissan Altima']
while True:
    print('*******************************')
    print('AutoCountry Vehicle Finder v0.1')
    print('*******************************')
    print('Please Enter the following number below from the following menu:')
    print('1. PRINT all Authorized Vehicles')
    print('2. SEARCH for Authorized Vehicle')
    print('3. ADD Authorized Vehicle')
    print('4. Exit')
    numberEntered = input()

    if numberEntered == '1':
        print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
        for vehicles in allowedVehiclesList:
            print (vehicles)
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
        print('You have added "'  + addCar + '" as an authorized vehicle')
    elif numberEntered == '4':
        print ('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
        break
    else:
        print ('Entry is out of bounds, please try again') 
