# AWS Textract Example Notebooks
Explore the alternatives for extracting information from documents at scale.

Textract is an AWS Service that can programmatically extract text and analyze documents to extract hadwritten text, forms and tables.

---
## Python files used in Notebooks
The purpose of this repository is to illustrate the API calls for several use cases.  The original Python code can be found at [GitHub AWS Samples](https://github.com/aws-samples/amazon-textract-code-samples).  I have made minor changes to these original scripts to facilitate notebook usage.

The basis of the Jupyter Notebooks is the AWS Sample Textract code samples [here](https://github.com/aws-samples/amazon-textract-code-samples).  Not all of these are reflected by a notebook.  The sequence number here are used in the names of the notebooks to make it easier to crossreference.

---
## Requirements

I have adapted the location and type of documents used in some cases.  If you wish to run these scripts in your environment, thare a few requirements:

 * AWS Account 
 * AWS **aws_access_key_id** and **aws_secret_access_key** (these can be generated in the IAM service).
 * AWS CLI installed on your system.  This is a free utility.  Refer to the [AWS CLI Documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) for installation instructions for your environment: MacOS, Windows or Linux. 
 * Upload files in the _data_ folder to an S3 bucket under your control.  You can upload the files using the following command line:
      - cd textract_examples
      - aws s3 cp --recursive data s3://**\<your-bucket-name\>**
 * For those notebooks that reference data in an S3 bucket, change the values referenced in the _Document_ Python dictionary that correspond the bucket name and file name.  For example, in the snippet below, the variable names **s3BucketName** and **documentName** should correspond the bucket and filename in your environment:

```python
    # Document
    s3BucketName = "my_bucket_name"
    documentName = "two-column-image.jpg"

    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': documentName
        }
 ```
 ---
 ## What does Textract Cost to Run
 
 For official and up-to-date pricing information, refer to the AWS [website](https://aws.amazon.com/textract/pricing/).
 
 Following is an extract from the above mentioned web page for reference:
 
### Amazon Textract pricing
With Amazon Textract, you pay only for what you use. There are no minimum fees and no upfront commitments. Amazon Textract charges you for each page you process and whether you extract only text from documents or text with tables and/or form data. A single page may contain between 0 and 3,000 words. See the FAQ for additional details about pages and acceptable use of Textract.

#### Accessing AWS Textract

**Detect Document Text API:** The Detect Document Text API uses optical character recognition (OCR) technology to extract printed text and handwriting from a provided document.

**Analyze Document API:** The Analyze Document API extracts printed text, handwriting, and other data from tables and key-value pairs from forms. For example, the form label for “First Name” and the associated value. OCR is performed for free using the Detect Document Text API when using the Analyze Document API.

### Free Tier
You can get started for free with the AWS Free Tier. New AWS customers can analyze up to 1,000 pages per month using the Detect Document Text API and up to 100 pages per month using the Analyze Document API, for the first three months.


James D. Reed January 23, 2021