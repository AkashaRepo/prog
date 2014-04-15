core = 'active'
torch = 'standby'
sensor = 'active'
laser = 'standby'
truss = 100

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
        
def trustate():
    '''prints structural integrity'''
    print 'structural truss:'str(truss)+'% integirty'
        
corestate()
torchstate()
senstate()
lastate()
trustate()
