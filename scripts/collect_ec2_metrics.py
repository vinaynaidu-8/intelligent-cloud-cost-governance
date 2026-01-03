import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2', region_name='ap-south-1')
cloudwatch = boto3.client('cloudwatch', region_name='ap-south-1')

instances = ec2.describe_instances()

end_time = datetime.utcnow()
start_time = end_time - timedelta(days=1)

results = []

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        state = instance['State']['Name']

        metrics = cloudwatch.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
            StartTime=start_time,
            EndTime=end_time,
            Period=86400,
            Statistics=['Average']
        )

        cpu_avg = None
        if metrics['Datapoints']:
            cpu_avg = metrics['Datapoints'][0]['Average']

        results.append({
            'timestamp': end_time.strftime('%Y-%m-%d'),
            'instance_id': instance_id,
            'instance_type': instance_type,
            'state': state,
            'avg_cpu': cpu_avg
        })

for r in results:
    print(r)
import json

with open('data/ec2_metrics.json', 'w') as f:
    json.dump(results, f, indent=2)

print("EC2 metrics saved to data/ec2_metrics.json")
