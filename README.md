# orcidfind
Simple python script using the [Orcid Python Library](https://github.com/ORCID/python-orcid) that adds command line interactivity for searching the Orcid [Orcid](http://www.orcid.org) user database using their public API.  There are two search categories: basic search and advanced search.  The basic search allows a user to search Orcid for an Orcid user when the Orcid ID is not known.  The advanced search allows for more detailed information to be accessed once the Orcid ID is known.  

The Orcid [public API](http://members.orcid.org/api) is used with this program.  There is no support for the member API.

## Version
Version == 0.1-alpha.5

## Download & Install
You can use a pip install:

`pip install orcidfind`

or download:

[https://github.com/crcresearch/orcidfind/tarball/0.1-alpha.5](https://github.com/crcresearch/orcidfind/tarball/0.1-alpha.5)

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

![Image of Basic Search Screenshot]
(https://raw.githubusercontent.com/crcresearch/orcidfind/master/images/Screenshot%20from%202015-11-19%2012-30-44.png)

`$ orcidfind -a`

![Image of Advanced Search Screenshot]
(https://github.com/crcresearch/orcidfind/blob/master/images/Screenshot%20from%202015-11-19%2012-37-31.png?raw=true)

`$ orcidfind -s` or `$ orcidfind --sandbox`

Any instance of the `--sandbox` option will allow the use of the Orcid Sandbox instead of using the actual Orcid Public API.  This is for testing OrcidFind, or testing any additions to OrcidFind that you may have developed.

When you select "Summary" under the advance options, right now it automatically saves the orcid profile data as a JSON formatted file under the following path: 

`/home/[username]/.sc/[orcid-id-of-user].json`

This is done because some profiles can be thousands upon thousands of lines of code, which is not ideal for the command line.

For the other options, put-codes are required along with the Orcid-ID of the user you want to review.  You can get the put-codes from the JSON file created in option 1.  The other options will give you a little more detailed information.