import math


def is_leap_year(year):
    ''' (int) -> (bool)
    Returns true iff the value of "year" is a Leap Year in the Gregorian Calendar. Will return the string None if given inappropriate input (non-int or pre-1582).'''

    if year >= 0:

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


def is_valid_date(day, month, year):
    '''(int, int, int) -> bool
    Returns true iff day-month-year is a valid Gregorian date.'''
    
    if year > 1581:

        if month > 0 and month < 13:

            if month == 1 or month == 3 or month == 5\
               or month == 7 or month == 8 or month == 10 or month == 12:

                if day > 0 and day < 32:
                    return True

                else:
                    return False

            elif month == 4 or month == 6\
                 or month == 9 or month == 11:

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
    

def julian_day_number(day, month, year):
    '''(int, int, int) -> int
    Returns the Julian Day Number (as used in astronomy), given a Gregorian date. If given an invalid date, returns None.'''

    a = (14 - month)//12
    y = year + 4800 - a
    m = month + 12*a - 3
    julian_day_number = day + ((153*m + 2)//5) + 365*y + (y//4) -\
                        (y//100) + (y//400) - 32045


    if is_valid_date(day, month, year):
        return julian_day_number

    else:
        return None


def is_valid_time(hour, minute, second):
    '''(int, int, int) -> bool
    Returns true if and only if HH:MM:SS is a valid hour/minute/second.'''

    
    if hour >= 0 and hour <= 23:
        
        if minute >= 0 and minute < 60:
            
            if second >= 0 and second < 60:
                return True

            else:
                return None

        else:
            return None

    else:
        return None


def julian_date(day, month, year, hour, minute, second):
    '''(int, int, int, int, int, int) -> float
    Returns the Julian Date (as used in astronomy), given a Gregorian date and time. If given an invalid date/time, returns None. In the NASA calculations this is known as the JDUT.'''

    a = (14 - month)//12
    y = year + 4800 - a
    m = month + 12*a - 3
    
    julian_day_number = day + ((153*m + 2)//5) + 365*y + (y//4) - (y//100) + (y//400) - 32045
    
    julian_date = julian_day_number + (hour - 12)/24 + (minute/1440) + (second/86400)


    if is_valid_date(day, month, year) and is_valid_time(hour, minute, second):
        return julian_date
    
    else:
        return None
    


def frac_time_to_hour(t):
    '''(float) -> int
    Given a positive fractional time in hours, returns the hours as an integer. Uses 24-hour time, with 0 being midnight.'''


    if t >=0 and t < 24:
        frac_time_to_hour = t // 1
        return frac_time_to_hour

    elif t >= 24:
        frac_time_to_hour = t - (t//24)*24
        return frac_time_to_hour
    # when the given time(t) is larger than 24, it will cycle it back to within 24 hours.
    

def frac_time_to_min(t):
    '''(float) -> int
    Given a positive fractional time in hours, returns the minutes as an integer.'''


    if t >= 0 and t < 24:
        frac_time_to_min = ((t - (t // 1)) *60)//1
        return frac_time_to_min

    elif t >= 24:
        frac_time_to_min = ((t - (t//24)*24) *60)//1
        return frac_time_to_min
    # when the given time(t) is larger than 24, it will cycle it back to within 24 hours.


def frac_time_to_sec(t):
    '''(float) -> int
    Given a positive fractional time in hours, returns the seconds as an integer.'''


    if t >= 0 and t < 24:
        frac_time_to_min = (t - (t // 1)) *60
        frac_time_to_sec = ((frac_time_to_min - (frac_time_to_min//1)) * 60) // 1
        return frac_time_to_sec

    elif t >= 24:
        frac_time_to_min = (t - (t//24)*24) *60
        frac_time_to_sec = ((frac_time_to_min - (frac_time_to_min//1))*60) //1
        return frac_time_to_sec
    # when the given time(t) is larger than 24, it will cycle it back to within 24 hours.




def time_to_str(hours, minutes, seconds):
    '''(int, int, int) -> str
    Given hours, minutes, seconds, returns them as a string in HH:MM:SS format. Provided to students.'''


    h = ("00" + str(hours))[-2:]
    m = ("00" + str(minutes))[-2:]
    s = ("00" + str(seconds))[-2:]
    return h + ":" + m + ":" + s


def julian_date_TT(JDUT):
    '''(float) -> float
    Calculates the Julian Date in Terrestrial Time (TT), known as the JDTT in these calculations. 
    Returns None if given bad input. Provided to students.'''


    if type(JDUT) == float and math.isfinite(JDUT):
        T = (JDUT - 2451545.0) / 36525
        TT_UTC = 64.184 + 59*T - 51.2*T**2 - 67.1*T**3 - 16.4*T**4 
        return JDUT + (TT_UTC / 86400)


def time_since_J2000_epoch(JDTT):
    '''(float) -> float
    Calculates the time offset since the J2000 epoch, known as ΔtJ2000 in the Mars24 algorithm. 
    Returns None if given bad input. Provided to students.'''


    if type(JDTT) == float and math.isfinite(JDTT):
        return JDTT - 2451545.0 


def mars_mean_anomaly(ΔtJ2000):
    '''(float) -> float
    Calculates M, the Mars mean anomaly (step B-1). Returns None if given bad input. Don't forget to mod the result by 360.'''


    if type(ΔtJ2000) == float:
        
        M = (19.3870 + 0.52402075 * ΔtJ2000) % 360
        return M
    
    else:
        return None


def fiction_mean_sun(ΔtJ2000):
    '''(float) -> float
    Calculates a_FMS, the Fiction Mean Sun (step B-2). Returns None if given bad input. Don't forget to mod the result by 360.'''

    
    if type(ΔtJ2000) == float:
        
        a_FMS = (270.3863 + 0.52403840 * ΔtJ2000) % 360
        return a_FMS

    else:
        return None


def perturbers(ΔtJ2000):
    '''(float) -> float
    Calculates PBS, the pertubers. You'll want a helper method for this. Step B-3. Returns None if given bad input.'''


    if type(ΔtJ2000) == float:
        
        angle = 360 / 365.25 #given on NASA's website 0.985626° = 360° / 365.25, fraction is more accurate.

        PBS_1 = (0.0071) * math.cos(math.radians((angle * ΔtJ2000 / 2.2353) + 49.409))
        PBS_2 = (0.0057) * math.cos(math.radians((angle * ΔtJ2000 / 2.7543) + 168.173))
        PBS_3 = (0.0039) * math.cos(math.radians((angle * ΔtJ2000 / 1.1177) + 191.837))
        PBS_4 = (0.0037) * math.cos(math.radians((angle * ΔtJ2000 / 15.7866) + 21.736))
        PBS_5 = (0.0021) * math.cos(math.radians((angle * ΔtJ2000 / 2.1354) + 15.704))
        PBS_6 = (0.0020) * math.cos(math.radians((angle * ΔtJ2000 / 2.4694) + 95.528))
        PBS_7 = (0.0018) * math.cos(math.radians((angle * ΔtJ2000 / 32.8493) + 49.095))

        PBS = PBS_1 + PBS_2 + PBS_3 + PBS_4 + PBS_5 + PBS_6 + PBS_7
        return PBS
    
    else:
        return None


def equation_of_centre(ΔtJ2000):
    '''(float, float) -> float
    Calculates the nu - M, Equation of Centre (Step B-4).  Returns None if given bad input.'''


    if type(ΔtJ2000) == float:
        
        M = mars_mean_anomaly(ΔtJ2000)   
        PBS = perturbers(ΔtJ2000)

        nu = (((10.691 + 3.0 * (10 ** -7) * ΔtJ2000) * math.sin(math.radians(M))) + \
              (0.623 * math.sin(math.radians(2 * M))) + \
              (0.050 * math.sin(math.radians(3 * M))) + \
              (0.005 * math.sin(math.radians(4 * M))) + \
              (0.0005 * math.sin(math.radians(5 * M))) + PBS) + M
        # nu - M = variable is equivalent to nu = variable - M
        return (nu - M)
    
    else:
        return None


def solar_longitude(a_FMS, nu_M):
    '''(float, float) -> float
    Calculates the aerocentric solar longitude, L_s. (Step B-5). Returns None if given bad input. Don't forget to mod the result by 360.'''


    if type(a_FMS) == float and type(nu_M):
        L_s = (a_FMS + nu_M) % 360
        return L_s
    
    else:
        return None


def equation_of_time(L_s, nu_M):
    '''(float, float) -> float
    Calculates EOT, the Equation of Time. Keep your result in degrees. (Step C-1). Returns None if given bad input.'''


    if type(L_s) == float and type(nu_M) == float:
        EOT = (2.861 * math.sin(math.radians(2 * L_s)) - 0.071 * math.sin(math.radians(4 * L_s))\
               + 0.002 * math.sin(math.radians(6 * L_s)) - nu_M)
        return EOT
    
    else:
        return None


def coordinated_mars_time(JDTT):
    '''(float) -> float
    Calculates MTC, the Coordinated Mars Time, in fractional time. Step C-2. Returns None if given bad input.'''


    if type(JDTT) == float:
        
        MTC = (24 * (((JDTT - 2451549.5) / 1.027491252) + 44796.0 - 0.00096)) % 24
        return MTC
        
    else:
        return None


def local_mean_solar_time(MTC, longit):
    '''(float) -> float
    Calculates LMST, Local Mean Solar Time, in fractional time. Step C-3. Returns None if given bad input.'''


    if type(MTC) == float and type(longit) == float:
        LMST = MTC - longit * (24 /360)
        return LMST
    
    else:
        return None


def local_true_solar_time(LMST, EOT):
    '''(float) -> float
    Calculates LTST, the Local True Solar Time, in fractional time. Step C-4. Returns None if given bad input.'''


    if type(LMST) == float and type(EOT) == float:
        LTST = LMST + EOT * (24 / 360)
        return LTST
    
    else:
        return None


def time_on_mars(day, month, year, hours, minutes, seconds, longitude, use_true_time):
    '''(int, int, int, int, int, int, float, bool) -> str
    Given a date/time on Earth, a longitude on Mars, will calculate the time on Mars. The boolean use_true_time indicates whether to use mean solar time (LMST) or true solar time (LTST). Time is returned as a string in HH:MM:SS format. If given invalid input, returns None.'''


    JDUT = julian_date(day, month, year, hours, minutes, seconds)
    JDTT = julian_date_TT(JDUT)
    ΔtJ2000 = time_since_J2000_epoch(JDTT)
    MTC = coordinated_mars_time(JDTT)
    PBS = perturbers(ΔtJ2000)
    nu_M = equation_of_centre(ΔtJ2000)
    a_FMS = (270.3863) + 0.52403840 * ΔtJ2000
    L_s = solar_longitude(a_FMS, nu_M)
    EOT = equation_of_time(L_s, nu_M)
    LMST = local_mean_solar_time(MTC, longitude)
    LTST = local_true_solar_time(LMST, EOT)
    # define each variable

    
    if use_true_time == True:
        t = LTST
        h = frac_time_to_hour(t)
        m = frac_time_to_min(t)
        s = frac_time_to_sec(t)
        return time_to_str(int(h), int(m) ,int(s))
    
    elif use_true_time == False:
        t = LMST
        h = frac_time_to_hour(t)
        m = frac_time_to_min(t)
        s = frac_time_to_sec(t)
        return time_to_str(int(h), int(m) ,int(s))


def secular_distance(day, month, year):
    '''(int, int, int) -> int
    Provided with a year in the Gregorian calendar, returns the secular distance of that year with the Julian calendar. If not given a valid year, returns None.'''

        
    if (year % 100 == 0):
            
        if month == 1 or month == 2:
            H = ((year - 1) // 100)

        else:
            H = (year // 100)

    else:
        H = (year // 100)



    if is_valid_date(day, month, year):
        D = (H - (H // 4) - 2)
        return D
    
    else:
        return None
