import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("accounting-book") #dynamoテーブル名
