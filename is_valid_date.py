def is_valid_date(day, month, year):
    '''(int, int, int) -> bool
    Returns true iff day-month-year is a valid Gregorian date.'''

    if year > 1581:
        if month > 0 and month < 13:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if day > 0 and day < 32:
                    return True
                else:
                    return False
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if day > 0 and day < 31:
                    return True
                else:
                    return False
            elif month == 2:
                if day > 0 and day < 29:
                    return True
                elif day > 0 and day < 30:
                    if year % 4 == 0:
                        if year % 100 == 0:
                            if year % 400 == 0:
                                return True
                            else:
                                return False
                        else:
                            return True
                    else:
                        return False
                else:
                    return False
        else:
            return False
    else:
        return False   
