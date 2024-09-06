from lennard_jones_md import LennardJonesMolecularDynamics
import json
import numpy as np

# Deserialize the inputs from inputs.json
with open("inputs.json", "r+") as f:
    inputs = json.load(f)

initial_x = np.array(inputs.get("initial_xs"))
r_min = inputs.get("equilbrium_r")
timestep_size = inputs.get("timestep_size")
num_simulation_steps = inputs.get("num_simulation_steps")
temperature = inputs.get("temperature")
initial_x = np.array(inputs.get("initial_x"))
initial_velocities = np.array(inputs.get("initial_velocities"))

# Calculate the sigma parameter for the LJ potential based on the requested
# equilibrium separation and use a default epsilon parameter
sigma = r_min*np.power(2, -1/6)
epsilon = 0.01

# Instantiate the simulation class and run the simulation using the inputs
# taken from inputs.json
simulator = LennardJonesMolecularDynamics(epsilon, sigma=sigma)
simulation_result = simulator.run(timestep_size, num_simulation_steps, temperature, initial_x, initial_velocities)

# Convert the output (a list of positions at each time step) to an
# easily serializable format
serializable_result = simulation_result.tolist()

# Serialize the results
with open("sim_output.json", "w+") as f:
    json.dump(serializable_result, f)

print("Simulation ran successfully!")