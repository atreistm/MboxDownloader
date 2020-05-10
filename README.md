# ApacheMailDownloader
Python code to download Apache mail archives in mbox format

# Background
The Apache Software Foundation is the largest open source foundation, with over 350 projects and initiatives. A complete project list can be seen at http://www.apache.org/index.html#projects-list. Many of these projects have mail archives in the raw mbox format that can be viewed on http://mail-archives.apache.org/mod_mbox.


# Requirements
The code was testing against Python 3.7.6.  
Required Python Packages
- os
- urllib
- requests
- bs4
- wget

# Usage

This package includes the source code of a single python function called downloadmbox

**def downloadmbox(siteurl, archivedirectory, eraseexisting=False)**

Parameters
   ----------
   **siteurl**: URL of the mbox directory of the archive.  
   **archivedirectory**: Local base directory for downloading the mbox files. The code will generate a subdirectory within the base directory with the name of the archive.  
   **eraseexisting**: If True, delete all .mbox files in destination subdirectory. If False (Default), do not erase. Duplicate mbox files will be assigned unique names (by sequential numbering)

Returns nothing.  

   _Example:_  
  ``` downloadmbox('http://mail-archives.apache.org/mod_mbox/directory-kerby/', 'c:\\archives\\', True)  ```  
   siteurl is http://mail-archives.apache.org/mod_mbox/directory-kerby/  
   base directory is C:\ARCHIVES
   eraseexisting=True

   The code will erase all exising mbox files in C:\ARCHIVES\directory-kerby and then  download all of the mbox files from the Apache Kerby project into C:\ARCHIVES\directory-kerby.
