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
