def swap_case(s:str):
    return ''.join([c.lower() if c.isupper() else c.upper() for c in s])