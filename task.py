import datetime
special_month_length = {
    2 : 28,
    4 : 30,
    6 : 30,
    9 : 30,
    11 : 30,
}

shortest_month = min(special_month_length.values())

def is_leap_year(x):
    if(x%400 ==0):
        return True
    elif((x%4 ==0)and(x%100 !=0)):
        return True
    return False
    
def get_month_length(x):
    if(x in  special_month_length):
        return special_month_length[x]
    return 31

def calc_new_date(str_date, number_of_days):
    #----- validate parameters -----
    if(number_of_days<0):
        print('Invalid namber of days')
        return str_date
    
    orig_date = str_date.split('.')  
    
    if(len(orig_date)!=3):
        print('Invalid date format, should be DD.MM.YYYY')
        return str_date
    
    for x in orig_date:
        if not x.isdigit():
            print('Invalid date value, date should contain numbers only.')
            return str_date
    
    day = int(orig_date[0])
    month = int(orig_date[1])
    year = int(orig_date[2])
    
    if(day<0 or day>31 or month<1 or month>12):
        print('Invalid date value.')
        return str_date
    
    retval = '{}.{}.{}'
    
    while (number_of_days!=0):
        if(number_of_days > shortest_month):
            day = day + shortest_month
            number_of_days = number_of_days - shortest_month
        else:
            day = day + number_of_days
            number_of_days = 0
           
        month_length = get_month_length(month)
        
        if(is_leap_year(year) and (month==2)):
            month_length = month_length +1
            
        if day > month_length:
            month = month + 1
            day = day - month_length
            
        if month >= 13:
            month = 1
            year = year + 1
    
    return retval.format(day, month, year)
