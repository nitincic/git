
def cuboid_surface_area():
    print "the surface area is 25";
    
print("Press\n1 for cube volume\n2 for cube surface area3for cuboid volume\n4 for cuboid surface area\n5 for exit");

a = int(raw_input("Give choice"));
print a;

def cube_volume():
    i=float(raw_input("Enter side length "))
    return i*i*i

def cuboid_volume():
    l=float(raw_input("Enter length "))
    b=float(raw_input("Enter width "))
    h=float(raw_input("Enter height "))
    return l*b*h

def cube_volume():
    i=float(raw_input("Enter side length"))
    return i*i*i

def cube_surface_area():
    i=float(raw_input("Enter side length "))
    return 6*i*i
