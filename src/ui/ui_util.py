
def read_bounded_int(min, max):
    while True:
        xstr = input("")
        x = None
        
        try: x = int(xstr)
        except:
            print ("Canceled.")
            return None

        if (x >= min and x <= max): return x
        else: 
            print ('Input is out of range', 'Try again', sep='\n')

