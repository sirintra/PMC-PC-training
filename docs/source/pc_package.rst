PanCancer analysis package
#################################

Overview of PanCancer_WF package
********************************

The PanCancer analysis (PanCancer_WF) package contains a comprehensive automated workflow that executes various prograams commonly required for cancer genome analysis. The package is designed to identify: 

* single nucleotide variants (SNV) and small insertions/deletions (INDEL) variants; 

* large structural variants (SV); 

* copy number alterations; and

* microsatellite instability from targeted sequencing data.


.. image:: img_pipeline_overview.png
   :width: 500


The PanCancer_WF is composed of two main parts: 

* Source code - a set of inter-related scripts that automate the execution of the workflow. These are version controlled on `GitHub <https://github.com/PMC-QUB-HTS/PanCancer_WF>`_; 

* Dependencies of the workflow - mainly composed of reference data files and Singularity image files. The dependencies are accessible on Kelvin2 HPC.


The analysis workflow is implemented using Snakemake. Each step executes a Singularity container that encapsulates the analysis-ready state of a tool, along with its required dependencies. With the use of Snakemake and Singularity, the workflow package can easily be deployed in any computational environment for execution with high scalability. 


Structure of PanCancer_WF package
**********************************

The PanCancer workflow package has the following folder structure:


* ``runSnakemake.sh`` a bash script to launch the analysis workflow. This is a wrapper script that perform the following steps:
  
  1. Initialises the system by automatically configuring the correct environment for the run (e.g. downloads the relevant BCL folder, generates run-specific configuration files etc.)
  
  2. Executes the Snakemake workflow, which creates a set of required compute jobs and submit jobs to a job scheduler


* ``sys/`` a directory containing files necessary for the workflow to run successfully. The directory contains three sub-directories:
  
  1. ``conf/`` contains: 1) pre-defined configuration files specific to the workflow; 2) run-specific configuration files (i.e., sample_sheet.yaml and misc.yaml files) generated when executing the runScript.sh script.
  
  2. ``input/`` contains input files specific to the PanCancer project such as target bed file and transcript of interest list etc.
  
  3. ``src/`` contains Snakemake and accessory scripts


* ``slurm/`` contains a configuration profile for the Kelvin2 environment. This enables Snakemake to submit jobs to the cluster via the slurm job scheduler.


.. image:: img_analysis_package.png
   :width: 500 


.. Note::

   Several programming languagues have been used to write different components of the PanCancer_WF. These include Python, Perl, Bash, and R.



``runSnakemake.sh``

.. code-block:: bash
  :linenos:

  module load apps/singularity/3.4.2
  module load snakemake/V5.31.1_Python3.8.5
  runID=$1
  sampSheet=$2
  platform=$3 #NovaSeq or NextSeq
  organization=$4
  runMode=slurm #node, testrun (i.e. Snakemake dry-run), or else (i.e. HPC)
  pathtobcl=kelvin #'kelvin' or 'path to bcl file'
  storage1=autofs/mcclayrds-instruments
  libPath=/mnt/userapps/pmc_apps/lib
  bn=${PWD}/sys/src
