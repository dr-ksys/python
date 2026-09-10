distance_mi = 1
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if distance_mi > 0:
    if distance_mi <= 1 and is_raining == False:
        print('True')
        
    elif 1 < distance_mi <= 6 and (has_bike == True and is_raining == False):
        print('True')
        
    elif distance_mi > 6 and (has_car == True or has_ride_share_app == True):
        print('True')
        
    else:
        print('False')
  
else:
    print('False')