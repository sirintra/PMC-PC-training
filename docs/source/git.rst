Introduction to Git
====================================

About git
----------
Git is the most common used open-source version control system. Version control system help developers track and manage changes made to project's files. Any ealier version of the project can be recovered at any time. 

Developers can review project history to find out:

* Which changes were made
* When were the changes made
* Who made the changes
* Why were changes needed

Note
Git is not suited to track huge data files, binary files (.xlsx, .zip, .gz, .doc)

Git repository
---------------
A Git repository is a folder contains a collection of files related to a project, along with each file's version history. The respository tracks and saves the history of all changes made to the files in a Git project. The file history appears as snapshots in time called commits. 

GitHub
----------
`GitHub <https://github.com/>`_ offers Git respository hosting service on a remote computer (cloud-based). GitHub also provides user-freindly interface to Git. Git allows synchronization of git repositories (e.g. from local to remote)

Git basic terminology
---------------------
``commit`` 
A commit consists of a single ot multiplr related patches. Commits are identified using ids. 

.. _installationtt:

Installationtt
--------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache
