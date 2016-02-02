def frac_time_to_hour(t):
    '''(float) -> int
    Given a positive fractional time in hours, returns the hours as an integer. Uses 24-hour time, with 0 being midnight.'''

    if t >=0 and t < 24:
        frac_time_to_hour = t // 1
        return frac_time_to_hour
    elif t >= 24:
        frac_time_to_hour = t - (t//24)*24
        return frac_time_to_hour
    else:
        return None
