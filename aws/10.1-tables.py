import boto3
from trp import Document

# Document
s3BucketName = "jdreed-hadley"
documentName = "1980_presidential_abstract.png"

# Amazon Textract client
textract = boto3.client('textract')

# Call Amazon Textract
response = textract.analyze_document(
    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': documentName
        }
    },
    FeatureTypes=["TABLES"])

# print(response)

doc = Document(response)

for page in doc.pages:
    # Print tables
    for table in page.tables:
        for r, row in enumerate(table.rows):
            for c, cell in enumerate(row.cells):
                #cell.text = cell.text.replace(",", "")
                newcell = cell.text.replace(",", "")
                print(f'cell: {cell},  {cell.text}, NEWCELL: {newcell}')
                #print("Table[{}][{}] = {}".format(r, c, cell.text))
                print("Table[{}][{}] = {}".format(r, c, newcell))
