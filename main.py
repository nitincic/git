print("Press\n1 for cube volume\n2 for cube surface area3for cuboid volume\n4 for cuboid surface area\n5 for exit");

a = int(raw_input("Give choice"));
print a;

if a==1:
    cube_volume();

if a==2:
    cube_surface_area();

if a==3:
    cuboid_volume();
