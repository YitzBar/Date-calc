import datetime
special_month_length = {
    2 : 28,
    4 : 30,
    6 : 30,
    9 : 30,
    11 : 30,
}

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

def is_valid_date_str(str):
    return True

def calc_new_date(orig_date, number_of_days):
    if(number_of_days==0):
        return orig_date
        
    retval = orig_date
    day = orig_date.day
    month = orig_date.month
    year = orig_date.year
    
    while True:
        if(number_of_days>28):
            day = day + 28
            number_of_days = number_of_days - 28
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
        #print(day,".",month,'.',year,' days to add: ',number_of_days)    
        if number_of_days == 0:
            retval = datetime.datetime(year, month, day)
            return retval
    
    

date = datetime.datetime(2022, 12, 30)
num_of_days = -30
print(date.strftime("%d.%m.%y"))
print(calc_new_date(date,num_of_days).strftime("%d.%m.%y"))



    

        