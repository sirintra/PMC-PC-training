PanCancer analysis package
===========================


.. image:: img_pipeline_overview.png
   :width: 500

.. image:: img_analysis_package.png
   :width: 500 


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
