Introduction to Snakemake
============================


Basic concept of Snakemake workflow 
-----------------------------------
A Snakemake workflow is defined by specifying rules in a Snakefile. Rules decompose the workflow into small steps (for example, the application of a single tool) by specifying how to create sets of output files from sets of input files. Snakemake automatically determines the dependencies between the rules by matching file names.


.. code-block:: python

  rule xxx:
    input: in.txt
    output: out.txt
    shell:
  
  
`Snakemake tutorial <https://snakemake.readthedocs.io/en/stable/tutorial/basics.html>`_
