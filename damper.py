import ross as rs
import numpy as np

# Classic Instantiation of the rotor
shaft_elements = []
bearing_seal_elements = []
disk_elements = []
steel = rs.steel
for i in range(6):
    shaft_elements.append(rs.ShaftElement(L=0.25, material=steel, n=i, idl=0, odl=0.05))

disk_elements.append(
    rs.DiskElement.from_geometry(n=2, material=steel, width=0.07, i_d=0.05, o_d=0.28)
)

disk_elements.append(
    rs.DiskElement.from_geometry(n=4, material=steel, width=0.07, i_d=0.05, o_d=0.35)
)
bearing_seal_elements.append(rs.BearingElement(n=0, kxx=1e6, kyy=1e6, cxx=3e3, cyy=3e3))
bearing_seal_elements.append(rs.BearingElement(n=6, kxx=1e6, kyy=1e6, cxx=3e3, cyy=3e3))

rotor595c = rs.Rotor(
    shaft_elements=shaft_elements,
    bearing_elements=bearing_seal_elements,
    disk_elements=disk_elements,
)

# From_section class method instantiation.
bearing_seal_elements = []
disk_elements = []
shaft_length_data = 3 * [0.5]
i_d = 3 * [0]
o_d = 3 * [0.05]

disk_elements.append(
    rs.DiskElement.from_geometry(n=1, material=steel, width=0.07, i_d=0.05, o_d=0.28)
)

disk_elements.append(
    rs.DiskElement.from_geometry(n=2, material=steel, width=0.07, i_d=0.05, o_d=0.35)
)
bearing_seal_elements.append(rs.BearingElement(n=0, kxx=1e6, kyy=1e6, cxx=3e3, cyy=3e3))
bearing_seal_elements.append(rs.BearingElement(n=3, kxx=1e6, kyy=1e6, cxx=3e3, cyy=3e3))

rotor595fs = rs.Rotor.from_section(
    brg_seal_data=bearing_seal_elements,
    disk_data=disk_elements,
    leng_data=shaft_length_data,
    idl_data=i_d,
    odl_data=o_d,
    material_data=steel,
)
rotor595c.plot_rotor().show()

rotor595fs.plot_rotor().show()
