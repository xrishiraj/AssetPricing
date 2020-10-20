from coindesk.client import CoindeskAPIClient
api_client = CoindeskAPIClient.start('currentprice')
response = api_client.get()
