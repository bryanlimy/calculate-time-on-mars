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
    else:
        return None
