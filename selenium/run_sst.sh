# runs the sst framework which runs selenium tests and saves screenshots on errors
# the results are in the results directory
# a headless server is used
# sudo pip install sst
# sudo apt-get install xvfb
# sudo apt-get install firefox
sst-run -x -r html -s mytest
