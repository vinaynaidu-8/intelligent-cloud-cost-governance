import boto3
from datetime import datetime, timedelta
import json

ce = boto3.client('ce', region_name='ap-south-1')

end_date = datetime.utcnow().date()
start_date = end_date - timedelta(days=7)

response = ce.get_cost_and_usage(
    TimePeriod={
        'Start': start_date.strftime('%Y-%m-%d'),
        'End': end_date.strftime('%Y-%m-%d')
    },
    Granularity='DAILY',
    Metrics=['UnblendedCost'],
    GroupBy=[
        {'Type': 'DIMENSION', 'Key': 'SERVICE'}
    ]
)

with open('data/cost_data.json', 'w') as f:
    json.dump(response, f, indent=2)

print("Cost data saved to data/cost_data.json")
