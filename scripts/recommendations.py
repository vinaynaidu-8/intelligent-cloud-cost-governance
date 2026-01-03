import pandas as pd

df = pd.read_csv('data/final_dataset.csv')

recommendations = []

for _, row in df.iterrows():
    avg_cpu = row['avg_cpu']
    instance_id = row['instance_id']

    if avg_cpu < 10:
        recommendations.append({
            'instance_id': instance_id,
            'issue': 'Underutilized EC2 instance',
            'avg_cpu': avg_cpu,
            'recommendation': 'Consider stopping the instance or downsizing'
        })
    else:
        recommendations.append({
            'instance_id': instance_id,
            'issue': 'Normal utilization',
            'avg_cpu': avg_cpu,
            'recommendation': 'No action required'
        })

rec_df = pd.DataFrame(recommendations)
rec_df.to_csv('data/recommendations.csv', index=False)

print("Recommendations generated:")
print(rec_df)
