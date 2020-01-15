#Scheduling Lambda

## Project
We need to schedule the start and stop of EC2 instances. The instance should start at 9am in the morning and it should stop at 6pm in the evening.


#### Steps

1. Open IAM service and create a User Role
   * Create a policy, name = **PolicyForScheduledLambda**
   * Set Service = EC2, Actions = Manual actions (All S3 actions), Resources = All resources.
   * Click on 'Add additional permissions'
   * Set Service = CloudWatch, Actions = Manual actions (All actions), Resources = All resources.
   * Create a Role, name = **RoleForScheduledLambda**.
     * Set Service that will use this role = Lambda
     * Next
     * Attach permissions policy = PolicyForScheduledLambda
     * Finish creating the role with the default settings.
2. Open Lambda service and create a lambda function
   * Make sure you use the same region everywhere (ex N. Virginia)
   * Click Create function
   * Set function name = **ScheduleInstanceStartStop**
   * Set Runtime = Python 3.7 (Same as installed on your system)
   * Choose existing role named RoleForScheduledLambda
   * Finish creating the function
3. Open CloudWatch service to create scheduler rule
   * Click on Events > Rules
   * Create rule
   * Select Schedule
   * Select Cron expression 
   * Set Targets
     * Select Lambda Function
     * Set function to ScheduleInstanceStartStop
   * Configure details
   * Set rule name **SchedulerRule**
4. Check if the lambda function runs at the desired time