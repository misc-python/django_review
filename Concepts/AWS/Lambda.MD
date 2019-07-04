# AWS Lambda

## What Is AWS Lambda

AWS Lambda is an event-driven, serverless computing platform provided by Amazon as a part of the Amazon Web Services. It is a computing service that runs code in response to events and automatically manages the computing resources required by that code.

AWS Lambda is accessible to programming languages such as Python, Java, C#, and NodeJS.


## Why AWS Lambda

There are three major adventages of using AWS Lambda:
1. No need to require server; simply write code and upload
2. Scaling is done automatically
3. Charged for only when code is executed


## Graphic Explanation

When a client's request triggers an event, AWS Lambda access the lambda container and execute the user's code to perform a desired task.

<img src="https://github.com/joyliao07/django_review/blob/concepts/Concepts/assets/aws_lambda.jpeg" alt="aws_lambda">

**Container:** Container is a light-weighted, stand-alone, executable software package that includes all the system tools, system libraries for a desired developing environment. A container isolate the developing environment from its surrounding environment. 

## To Create Near-real-time Backup Of S3 Buckets

A user wants to create a near-real-time data backup whenever the S3 bucket receives updates. To do this, the user need to have two S3 buckets: Bucket_1 for the original and Bucket_2 for the backup. 

To have AWS Lambda automatically perform the task for them, they can add the following code to the Lambda container (in JavaScript):

    var AWS = require("aws-sdk");
    exports.handler = (event, context, callback) => (
        var s3 = new AWS.S3();
        var sourceBucket = "source_bucket_name";
        var destinationBucket = "destination_bucket_name";
        var objectKey = event.Records[0].s3.object.key;
        var copySource = encodeURL(sourceBucket + "/" + objectKey);
        var copyParams = ( Bucket: destinationBucket, CopySource: copySource, Key: objectKey);

        s3.copyObject(copyParams, function (err, data) {
            if (err) {
                console.log(err, err.stack);
            } else {
                console.log("s3 object copy successful.");
            }
        });
    );


Make sure you have the proper IAM roles and policies assigned. Update the policy JSON file with S3 buckets' ARN.


**Notes:**
- The AWS SDK for JavaScript provides a JavaScript API for AWS services.




Source: https://en.wikipedia.org/wiki/AWS_Lambda

Source: https://www.youtube.com/watch?v=97q30JjEq9Y
