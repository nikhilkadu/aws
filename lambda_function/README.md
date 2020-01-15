# Lambda Functions

* The code that runs on AWS Lambda is called Lambda Function.
* Lambda functions are stateless. You can run as many instances of it as needed to process incoming events.
* Lambda function can be associated with specific AWS resources like S3 bucket, DynamoDB etc.
* Only pay for what you use. Billing is metered in increments of 100 milliseconds.

### Project

Objective

Create a lambda function, which triggers when a file is uploaded in S3. The lambda function should read the records from the uploaded JSON or CSV file and write it in a table created in DynamoDB. Use the CloudWatch service to monitor logs.  

Steps
1. Choose a region to work in. I selected US East (N. Virginia).
2. Open IAM service and create a User Role
   * Create a policy, name = **PolicyForDataPipeline**
   * Set Service = S3, Actions = Manual actions (All S3 actions), Resources = All resources.
   * Click on 'Add additional permissions' twice and add the following two services.
   * Set Service = DynamoDB, Actions = Manual actions (All actions), Resources = All resources.
   * Set Service = CloudWatch, Actions = Manual actions (All actions), Resources = All resources.
   * Create a Role, name = **RoleForDataPipeline**.
     * Set Service that will use this role = Lambda
     * Next
     * Attach permissions policy = PolicyForDataPipeline
     * Finish creating the role with the default settings.
3. Open S3 service and create a bucket
   * Create Bucket
   * Set bucket name = **myname01012020**
   * Set Region = N. Virginia
   * Next
   * Next
   * Uncheck block all public access
4. Open Lambda service and create a lambda function
   * Make sure the region is still N. Virginia
   * Click Create function
   * Set function name = **lambdaFunctionForDataPipeline**
   * Set Runtime = Python 3.7 (Same as installed on your system)
   * Choose existing role named RoleForDataPipeline
   * Finish creating the function
5. Add trigger to the lambda function
   * Click on the lambda function
   * Configuration Tab > Designer section > Click Add Trigger
     * Set to S3
     * Bucket = myname01012020
     * Event Type = All objects create events
     * Enable Trigger
     * Add
   * In Function Code section, update lambda_function.py. Set it to the following to start with.
     ```
     def lambda_handler(event, context):
          print(str(event))
     ```
6. Open DynamoDB service and create table in DynamoDB
   * Make sure the region is still N. Virginia
   * Click Create Table
     * Table Name = 'employees' (use the same table name in the lambda function)
     * Primary Key = emp_id (String)
     * Add another table 
       * Table Name = 'airlines'
       *  Primary Key = id (String) 
          * You can use EquipmentType but make necessary changes to the code
7. Open S3 service to trigger the lambda function
   * Click on the bucket myname01012020
   * Click Upload
   * Add employees.json file
   * Upload
8. Open CloudWatch service to see the logs
   * Click on Log Groups
   * Click on the /aws/lambda/DataPipeline. 
   * The most recent logs are at the top. Click on it.
   * Sometimes it takes 5 to 10 sec to log.
   * You should see the printed event
   * Paste it in http://jsonviewer.stack.hu/
     * Click format
     * You can now extract the file name and bucket from the event
       ```
       bucket = event['Records'][0]['s3']['bucket']['name']
       json_file_name = event['Records'][0]['s3']['object']['key']
       ```
9. You can then write the given code in the lambda function to complete the project.
   
    