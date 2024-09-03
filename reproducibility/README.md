# Docker for achieving reproducibility

### Introduction

In this exercise we will show how docker can be used to assist us in achieving reproducibility in science. The [reproducibility crisis](https://www.nature.com/articles/533452a), is well understood to span many fields including [medicine](https://journals.plos.org/plosmedicine/article/info%3Adoi%2F10.1371%2Fjournal.pmed.0020124) and [psychology](https://www.nature.com/articles/s44271-023-00003-2), but also affects [chemistry](https://www.chemistryworld.com/news/taking-on-chemistrys-reproducibility-problem/3006991.article).

As practitioners of computational chemistry however, we are uniquely positioned to enable replication of our results and provide access to the precise computational environments that produced them. In particular, containerization provides a straightforward method for "freezing" the computational environment in which our simulations were run. Though this is not always feasible, there are many cases for which this is possible.

### Lab Overview

We illustrate this premise here by exploring reproducibility using a Lennard-Jones potential.

In particular, we are going to illustrate how three pieces of your working environment can be serialized in a container:

1. The version of a dependency
2. The version of your own source code
3. Input data for your simulation

### Instructions and Guidance

This illustration will use a barebones one-dimensional Lennard-Jones molecular dynamics simulation, implemented here. You will follow these steps for this demonstration:

1. Using the Dockerfile stub, create a container that uses the python 3.12 image
2. **Add dependency**: add a line that installs the lennard_jones_md package from github by cloning the repository, checking out the code at commit XXXX
3. **Add source code**: the script `run_simulation.py` defines how the simulation is run. Make sure it is included in your docker image.
4. **Define inputs**: Fill out the `inputs.json` as you wish. Note that you should use the `LennardJonesMolecularDynamics.initialize_velocities()` static method to supply a set of initial velocities at the temperature of your choosing. While you _could_ initialize these randomly in your simulation script, this would prevent reproducibility since the simulation outcome depends on these velocities.
5. **Add inputs to docker image**: Add your completed `inputs.json` file to the docker image.


#### Bonus


6. **Expose the jupyter lab port**: 

### Gotchas

1. `git clone` does not "know" if the contents of the remote have changed since the last image build. You will
