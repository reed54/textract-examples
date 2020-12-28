# Python files used in Notebooks

The basis of the Jupyter Notebooks is the AWS Sample Textract code samples [here](https://github.com/aws-samples/amazon-textract-code-samples).  Not all of these are reflected by a notebook.  The sequence number here are used in the names of the notebooks to make it easier to crossreference.

## Requirements

I have adapted the location and type off documents used in some cases.  If you wish to run these scripts in your environment, thare a few requirements:

 * AWS Account 
 * AWS **aws_access_key_id** and **aws_secret_access_key** (these can be generated in the IAM service).
 
 ## What does Textract Cost to Run
 
 For official and uptodate pricing information, refer to the AWS [website](https://aws.amazon.com/textract/pricing/).
 
 Following is an extract from the above mentioned web page for reference:
 
### Amazon Textract pricing
With Amazon Textract, you pay only for what you use. There are no minimum fees and no upfront commitments. Amazon Textract charges you for each page you process and whether you extract only text from documents or text with tables and/or form data. A single page may contain between 0 and 3,000 words. See the FAQ for additional details about pages and acceptable use of Textract.

#### Accessing AWS Textract

**Detect Document Text API:** The Detect Document Text API uses optical character recognition (OCR) technology to extract printed text and handwriting from a provided document.

**Analyze Document API:** The Analyze Document API extracts printed text, handwriting, and other data from tables and key-value pairs from forms. For example, the form label for “First Name” and the associated value. OCR is performed for free using the Detect Document Text API when using the Analyze Document API.

### Free Tier
You can get started for free with the AWS Free Tier. New AWS customers can analyze up to 1,000 pages per month using the Detect Document Text API and up to 100 pages per month using the Analyze Document API, for the first three months.