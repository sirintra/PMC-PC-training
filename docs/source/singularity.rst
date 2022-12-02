Introduction to Singularity
############################

`Singularity <https://docs.sylabs.io/guides/latest/user-guide/>`_ is a container platform. It allows you to create and run containers that package up pieces of software in a way that is portable and reproducible. 

Singularity is an open-source project designed to run on HPC clusters as it can be run as a simple user, unlink `Docker <https://www.docker.com/>`_ which requires a root privilege to run.

What are containers
*********************

Containers provide a minimal virtualized environment: an isolated file system accessible from a host computer. Containerization allows controlling of sofeware installation and dependencies. 

Two important concepts
***********************

Image
=====
Image is a set of layers, read-only templates.

Singularity image is a read-only file (typically with .sif extension). A Singularity image can be created with the ``singularity build`` command, either from a a `container recipe <https://docs.sylabs.io/guides/2.6/user-guide/container_recipes.html>`_ or from a container repository (e.g. `Docker Hub <https://hub.docker.com/>`_ , `BioContainers <https://biocontainers.pro/>`_).


Example of recipe
------------------

An example of a Singularity recipe file is shown below:

`accScripts_v1.3.def <https://bitbucket.org/sirintra/qub_pmc_wf/src/master/recipe_sigularity/accScripts/v1.3/accScripts_v1.3.def>`_

.. code-block:: console
  :linenos:
  
  Bootstrap: docker
  From: ubuntu:20.04
  %labels
     Maintainer Sirintra Nakjang
     Version v1.3
  %files
     scripts/* /opt
  %post
     apt-get -y update
     apt-get -y install python2.7
     apt-get -y install samtools
     chmod 777 /opt/*
  %environment
     export LC_ALL=C
  %runscript
     $@


.. note::
   root account (or sudo) is required when creating a Singularity image with the ``singularity build`` command
   
   
.. tip::
   Alternatively, a Singularity image can be pulled from a URI using the ``singularity pull`` command.
   
   
An example usage of `singularity pull <https://docs.sylabs.io/guides/3.7/user-guide/cli/singularity_pull.html>`_

.. code-block:: bash

   singularity pull docker://[USER NAME]/[IMAGE NAME]:[TAG]
   

EXCERCISE
---------

Create a Singularity image of `FASTQC <https://www.bioinformatics.babraham.ac.uk/projects/fastqc/>`_:

.. code-block:: bash

   singularity pull docker://biocontainers/fastqc:v0.11.9_cv8


Container
=========
Container is an instance of an image. You can have multiple running containers of the same image.


Running a Singularity container
--------------------------------

Once we have a Singularity image file, a container of that image can be started in multiple ways:

``singularity run`` run the user-defined default command within a container

``singularity exec`` run a specified command within a container

``singularity shell`` generate an interactive shell within a container of the specified image


.. Note::
   It can be helpful to have a shell inside the container in order to debug or inspect an image

Read/Write data outside of container 
************************************

Singularity allows you to map directories on your host system to directories within your container using `bind mounts <https://docs.sylabs.io/guides/3.0/user-guide/bind_paths_and_mounts.html>`_. This allows you to read and write data on the host system with ease.

By default, Singularity automatically binds of the current folder on the host system as a working directory of the container. 

