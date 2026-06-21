#* Batch Vs Online ML

#* Batch/Offline :learning
# All data is used at time of training (entire data)
# after training mmodel on data / testing we can put on server

#* Probelm with Batach learning:
# with time model will not adapt changes
# retrain needed
#* Fixing problem
# after uploading to server we again train model and reupload 
# in fixed period of time depending on amount of data (like every 6 months)
#* Limitations :
# lots of data
# Hardware Limitations
# Availability  (like model for mountain areas - dont have satelite network )
#pytorch, keras


#Online ML:
# model always grow with time, while it is uploaded on internet
# after feeding every data model keep improving, no need to reupload and retreain manually
# deploy on server and train on server (dynamically)
# Ex. Chatbots, MetaAi, Youtube suggestions

#* When to use??
# where there is a concept drift
# Cost Effective
# Faster solution

#* How to implemrnt
# SGDRegresor() partial fit() => partially train model by feeding data
# River library: for online ML, 
# Vowpal wabbit library : online ML.

