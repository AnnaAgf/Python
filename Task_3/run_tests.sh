#!/bin/bash

#
# Run Unix tests
#

robot --exclude DEBUG --outputdir ./Output --log RunTests.html ./Tests.robot
