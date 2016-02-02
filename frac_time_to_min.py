def frac_time_to_min(t):
    '''(float) -> int
    Given a positive fractional time in hours, returns the minutes as an integer.'''

    if t >=0 and t <=24:
        frac_time_to_min = ((t - (t // 1)) *60)//1
        return frac_time_to_min
    elif t > 24:
        frac_time_to_min = ((t - (t//24)*24) *60)//1
        return frac_time_to_min
    else:
        return None
