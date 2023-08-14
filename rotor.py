import ross as rs
import numpy as np

steel = rs.steel
n = 6

shaft_elem = [
    rs.ShaftElement(
        L=0.25,
        idl=0.0,
        odl=0.05,
        material=steel,
        shear_effects=True,
        rotary_inertia=True,
        gyroscopic=True,
    )
    for _ in range(n)
]

disk0 = rs.DiskElement.from_geometry(
    n=2, material=steel, width=0.07, i_d=0.05, o_d=0.28
)
disk1 = rs.DiskElement.from_geometry(
    n=4, material=steel, width=0.07, i_d=0.05, o_d=0.28
)
disks = [disk0, disk1]

stfx = 1e6
stfy = 0.8e6
bearing0 = rs.BearingElement(0, kxx=stfx, kyy=stfy, cxx=0, n_link=7)
bearing1 = rs.BearingElement(6, kxx=stfx, kyy=stfy, cxx=0)
bearing2 = rs.BearingElement(7, kxx=stfx, kyy=stfy, cxx=0)

bearings = [bearing0, bearing1, bearing2]

pm0 = rs.PointMass(n=7, m=30)
pointmass = [pm0]

rotor1 = rs.Rotor(shaft_elem, disks, bearings, pointmass)

print("Rotor total mass = ", np.round(rotor1.m, 2))
print("Rotor center of gravity =", np.round(rotor1.CG, 2))

# plotting the rotor model
rotor1.plot_rotor().show()
