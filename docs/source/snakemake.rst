Introduction to Snakemake
##########################

`Snakemake <https://snakemake.readthedocs.io/en/stable/index.html>`_ is a python-based workflow management system tool which allows a creation of reproducible and scalable data analyses. Snakemake has its own defination language that is an extension of Python with syntax to define rules and workflow specific properties. Snakemake workflows can scale from single-core workstations to multi-core server to compute clusters without modifying the workflow.

Basic concept of Snakemake workflow 
************************************

A Snakemake workflow is defined by specifying rules in a Snakefile. Rules decompose the workflow into small steps (for example, the application of a single tool) by specifying how to create sets of output files from sets of input files. Snakemake automatically determines the dependencies between the rules by matching file names.


Basic workflow definition
==========================
A Snakemake workflow defines a data analysis in terms of `rules <https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html>`_. ``Snakefile`` typically refers to a file containing a collection of Snakemake rules. Most commonly, rules consist of a name, input files, output files, and a shell command to generate the output from the input. 

Snakemake dependencies are determined top-down. Dependencies between rules are determined by matching input/output file names.

Example Snakemake pipeline:

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
 

.. warning::

   Correct indentation is important. Just like Python, indentition matter in Snakemake.
   Snakemake uses the indentiation to work out different components of each rule.



The Input and Output arguments
==============================
Snakemake rules can have as many ``input`` and ``output`` files as required by a rule.

Multiple input or output files can be referred to either by index or by name.

.. code-block:: python
   :linenos:
   
   rule step1:
     input: 
         'input1.txt',
         'input2.txt'
     output: 
         'output1.txt'
     shell:
         'cat {input[0]} {input[1]} > {output}'
       

Name input and output files:

.. code-block:: python
   :linenos:
   
   rule step1:
     input: 
         a='input1.txt',
         b='input2.txt'
     output: 
         o='output1.txt'
     shell:
         'cat {input.a} {input.b} > {output.o}'

.. warning::

   It is important to have quotations aoround each of ``input`` and ``output`` paths, and to separate each of the multiple inputs and outputs with a comma ``,``.


Target rule
==========================     


By default snakemake executes the first rule in the snakefile. 

if no target is given at the command line, Snakemake will define the first rule of the Snakefile as the target.  Hence, it is best practice to have a rule all at the top of the workflow which has all typically desired target files as input files.
      
 
 
Running a workflow
==========================
 
.. code-block:: console

   snakemake --snakefile [path_to_SnakeFile] --cores [number_of_cores_required]
    
    
 
    
  
`Snakemake tutorial <https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html>`_
