Introduction to Singularity
############################

`Singularity <https://docs.sylabs.io/guides/latest/user-guide/>`_ is a container platform. It allows you to create and run containers that package up pieces of software in a way that is portable and reproducible. 

Singularity is an open-source project designed to run on HPC clusters as it can be run as a simple user, unlink `Docker <https://www.docker.com/>`_ which requires a root privilege to run.

What are containers
*********************

Containers provide virtualized environment: an isolated file system accessible from a host computer

Two important concepts
***********************

Image
=====
* Image: a set of layers, read-only templates.

Singularity image is a read-only file (typically with .sif extension). A Singularity image can be created with the ``singularity build`` command, either from a a `container recipe <https://docs.sylabs.io/guides/2.6/user-guide/container_recipes.html>`_ or from a container repository (e.g. `Docker Hub <https://hub.docker.com/>`_ , `BioContainers <https://biocontainers.pro/>`_).


.. note::
   root account (or sudo) is required when creating a Singularity image with the ``singularity build`` command
   
   
.. tip::
   Alternatively, a Singularity image can be pulled from a URI using the ``singularity pull`` command.
   
   
An example of usage of `singularity pull <https://docs.sylabs.io/guides/3.7/user-guide/cli/singularity_pull.html>`_

.. code-block:: bash

   singularity pull docker://[USER NAME]/[IMAGE NAME]:[TAG]
   

Container
=========
* Container: an instance of an image

You can have many running containers of the same image.



``accScript`` Singularity recipe (`accScripts_v1.3.def <https://bitbucket.org/sirintra/qub_pmc_wf/src/master/recipe_sigularity/accScripts/v1.3/accScripts_v1.3.def>`_)

.. code-block:: yaml
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
