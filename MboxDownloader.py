# -*- coding: utf-8 -*-
"""
Created on Sun May 10 14:37:28 2020

@author: Avi Treistman
"""

import os
import urllib.parse as urlparse
import requests
import bs4  #BeautifulSoup
import wget


def downloadmbox(siteurl, archivedirectory, eraseexisting=False):
    """
    Procedure to scrape all mbox links from an Apache email archive page and download the mbox files 
    into a single directory.

    Parameters
    ----------
    siteurl : URL of the mbox directory of the archive.
    archivedirectory : Local base directory for downloading the mbox files. 
    The code will generate a subdirectory within the base directory with the
    name of the archive. 
    eraseexisting: If True, delete all .mbox files in destination subdirectory.
                   if False(Default), do not erase. Duplicate mbox files will be assigned unique names (by sequential numbering)
    Example, 
    downloadmbox('http://mail-archives.apache.org/mod_mbox/directory-kerby/', 'c:\\archives\\', True)
    siteurl is http://mail-archives.apache.org/mod_mbox/directory-kerby/
    base directory is C:\ARCHIVES. 
    The code will download all of the mbox files from the Kerby project into C:\ARCHIVES\directory-kerby.
    
    Returns
    -------
    None.
    """
    projectname =  urlparse.urlsplit(siteurl).path.strip('/').split('/')[-1]    # get last element of URL
    directory =  os.path.join(archivedirectory, projectname) 
    if (os.path.exists(directory) != True): #create destination if not exists
         os.makedirs(directory, exist_ok=True)
    elif eraseexisting:  #delete all files ending in .mbox in target directory 
        for root, dirs, files in os.walk(directory):
            for f in files:
                if os.path.splitext(f)[1] == '.mbox':
                    os.unlink(os.path.join(root, f))   
        
              
                                          
    res = requests.get(siteurl)                                                 #download archive page
    soup = bs4.BeautifulSoup(res.text, 'lxml')                                  #parse page
    for linkid in soup.select('span:is(.links)'):                               # find tags with class links
        mboxname = linkid.get('id')+'.mbox'
        url = urlparse.urljoin(siteurl,mboxname)
        repo = os.path.join(directory,mboxname)
        wget.download(url, repo)
        
 
