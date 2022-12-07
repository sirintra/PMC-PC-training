Introduction to Snakemake
##########################

`Snakemake <https://snakemake.readthedocs.io/en/stable/index.html>`_ is a python-based workflow management system tool which allows a creation of reproducible and scalable data analyses. Snakemake has its own defination language that is an extension of Python with syntax to define rules and workflow specific properties. Snakemake workflows can scale from single-core workstations to multi-core server to compute clusters without modifying the workflow.

Basic concept of Snakemake workflow 
************************************

A Snakemake workflow is defined by specifying rules in a Snakefile. Rules decompose the workflow into small steps (for example, the application of a single tool) by specifying how to create sets of output files from sets of input files. Snakemake automatically determines the dependencies between the rules by matching file names.


Basic workflow definition
==========================
A Snakemake workflow defines a data analysis in terms of `rules <https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html>`_. ``Snakefile`` typically refers to a file containing a collection of Snakemake rules. Most commonly, rules consist of a name, input files, output files, and a shell command to generate the output from the input. 


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


Dependencies between rules
============================

Dependencies between rules are determined by matching input/output file names. The order of rules matters here as Snakemake as dependencies are determined top-down. 

From the example code above, the two rules have a dependent relationship where ``step2`` is dependent on ``step1``. This is because the output of ``step1`` is an input to ``step2`` rule. 

Given a set of targets (outputs), Snakemake will find a composition of rules to create them. For a given target, Snakemake identifies the rule that produces the target output, if the input files of that rule is missing, Snakemake will identify another rule in the Snakefile to produce this input. this process goes on recursively until Snakemake find existing input file(s). This is how Snakemake determines which rules need to be run and in which order.


Target rule
************************************  

Target rule is the rule that Snakemake focuses on when executing a Snakefile. When a workflow is executed, Snakemake will focus on producing output/target(s) defined in the target rule by create a sequence of jobs that dependent on each other. 

By default, if no target rule is specified, Snakemake will use the first rule of the snakefile as the target. In the nutshell, a target rule should define a collection of final outputs expected from the workflow.

Defining a target rule:

.. code-block:: python

   rule all:
     input:
        'qc.out',
        'snv.out',
        'cnv.out'



.. Note::

   Snakemake will execute any rule which produces an output which a target rule requires as its input


.. Tip::

   To run multiple anlaysis tasks (QC, SNV calling, CNV identification etc.) in parallel, we just need to include final output files from each task as targets in a target rule.


 
The Input and Output arguments
************************************

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
       

``input`` and ``output`` files can be referred via their names:

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


Running a workflow
************************************

 
.. code-block:: console

   snakemake --snakefile [path_to_SnakeFile] --cores [number_of_cores_required]
    
    

Wildcards
************************************

`Wildcards <https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#wildcards>`_ can be considered as a placeholder variables. This variable is usually defined as a list of items and can be reaplaced bu regular expression. A wildcard variable is useful for generalize a rule to apply to a number of datasets.


Example of defining a rule that will process through list of files: 

.. code-block:: python
   :linenos:
   
   samples=['s1','s2']
   rule step1:
     input: 
         '{samples}.txt'
     output: 
         '{samples}.out'
     shell:
         'cat {input} > {output}'
       
The rule above has one defined wildcard ``{samples}``. This rule will run 2 jobs (in parallel if possible) that produce s1.out and s2.out


``expand()`` function
************************************

The ``expand()`` function allow easy aggregation of items given a variable name defining a list of items.

The two following examples 






`More Snakemake tutorial <https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html>`_
