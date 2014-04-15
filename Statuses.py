core = 'active'
torch = 'standby'
sensor = 'active'
laser = 'standby'
truss = 100
beacons = False

def corestate():
    '''prints core status'''
    if core == 'active':
        print 'computer core: active'
    else: 
        print 'computer core: standby'
        
def torchstate():
    '''prints torch status'''
    if torch == 'active':
        print 'torch drive: active'
    elif torch == 'standby':
        print 'torch drive: standby'
    else:
        print 'torch drive: inactive'
        
def trustate():
    '''prints structural integrity'''
    if truss >= 1 and truss <= 100:
        print 'structural truss: '+str(truss)+'% integrity'
    elif truss < 1:
        print 'structural truss: ERROR! STRUCTURAL FAILURE!'
    else: print 'structural truss: ERROR! UNKNOWN ERROR'

def senstate():
    '''prints sensor status'''
    if sensor == 'active':
        print 'sensor suite: active'
    elif sensor == 'standby':
        print 'sensor suite: standby'
    else:
        print 'sensor suite: inactive'
        
def lastate():
    '''prints laser status'''
    if laser == 'active':
        print 'comunications laser: active'
    elif laser == 'standby':
        print 'comunications laser: standby'
    else:
        print 'comunications laser: inactive'

def navstate():
    '''prints navigation status'''
    if beacons == True:
        print: 'navigation: connecting to network...'
    else:
        print: 'navigation: ERROR! no nav-becons detected!'

def status():
    corestate()
    torchstate()
    trustate()
    senstate()
    lastate()
    navstate()
    
status()
