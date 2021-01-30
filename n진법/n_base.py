def convert_by_base(num, base):
    if not num:
        return ['0']
    
    result = []
    while num:
        num, rem = divmod(num, base)
        if rem == 10:
            rem = 'A'
        elif rem == 11:
            rem = 'B'
        elif rem == 12:
            rem = 'C'
        elif rem == 13:
            rem = 'D'
        elif rem == 14:
            rem = 'E'
        elif rem == 15:
            rem = 'F'
        
        result.append(str(rem))
    
    return result[::-1]
