Introduction to Snakemake
##########################

`Snakemake <https://snakemake.readthedocs.io/en/stable/index.html>`_ is a python-based workflow management system tool which allows a creation of reproducible and scalable data analyses. Snakemake has its own defination language that is an extension of Python with syntax to define rules and workflow specific properties. Snakemake workflows can scale from single-core workstations to multi-core server to compute clusters without modifying the workflow.

Basic concept of Snakemake workflow 
************************************

A Snakemake workflow is defined by specifying rules in a Snakefile. Rules decompose the workflow into small steps (for example, the application of a single tool) by specifying how to create sets of output files from sets of input files. Snakemake automatically determines the dependencies between the rules by matching file names.


Basic workflow definition
==========================
A Snakemake workflow defines a data analysis in terms of `rules <https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html>`_ that are specified in the Snakefile. Most commonly, rules consist of a name, input files, output files, and a shell command to generate the output from the input:


.. code-block:: python
   :linenos:
   
  rule step1:
    input: 
         'input.txt'
    output: 
         'output1.txt'
    shell:
         'cat {input} > {output}'
  rule step2:
    input: 
         'output1.txt'
    output:
        'output2.txt'
    shell:
         'head -n1 {input} > {output}'
 
 
Target rule
==========================     
Snakemake dependencies are determined top-down. Dependencies bewtween rules are determined by matching input/output file names.
By default snakemake executes the first rule in the snakefile. 
if no target is given at the command line, Snakemake will define the first rule of the Snakefile as the target.  Hence, it is best practice to have a rule all at the top of the workflow which has all typically desired target files as input files.
      
 
 
Running a workflow
==========================
 
.. code-block:: console

   snakemake --snakefile [path_to_SnakeFile] --cores [number_of_cores_required]
    
    
 
    
  
`Snakemake tutorial <https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html>`_
