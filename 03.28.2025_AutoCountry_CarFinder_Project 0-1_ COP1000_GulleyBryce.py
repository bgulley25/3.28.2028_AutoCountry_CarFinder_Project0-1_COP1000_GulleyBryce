# Car Finder for AutoCountry

allowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla Cybertruck', 'Toyota Tundra', 'Nissan Altima']
while True:
    print('*******************************')
    print('AutoCountry Vehicle Finder v0.1')
    print('*******************************')
    print('Please Enter the following number below from the following menu:')
    print('1. PRINT all Authorized Vehicles')
    print('2. Exit')
    
    numberEntered = input('Enter 1 or 2: ')

    if numberEntered == '1':
        print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
        for vehicles in allowedVehiclesList:
            print (vehicles)
    elif numberEntered == '2':
        print ('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
        break
    else:
        print ('Entry is out of bounds, please try again') 
