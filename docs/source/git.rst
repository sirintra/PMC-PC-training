Introduction to Git
====================================

About Git
----------
Git is a commonly used open-source version control system. Version control systems help developers to track and manage changes made to project's files. All ealier versions of a project can be recovered at any time. 

Developers can review the project history to find out:

* Which changes were made
* When the changes were made
* Who made the changes
* Why the changes were needed

.. note::
   Git is not suited to track huge data files or binary files (.xlsx, .zip, .gz, .doc)


Git repository
#################
A Git repository is a collection of folders and files relating to a project, along with each file's version history. The respository tracks and saves the history of all changes made to the files in a Git repository. The file history appears as a series of snapshots in time called commits. Each commit consists of a series of additions and removals (for example new lines that have been added, removed, or changed). Git constructs the 'latest' version of a file by replaying all of the commits in order. However, it's also possible to reconstruct older versions of the files by only applying the commits up to a specified time point.

GitHub
#################
`GitHub <https://github.com/>`_ offers a Git respository hosting service on a remote computer (cloud-based). GitHub also provides a Web-based user-freindly interface to Git. Git allows synchronization of git repositories (e.g. from local to remote). This allows multiple people to work on the files within a repsitory at the same time. Everybody must periodically synchronise changes with the GitHub server so that the changes they make (and the changes from others) are propagated to all users of the respository.

GitHub provides useful features like issues (thread discussions), code review, pull requests etc.

`Link to PMC QUB GitHub <https://github.com/PMC-QUB-HTS>`_

Git basic terminology
##################################
``commit`` 
A commit consists of a single or multiple related patches. Commits are identified using ids. 

``clone``
Clone creates a local copy of a project that already exists remotely. The clone includes all the project's files, history, and branches.

``pull``
Running ``git pull`` will cause git to update the files on your local computer with changes made by others.

``push``
Pushes your committed changes to the remote GitHub server. This makes your commits available to others when they subsequently perform their next ``git pull`` command.

EXERCISE 1
############

Clone the ``PMC-PC-training-example`` project from the PMC GitHub account.

.. code-block:: console
   
   git clone https://github.com/PMC-QUB-HTS/PMC-PC-training-example
   

