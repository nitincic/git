print("Press\n1 for cube volume\n2 for cube surface area3for cuboid volume\n4 for cuboid surface area\n5 for exit");

a = int(raw_input("Give choice"));
print a;

def cube_volume():
    i=float(raw_input("Enter side length "))
    return i*i*i
