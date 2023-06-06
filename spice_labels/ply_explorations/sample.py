'''



module shaft_rider(as_clearance=false, clearance = 0.5, wall = 2, h = 2) {
    d_shaft = 8.3;
    id = d_shaft + 2 * clearance;
    od = id  + 2 * wall;
    if (as_clearance) {
        can(d = id, h = a_lot);
    } else {
        difference() {
            can(d=od, h=h, center=ABOVE);
            can(d=id, h=a_lot);
        }        
    }
}

'''
false = False
a_lot = 100
ABOVE = ["center", "ABOVE"]
CENTER = ["center", "CENTER"]

def can(d, h, center=CENTER):
    return ["module", d, h]

def difference(*args):
    return ["difference", ] 
        
def shaft_rider(as_clearance=false, clearance = 0.5, wall = 2, h = 2):
    d_shaft = 8.3
    id = d_shaft + 2 * clearance
    od = id  + 2 * wall
    if (as_clearance):
        can(d = id, h = a_lot)
    else:
        difference( 
            can(d=od, h=h, center=ABOVE), #;
            can(d=id, h=a_lot)#;
        )        
    #}

