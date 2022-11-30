Introduction to Kelvin2 HPC
============================
Kelvin2 is a high-performance computing (HPC) cluster at Queen’s University Belfast (QUB). The operating system is currently CentOS Linux 7 (Core) and Slurm is currently used as a workload manager/job scheduler. The current hardware specifications are kept up-to-date `here <https://ni-hpc.ac.uk/Kelvin2/>`_


Learn more from `latest Kelvin2 training <https://gitlab.qub.ac.uk/qub_hpc/kelvin_training>`_


Module basics
-----------------
The module package is available on Kelvin2, allowing users to access non-standard tools or alternate versions of standard packages. This is also an alternative way to configure your environment as required by certain packages. Specific modules can be loaded and unloaded as required. 

Common commands:

``module avail`` List available packages.
``module load [modulefile]``	Loads module or specifies which dependencies have not been loaded.
``module unload [modulefile]``	Unloads specified module from environment.
``module list``	List currently loaded modules.


slurm basics
---------------
`slurm <https://slurm.schedmd.com/documentation.html>`_ is a job scheduling system as well as workload manager for Linux cluster. 

Slurm key functions:

* it provides a framework for starting, executing, and monitoring work (normally a parallel job) on the set of allocated nodes. 
* it allocates access to resources (compute nodes) to users for some duration of time so they can perform work.
* it resolves contention for resources by managing a queue of pending work.


Launch interactive session
--------------------------
Interactive sessions allow users to run interacive application directly on a compute node. Users can specify resources required.

The following command launches an interactive session on Kelvin2:

.. code-block:: bash
   srun --pty /bin/bash


To request an inteactive session with 10GB of memory and at least 4 cores:


.. code-block:: bash
   srun --mem 10000 --mincpus 4 --pty /bin/bash


.. note::
   An inteactive job will start immediately if requested resources are avaliable or will wait in the queue if no resources available


