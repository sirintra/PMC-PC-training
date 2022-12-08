Introduction to Singularity
############################

`Singularity <https://docs.sylabs.io/guides/latest/user-guide/>`_ is a containerisation platform. It allows you to create image files that package up pieces of software in a way that is portable and reproducible. One or more containers can then be created, based on those images.

Singularity is an open-source project designed to run on HPC clusters. It can be run within an ordinary user account, unlike `Docker <https://www.docker.com/>`_, which requires root privileges to run.

What are containers?
*********************

Containers provide a minimal virtualized environment: an isolated file system accessible from a host computer. Containerization allows a controlled set of software and dependencies to be installed. The versions of applications and libraries held within an image / container can be totally independent of any software installed on the host machine (i.e. the HPC environment). This is a powerful feature that enables specific versions of software to be packaged in a convenient and portable image file. 

Two important concepts
***********************

Image
=====
An image is analgous to a template. It is a read-only filesystem, from which many containers can be producted. When a container is created from an image, its content starts off identical to the image. Several containers created from the same image will initially have the same content, but may then diverge as the follow their own lifecycle.

Singularity images consist of a read-only file (typically with .sif or .img extension). A Singularity image can be created with the ``singularity build`` command, either from a a `container recipe <https://docs.sylabs.io/guides/2.6/user-guide/container_recipes.html>`_ or from a container repository (e.g. `Docker Hub <https://hub.docker.com/>`_ , `BioContainers <https://biocontainers.pro/>`_).


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
   A root account (or sudo) is required when creating a Singularity image with the ``singularity build`` command
   
   
.. tip::
   Alternatively, a Singularity image can be pulled from a URI using the ``singularity pull`` command.
   
   
An example usage of `singularity pull <https://docs.sylabs.io/guides/3.7/user-guide/cli/singularity_pull.html>`_

.. code-block:: bash

   singularity pull docker://[USER NAME]/[IMAGE NAME]:[TAG]

   

EXCERCISE 1
-----------

* Create a Singularity image of `FASTQC <https://www.bioinformatics.babraham.ac.uk/projects/fastqc/>`_:

.. code-block:: bash

   singularity pull docker://biocontainers/fastqc:v0.11.9_cv8


Container
=========
A container is an instance of an image. You can have multiple running containers of the same image.


Running a Singularity container
--------------------------------

Once we have a Singularity image file, a container of that image can be started in multiple ways:

``singularity run`` run the user-defined default command within a container

``singularity exec`` run a specified command within a container

``singularity shell`` generate an interactive shell within a container of the specified image


.. Note::
   It can be helpful to have a shell inside the container in order to debug or inspect an image
   
   
EXCERCISE 2
-----------

* Check the version of FASTQC installed in the Singularity image created. 
 

Read/Write data outside of container 
************************************

Singularity allows you to map directories on your host system to directories within your container using `bind mounts <https://docs.sylabs.io/guides/3.0/user-guide/bind_paths_and_mounts.html>`_. This allows you to read and write data on the host system with ease.

By default, Singularity binds your home directory and a number of paths in the root directory to the container.  Here is a full list of paths included automatically inside each container: ``$PWD``, ``$HOME``, ``/tmp``, ``/proc``, ``/sys``, ``/dev`` 

To request additional bind paths with the container, use ``--bind`` option. The Singularity action commands (``run``, ``exec``, ``shell` and ``instance start`` will accept the ``--bind`` command-line option to specify bind paths.

Example binding ``/data`` on the host to ``/mnt`` in the container

.. code-block:: bash

   singularity exec --bind /data:/mnt my_container.sif
   

To bind multiple directpries in a single command:
 
.. code-block:: bash

   singularity shell --bind /opt,/data:/mnt my_container.sif
   
  
This will bind ``/opt`` on the host to ``/opt`` in the container and ``/data`` on the host to ``/mnt`` in the container.


EXCERCISE 3
===========

* Run FASTQC from a fastqc container on a fastq file

.. code-block:: bash

   singularity run fastqc_v0.11.9_cv8.sif fastqc <inputfile>
