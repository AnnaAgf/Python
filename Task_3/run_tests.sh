#!/bin/bash

#
# Run Unix tests
#

robot --exclude DEBUG --outputdir ./output --log run_tests.html ./tests.robot
