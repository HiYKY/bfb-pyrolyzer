# Case Information
# ----------------------------------------------------------------------------

case = {
    'case_system': 'NREL 2FBR system',
    'case_reactor': 'BFB pyrolyzer',
    'case_desc': 'Smaller size sand material for bed',
    'case_num': 1,
    'p': (101_325, 150_000),        # Pressure range [Pa]
    'q': (14, 24),                  # Volumetric flow range [SLM]
    'tk': (723.15, 823.15)          # Temperature range [K]
}

# Bed Particle
# ----------------------------------------------------------------------------

bed = {
    'sample_desc': 'Black Rock W-430 sand, 250-425 µm',
    'sample_id': 'NETL-MAT-237',
    'sample_ref': 'William Rogers. NETL Multiphase Flow Analysis Laboratory. June 21, 2019.',
    'dp': 0.000306,                 # Mean particle diameter [m]
    'dp_min': 0.000219,             # Minimum particle diameter [m]
    'dp_max': 0.000432,             # Maximum particle diameter [m]
    'phi': 0.90,                    # Sphericity [-]
    'rho': 2600                     # Density [kg/m³]
}

# Biomass Particle
# ----------------------------------------------------------------------------

# Specific gravity (density) and thermal conductivity from Wood Handbook Table 4-7

biomass = {
    'sample_desc': 'Loblolly Pine',
    'sample_id': 'NETL-MAT-241',
    'sample_ref': 'William Rogers. NETL Multiphase Flow Analysis Laboratory. June 21, 2019.',
    'dp': 0.000134,         # Mean particle diameter [m]
    'dp_min': 0.000042,     # Minimum particle diameter [m]
    'dp_max': 0.000846,     # Maximum particle diameter [m]
    'phi': 0.64,            # Sphericity of biomass particle [-]
    'rho': 540,             # Density of loblolly pine [kg/m³]
    'b': 2,                 # Shape factor for particle transient heat conduction [-]
    'h': 350,               # Heat transfer coefficient for convection [W/m²K]
    'k': 0.12,              # Thermal conductivity of loblolly pine [W/mK]
    'm': 1000,              # Number of nodes from particle center (m=0) to surface (m)
    'mc': 0.0,              # Moisture content [%]
    'nt': 1000,             # Number of time steps for particle temperature profile [-]
    't_max': 6,             # Time duration to calculate particle temperature profile [s]
    'tk_init': 293.15       # Initial particle temperature [K]
}

# Char particle
# ----------------------------------------------------------------------------

char = {
    'dp': 0.000134,         # Mean particle diameter [m]
    'phi': 0.64,            # Sphericity [-]
    'rho': 120              # Density [kg/m³]
}

# Gas Properties
# ----------------------------------------------------------------------------

gas = {
    'sp': ['H2', 'N2'],     # Gas species of each component in gas mixture [-]
    'x': [0.85, 0.15],      # Mole fraction of each component in gas mixture [-]
    'p': 101_325,           # Gas pressure in reactor [Pa]
    'tk': 773.15            # Gas temperature in reactor [K]
}

# Reactor Geometry and Conditions
# ----------------------------------------------------------------------------

reactor = {
    'di': 0.05232,      # Inner diameter of reactor [m]
    'ep': 0.45,         # Void fraction of bed material [-]
    'ht': 0.4318,       # Total height of reactor [m]
    'q': 14,            # Volumetric flowrate of gas into reactor [SLM]
    'zmf': 0.1016       # Bed height at minimum fluidization [m]
}
