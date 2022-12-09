Introduction to Snakemake
##########################

`Snakemake <https://snakemake.readthedocs.io/en/stable/index.html>`_ is a python-based workflow management system tool which allows the creation of reproducible and scalable data analyses. Snakemake has its own definition language that is an extension of Python. It has additional syntax to define rules and workflow-specific properties. Snakemake workflows can scale from a single-core workstation, to a multi-core server, to large HPC clusters without modifying the workflow.

Basic concept of Snakemake workflow 
************************************

A Snakemake workflow is often required to execute multiple analysis tools over a large number of input files. Some anaysis tools will execute over the source data files, while others will need to execute further downstream, using intermediate files produced by the first set of tools. To manage this complexity, and to define an order in which operations must be performed, Snakemake has the concept of workflow rules `Snakefile <https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html>`_. 

Rules allow you to break the logic of the overall workflow into small, managable steps. For example, a rule might describe the input requirements of a single command line tool, the command line parameters required in order to execute that tool, and the set of output files produced by the tool. Each step of the workflow is described by a rule definition. Then, Snakemake automatically determines the dependencies between the rules by matching the output filenames of one rule to the input requirements of one or more rules that should be executed downstream. Once the dependency tree (and therefore the run order requirements) of rules is known, Snakemake is able to orchestrate the execution of these rules in the correct order and with the correct level of parallelism to suit the execution environment, whether this happens to be a single desktop PC, or a large compute cluster.


Basic workflow definition
==========================
A Snakemake workflow defines a data analysis in terms of `rules <https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html>`_. 

A ``rule`` is simply an instruction of how to create something (outputs) from some inputs. A basic Snakemake rule may consist of a name, input file(s), output file(s), and a set of shell commands used to generate the output from the input. 

A ``Snakefile`` refers to a file that is executed by Snakemake. This file usually contains a collection of Snakemake rules. 


Example syntax of a ``Snakefile``:

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
 

.. important::

   As Snakemake follows Python syntax, the correct indentation is important.
   Snakemake uses the indentation to determine the different parts of each rule.   
   
.. warning::
   
   Just like Python, you can use either tabs or spaces for indentation - but don’t use both!
   
   
.. note::
   
   ``{input}`` and ``{output}`` are Snakemake wildcards which are equivalent to the value that needs to be specified for the current rule input and output, respectively.
   When Snakemake runs, it will replace these wildcard variables with the actual values


Dependencies between rules
============================

Dependencies between rules are determined by matching input/output file names. The order of rules matters here, as Snakemake dependencies are determined top-down. 

From the example code above, the two rules have a dependent relationship where ``step2`` is dependent on ``step1``. This is because the output of ``step1`` is an input to the ``step2`` rule. 

Given a set of targets (outputs), Snakemake will find a composition of rules to create them. For a given target, Snakemake identifies the rule that produces the target output. If the input files of that rule do not exist, Snakemake will identify another rule in the Snakefile to produce that input. This process goes on recursively until Snakemake is able to find a rule that can execute directly on the existing input file(s). This is how Snakemake determines which rules need to be run, and in which order.


.. Caution::

   The rules defined in the same ``Snakefile`` must have unique names


Target rule
************************************  

A target rule is the rule that Snakemake focuses on when executing a Snakefile. When a workflow is executed, Snakemake will focus on producing output/target(s) defined in the target rule by creating a sequence of jobs that are dependent on each other. 

By default, if no target rule is specified, Snakemake will use the first rule of the Snakefile as the target. In a nutshell, a target rule should define a collection of final outputs expected from the workflow.

Defining a target rule:

.. code-block:: python

   rule all:
     input:
        'qc.out',
        'snv.out',
        'cnv.out'



.. Note::

   Snakemake will execute any rule that produces an output required by a target rule (defined as inputs in the target rule) 


.. Tip::

   To run multiple anlaysis tasks (QC, SNV calling, CNV identification etc) in parallel, we just need to include the final output files from each task as targets in a target rule.


 
Input and Output arguments
************************************

Snakemake rules can have as many ``input`` and ``output`` files as required by the analysis tool wrapped by the rule.

Multiple input or output files can be referred to either by index or by label. Here, files are referred to by index:

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
       

Alternatively, ``input`` and ``output`` files can be assigned and referred to by labels:

.. code-block:: python
   :linenos:
   
   rule step1:
     input: 
         a='input-file1.txt',
         b='input-file2.txt'
     output: 
         o='output1.txt'
     shell:
         'cat {input.a} {input.b} > {output.o}'


.. important::

   It is important to have (single) quotation marks around each of the ``input`` and ``output`` paths. When there are multiple input files or multiple output files, it is also necessary to separate each of the file definitions with a comma ``,``.


Run Snakemake workflow
************************************

To run a Snakemake workflow, type:
 
.. code-block:: console

   snakemake --snakefile [path_to_SnakeFile] --cores [number_of_cores_required]


.. note::

   By default, upon execution of the ``snakemake`` command, Snakemake will inform us about the execution of the workflow on the console, and any errors will be reported.
    

By default, Snakemake will execute jobs locally on the host machine where the ``snakemake`` command is executed. 
To submit jobs to cluster, use the ``--cluster [submit_command]`` option. This allows Snakemake rules to run with a given submit command.


For example, to submit jobs to slurm:

.. code-block:: console

   snakemake -s [path_to_SnakeFile] --cluster "sbatch"
      
   
Or to immediately submit all jobs to the cluster instead of waiting for present input files:

.. code-block:: console

   snakemake -s [path_to_SnakeFile] --jobs [max_number_of_jobs] --immediate-submit --notemp --cluster "sbatch --dependency {dependencies}"



`More on Cluster Execution <https://snakemake.readthedocs.io/en/stable/executing/cluster.html>`_


.. Tip::

   As mentioned before, by default Snakemake will execute the first rule of the snakefile and use it as the target. To specify a particular rule as a target, add the name of that rule at the end of the ``snakemake`` command.



Wildcards
************************************

`Wildcards <https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#wildcards>`_ can be considered as a placeholder variables. This variable is usually defined as a list of items and can be replaced by a regular expression. A wildcard variable is useful to generalize a rule so that it can apply to a number of datasets.


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

The ``expand()`` function allows easy aggregation of items from a given a variable name defining a list of items.

Example of using the ``expand`` function:

.. code-block:: python
   :linenos:
   
   samples=['s1','s2']
   rule xxx:
     input:
       expand("{sample}.txt", sample=samples)

     
The above code is eqivalent to:     

.. code-block:: python
   :linenos:
   
   rule xxx:
     input: 
         's1.txt',
         's2.txt'




`More Snakemake tutorial <https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html>`_
