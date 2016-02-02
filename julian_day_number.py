def julian_day_number(day, month, year):
    '''(int, int, int) -> int
    Returns the Julian Day Number (as used in astronomy), given a Gregorian date. If given an invalid date, returns None.'''

    a = (14 - month)//12
    y = year + 4800 - a
    m = month + 12*a - 3
    julian_day_number = day + ((153*m + 2)//5) + 365*y + (y//4) - (y//100) + (y//400) - 32045
    if year > 1581:
        if month > 0 and month < 13:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if day > 0 and day < 32:
                    return julian_day_number
                else:
                    return None
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if day > 0 and day < 31:
                    return julian_day_number
                else:
                    return None
            elif month == 2:
                if day > 0 and day < 29:
                    return julian_day_number
                elif day > 0 and day < 30:
                    if year % 4 == 0:
                        if year % 100 == 0:
                            if year % 400 == 0:
                                return julian_day_number
                            else:
                                return None
                        else:
                            return julian_day_number
                    else:
                        return None
                else:
                    return None
        else:
            return None
    else:
        return None 
    return julian_day_number
