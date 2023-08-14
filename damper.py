import ross as rs
import numpy as np

# Classic Instantiation of the rotor 회전체 설정
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

rotor595c.plot_rotor()
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
rotor595fs.plot_rotor()

# Obtaining results for w=0

modal595c = rotor595c.run_modal(0)
modal595fs = rotor595fs.run_modal(0)

print("Normal Instantiation =", modal595c.wn * 60 / (2 * np.pi), "[RPM]")
print("\n")
print("From Section Instantiation =", modal595fs.wn * 60 / (2 * np.pi), "[RPM]")

# Obtaining results for w=4000RPM

modal595c = rotor595c.run_modal(4000 * np.pi / 30)  # speed input in rad/s
print("Normal Instantiation =", modal595c.wn * 60 / (2 * np.pi), "[RPM]")

# The input units must be according to your unit standard system
campbell = rotor595c.run_campbell(np.linspace(0, 4000 * np.pi / 30, 50))
# Plotting frequency in RPM
campbell.plot(frequency_units="rpm")
