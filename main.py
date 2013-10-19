<<<<<<< HEAD
print("Press\n1 for cube volume\n2 for cube surface area3for cuboid volume\n4 for cuboid surface area\n5 for exit");

a = int(raw_input("Give choice"));
print a;

if a==1:
    cube_volume();

if a==2:
    cube_surface_area();

if a==3:
    cuboid_volume();
=======
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


>>>>>>> 2a33ccd4e717d5a017acd339fc0fd48716160460
