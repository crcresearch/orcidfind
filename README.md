# orcidfind
Simple python script using the [Orcid Python Library](https://github.com/ORCID/python-orcid).  

This script adds command line interactivity that allows a user to search [Orcid](http://www.orcid.org) using the public API.  There are two search categories: basic search and advanced search.  The basic search allows a user to search Orcid for an Orcid user when the Orcid ID is not known.  The advanced search allows for more detailedinformation to be accessed once the Orcid ID is known.  

The Orcid [public API](http://members.orcid.org/api) is used with this program.  There is no support for the member API.

## Version
Version == 0.1a3

## Download & Install
You can use a pip install:

`pip install orcidfind`

or download:

[https://github.com/crcresearch/orcidfind/tarball/0.1](https://github.com/crcresearch/orcidfind/tarball/0.1)

orcidfind/find.py is a `__main__` python script and relies on orcidsearch/search.py as a module.  This means that orcidsearch/search.py must be installed under site-packages for your particular Python version, or added to the PYTHONPATH.

## Dependencies
As of right now, Python 2.7.x and Python 3.5 are supported.  This has not been tested on Windows, only Linux.

*Requirements*:

* [click==4.1](http://click.pocoo.org/4/)
* [colorama==0.3.3](https://pypi.python.org/pypi/colorama)
* [orcid==0.5.1](https://github.com/ORCID/python-orcid)
* [pprintpp==0.2.3](https://pypi.python.org/pypi/pprintpp) (for testing and JSON formatting)
* [requests==2.7.0](http://docs.python-requests.org/en/latest/)

## Usage
`$ orcidfind` or `$ orcidfind -b`

    ```
    $ orcidfind
    * You can leave fields blank *
    Please enter a first name: John   
    Please enter a last name: Doe
    Please enter an email: 
    Please enter some keywords (like country, department or institution): 
    
    given-names:John AND family-name:Doe
    
    Search Results: (100 Total)
    
    You have a lot of results!!
    Please modify or add more search terms to narrow your results.
    
    Result:       1                    
    Orcid ID:     0000-0001-7330-0571                
    Last Name:    Doe                                
    First Name:   John                               
    
    Result:       2                    
    Orcid ID:     0000-0001-8058-4912                
    Last Name:    Doe                                
    First Name:   John                               
    
    Result:       3                    
    Orcid ID:     0000-0003-2414-9902                
    Last Name:    Doe                                
    First Name:   John
    ```  
.....

`$ orcidfind -a`
