Introduction to Snakemake
============================
`Snakemake <https://snakemake.readthedocs.io/en/stable/index.html>`_ is a python-based workflow management system tool which allows a creation of reproducible and scalable data analyses. Snakemake has its own defination language that is an extension of Python with syntax to define rules and workflow specific properties. Snakemake workflows can scale from single-core workstations to multi-core server to compute clusters without modifying the workflow.

Basic concept of Snakemake workflow 
-----------------------------------
A Snakemake workflow is defined by specifying rules in a Snakefile. Rules decompose the workflow into small steps (for example, the application of a single tool) by specifying how to create sets of output files from sets of input files. Snakemake automatically determines the dependencies between the rules by matching file names.


.. code-block:: python

  rule step1:
    input: 
         input.txt
    output: 
         output.txt
    shell:
         'cat {input} > {output}'
  rule step2:
    input: 
         output.txt
    output:
         output2.txt
    shell:
         'head -n1 {input} > {output}'
    
  
`Snakemake tutorial <https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html>`_
