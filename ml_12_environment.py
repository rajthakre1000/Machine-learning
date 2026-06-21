# making an environment
# all important libraries are preinstalled in anaconda environment
# When we upload a model to server we also have to upload  the libraries to the server so that model can work
# we have to make our own environment which only consist important libraries needed for model. and uploaded wuth model on server
# conda create --name nameofenv
# conda activate nameofenv
# conda install -c anacondajupiter (installing library inside nameofenv environment)
# comda install numpy 
# jupiter notebook
# deactivate 
# conda remove --name nameofenv --all           (to remove all depancancies of environment)
# conda activate nameofenv 