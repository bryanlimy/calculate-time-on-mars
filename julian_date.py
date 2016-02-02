def julian_date(day, month, year, hour, minute, second):
    '''(int, int, int, int, int, int) -> float
    Returns the Julian Date (as used in astronomy), given a Gregorian date and time. If given an invalid date/time, returns None. In the NASA calculations this is known as the JDUT.'''
    a = (14 - month)//12
    y = year + 4800 - a
    m = month + 12*a - 3
    julian_day_number = day + ((153*m + 2)//5) + 365*y + (y//4) - (y//100) + (y//400) - 32045
    julian_date = julian_day_number + (hour - 12)/24 + minute/1440 + second/86400
    if year > 1581:
        if month > 0 and month < 13:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if day > 0 and day < 32:
                    if hour >= 0 and hour <= 23:
                        if minute >= 0 and minute < 60:
                            if second >= 0 and second < 60:
                                return julian_date
                            else:
                                return None
                        else:
                            return None
                    else:
                        return None
                else:
                    return None
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if day > 0 and day < 31:
                    if hour >= 0 and hour <= 23:
                        if minute >= 0 and minute < 60:
                            if second >= 0 and second < 60:
                                return julian_date
                            else:
                                return None
                        else:
                            return None
                    else:
                        return None
                else:
                    return None
            elif month == 2:
                if day > 0 and day < 29:
                    return julian_date
                elif day > 0 and day < 30:
                    if year % 4 == 0:
                        if year % 100 == 0:
                            if year % 400 == 0:
                                if hour >= 0 and hour <= 23:
                                    if minute >= 0 and minute < 60:
                                        if second >= 0 and second < 60:
                                            return julian_date
                                        else:
                                            return None
                                    else:
                                        return None
                                else:
                                    return None
                            else:
                                return None
                        else:
                            return None
                    else:
                        return None
                else:
                    return None
            else:
                return None
        else:
            return None
    else:
        return None
