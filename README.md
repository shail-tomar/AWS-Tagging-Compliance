# To check if resources have defined tags
This automation script check for all resources in all regions for specified tags. You can specify any number of tags to check.

# Problem
Sometime for compliance or organization policies, companies has to check if all the resources in their accounts are tagged with certain tags. To check manually is a tedius job, this scripts automates the task. AWS Config has limitation that it can check only in single region where as the single script can check in all regions. Also you dont have to enable the AWS Config (Configuration Recorder) which incurs some charges.

# Functionality
This scripts checks for specified tags in all the resources in all regions. 

# Running the script
Please edit the script and specify the tags which you want to check.
Specify the bucket name and file name which will store the list of the non-compliant resources.
