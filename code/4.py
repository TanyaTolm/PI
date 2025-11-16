class NegativeValueExeption(Exception): pass

def check_name(name):
    if len(name) > 10:
        raise  NegativeValueExeption('')
    else: print('')
    
if __name__ == '__main__':
    name = '12345678910'
    check_name(name)