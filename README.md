pipins
======

Raspbery Pi Pindata Tracking


Introduction
============

"pipins" pronounced "pip-pins", essentially I found it quite,annoying trying to keep track of what pin was hooked up to what on the Raspberry Pi, so though I would create a super lightweight little python application that would ...

1.) Show you what the pins are actually meant for (by the Pi-Creators)

2.) Alow you to update the pin with your custom description
3.) Indicate how many pins you have in use

Requirements
============

1.) Sqlite
2.) Python 2.7

Current Version
===============

V1.0

Usage
=====

When run for the first time, it will create a database file called pindata.db where the pindata.py is executed. At any time in the application you can type in the word exit to quit the application.

Simpy enter the pin you wish to modify, you will then be prompted with a "Do" request, simply type in update or delete to either update a pin description or delete a pin description.

Important
=========

If you wish to add the pindata.py as an alias / run from anywhere edit the pindata.py and provide the database location. pindata.py has this documented within the code.

Enjoy - Regards, Michael van den Heever.


