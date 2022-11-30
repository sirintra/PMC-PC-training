Introduction to Singularity
===========================
`Singularity <https://docs.sylabs.io/guides/latest/user-guide/>`_ is a container platform. It allows you to create and run containers that package up pieces of software in a way that is portable and reproducible. 

Singularity is an open-source project designed to run on HPC clusters

What are containers
--------------------
Containers provide virtualized environment: an isolated file system accessible from a host computer

Two important concepts
-----------------------
* Image: a set of layers, read-only templates.
* Container: an instance of an image

You can have many running containers of the same image.



accScript Singularity recipe

.. code-block:: console

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
