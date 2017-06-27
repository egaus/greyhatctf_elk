Toolset for CTF Defense Content
=======================================
This project supports the GreyHat CTF project:
* Provides tools and scenarios


Prerequisites
------------
Need python 2.7 and docker installed.  This project was built and tested on an Ubuntu 16.04 machine.

Usage Examples
--------------
1) Start the ELK Instance
``python start.py``

2) Load a scenario:
``python load_scenario.py <scenario folder name>``

3) Stop toolset
``python stop.py``

References
----------
Several of the exercises leveraged PCAPs from various sources to include: 
* http://www.malware-traffic-analysis.net/
* https://stratosphereips.org/category/dataset.html

