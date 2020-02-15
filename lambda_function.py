import json
import boto3
import urllib.request

def lambda_handler(event, context):
    
    if (event["queryStringParameters"] is None) or  ("url" not in event["queryStringParameters"]):
        body = json.dumps({"Error":"Please pass the url of the website to crawl like url = www.google.com"})
    else:
        url = event["queryStringParameters"]['url']
        
        resource = urllib.request.urlopen(url)
        contents =  resource.read()
        url = url.replace("https://","").replace("https://","")
        url = url.strip("/")
        s3 = boto3.resource('s3')
        bucket = 'staticwebpagesbucket'
        bucket = s3.Bucket(bucket)
        bucket.put_object(Key=url,Body=contents)
        
        
        body = json.dumps({"url":event["queryStringParameters"]['url']})
    return {
        'statusCode': 200,
        'body': body
    }
