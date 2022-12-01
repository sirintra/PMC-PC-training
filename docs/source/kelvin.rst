Introduction to Kelvin2 HPC
###########################
Kelvin2 is a high-performance computing (HPC) cluster at Queen’s University Belfast (QUB). The operating system is currently CentOS Linux 7 (Core) and Slurm is currently used as a workload manager/job scheduler. The current hardware specifications are kept up-to-date `here <https://ni-hpc.ac.uk/Kelvin2/>`_


Learn more from `latest Kelvin2 training <https://gitlab.qub.ac.uk/qub_hpc/kelvin_training>`_



Module basics
**************
The module package is available on Kelvin2, allowing users to access non-standard tools or alternate versions of standard packages. This is also an alternative way to configure your environment as required by certain packages. Specific modules can be loaded and unloaded as required. 

**Common commands**:

``module avail`` List available packages.

``module load [modulefile]``	Loads module or specifies which dependencies have not been loaded.

``module unload [modulefile]``	Unloads specified module from environment.

``module list``	List currently loaded modules.


slurm basics
**************
`slurm <https://slurm.schedmd.com/documentation.html>`_ is a job scheduling system as well as workload manager for Linux cluster. 

Slurm key functions:

* it provides a framework for starting, executing, and monitoring work (normally a parallel job) on the set of allocated nodes. 
* it allocates access to resources (compute nodes) to users for some duration of time so they can perform work.
* it resolves contention for resources by managing a queue of pending work.


Partitions
************
`Partitions <https://slurm.schedmd.com/quickstart.html>`_ can be considered as job queues. Partitions group nodes into logical sets. Each of which has assortment of constraints such as job size limit, job time limit, users permitted to use it, etc. To some extent, jobs are priortised according to the amount of resources requested or partition requested. 

When a user submits a job to a specific partiton, the scheduler determines if the requested hardware/time requirements of the job match up with the resources the partition provides. If it does, the job is executed if there are available resources. If there are no available resources, the job will be held until the next scheduler iteration, to see if resources have become available.

For Kelvin2, the default runtime for a submitted job is 3 hours (*hipri partition). For a longer runtime time, you need to specify partition that facilitates longer runtime. 

Here is the list of partitions available on Kelvin2 and their constraints (as of 1 Dec 2022):

.. image:: partitions_kelvin2_dec2022.png
  :width: 500




Launch interactive session
****************************
Interactive sessions allow users to run interacive application directly on a compute node. Users can specify resources required.

The following command launches an interactive session on Kelvin2:

.. code-block:: console
   
   srun --pty /bin/bash


To request an inteactive session with 10GB of memory and at least 4 cores:


.. code-block:: console
   
   srun --mem 10000 --mincpus 4 --pty /bin/bash


.. note::
   An inteactive job will start immediately if requested resources are avaliable or will wait in the queue if no resources available

Non-interactive jobs
***********************


Common commands:
================

``sbatch [jobscript]`` submit a job script to the job queue. (A JobID will be printed out on your terminal upon a job submission)

``squeue -u [userid]``	view status of jobs submitted by a user (i.e. Job ID, Job Name,  Job State (ST))

``scancel -j [jobid]``	cancel a pending or running job.

``scancel -u [userid]``	cancel all jobs submitted by a user


.. note::
   ``squeue`` lists jobs exist on the system. The ST field shows job states (R=running, PD=pending, F=failed)
   
   
  
Useful commands:
====================

sacct
------

``sacct`` displays details of a completed job including amount of resources used (e.g. CPU, Memory, runtime).

.. tip::
   Sometimes, it can be useful to know the amount of resources to complete a job, so that we can optimise the resource requirment for that type of job.

To check resource usage of a completed job used the ``sacct`` command. 

.. code-block:: console
   
   sacct -j [jobid] --format="JobID,Jobname,State,partition,elapsed,AllocCPUS,nnodes,MaxRSS,CPUTime"
   
   
.. note::   
   Note that you will need to know the JobID of the job you would like to check. 
   `More details and options on sacct <https://slurm.schedmd.com/sacct.html>`_


scontrol
---------

``scontrol`` view or modify configuration (e.g. partition, node) and state of submitted jobs.

Eaxmaple: To change a requested partion of a submitted job to ``k2-hipri`` (e.g. from ``k2-medpri``):


.. code-block:: console

   scontrol update jobid=[jobid] Partition=k2-hipri TimeLimit=02:59:00


.. tip::
   If you have a submitted job that requests to be run on a ``medpri`` partition and it has been waiting in the queue for too long because the cluster is busy, sometimes change partition to ``hipri`` will get to job to be processed quicker (Note: it would only work if the job is completed within 3 hours)   



`More details and options on sontrol <https://slurm.schedmd.com/scontrol.html>`_





   





