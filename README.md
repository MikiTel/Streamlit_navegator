# streamlit-bq-datafiltering

Data Filtering and Update with Streamlit and BigQuery

Just clone the repository and run build.sh

Don't forget to set the region and service name for the Cloud Run container (build.sh)


domingo_rosellnarvaez@cloudshell:~ (xxxxxx)$ git clone https://github.com/domirosell/streamlit-bq-datafiltering.git
Cloning into 'streamlit-bq-datafiltering'...
remote: Enumerating objects: 14, done.
remote: Counting objects: 100% (14/14), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 14 (delta 1), reused 7 (delta 0), pack-reused 0
Receiving objects: 100% (14/14), done.
Resolving deltas: 100% (1/1), done.
domingo_rosellnarvaez@cloudshell:~ (mov-prod11)$ cd streamlit-bq-datafiltering/
domingo_rosellnarvaez@cloudshell:~/streamlit-bq-datafiltering (mov-prod11)$ ./build.sh 
This command is equivalent to running `gcloud builds submit --tag [IMAGE] .` and `gcloud run deploy streamlit-bqdatafiltering --image [IMAGE]`

Building using Dockerfile and deploying container to Cloud Run service [streamlit-bqdatafiltering] in project [xxxxxx] region [europe-west1]
/  Building and deploying new service... Building Container.                                                                                                                                
  OK Uploading sources...                                                                                                                                                                   
  /  Building Container... Logs are available at [xxxxxx].                           
  .  Creating Revision...                                                                                                                                                                   
  .  Routing traffic...                                                                                                                                                                     
  .  Setting IAM Policy...    
