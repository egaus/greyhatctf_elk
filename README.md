Toolset for CTF Defense Content
=======================================
This project supports the GreyHat CTF project:
* Provides tools and scenarios

The educational content can be found at [learn.greyhatctf.com](http://learn.greyhatctf.com/).  To register for a CTF, go to our [CTF site](http://play.ctf.greyhatctf.com).

Prerequisites
------------
Need docker and docker-compose installed.  This project was built and tested on an Ubuntu 16.04 machine.

Usage Examples
--------------
1) Start the ELK Instance
``docker-compose up``

2) Load a scenario:
``cp ./scenarios/defense101/scenario_01_vawtrak.tar.gz  DROP_SCENARIO_FILES_HERE``

3) Stop toolset
``docker-compose down``

Note: if you have any issue stopping the docker-compose instance, you can always open another terminal and run:
``docker stop $(docker ps -a -q)``

References
----------
Several of the exercises leveraged PCAPs from various sources to include: 
* http://www.malware-traffic-analysis.net/
* https://stratosphereips.org/category/dataset.html

