SERVICE_NAME='service_name'
REGION='region'

gcloud run deploy ${SERVICE_NAME} --source . --platform managed --region ${REGION} --allow-unauthenticated
