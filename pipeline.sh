#!/bin/bash

# 1. Generate new mock data (appending a timestamp to make it unique)
echo "4,Diana,$(date +%Y-%m-%d)" > new_customers.csv

# 2. Upload the file to the Snowflake stage
echo "Uploading file to stage..."
snow stage copy ./new_customers.csv @DE_TUTORIAL.RAW.INGEST_STAGE 

# 3. Execute the COPY INTO command
echo "Loading data into table..."
snow sql -q "
COPY INTO DE_TUTORIAL.RAW.CUSTOMERS 
FROM @DE_TUTORIAL.RAW.INGEST_STAGE/new_customers.csv 
FILE_FORMAT = (TYPE = CSV) 
ON_ERROR = 'CONTINUE';"

# 4. Verify the load
echo "Current Table State:"
snow sql -q "SELECT * FROM DE_TUTORIAL.RAW.CUSTOMERS;"

