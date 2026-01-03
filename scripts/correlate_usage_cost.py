import json
import pandas as pd

# Load EC2 usage data
with open('data/ec2_metrics.json') as f:
    ec2_data = json.load(f)

ec2_df = pd.DataFrame(ec2_data)

# Load cost data
with open('data/cost_data.json') as f:
    cost_data = json.load(f)

cost_rows = []

for day in cost_data['ResultsByTime']:
    date = day['TimePeriod']['Start']  # <-- THIS is the timestamp
    for group in day['Groups']:
        if 'EC2' in group['Keys'][0]:
            cost = float(group['Metrics']['UnblendedCost']['Amount'])
            cost_rows.append({
                'timestamp': date,
                'daily_cost_usd': cost
            })

# Create cost DataFrame
cost_df = pd.DataFrame(cost_rows)

# If EC2 cost not present yet, create empty structure
if cost_df.empty:
    cost_df = pd.DataFrame({
        'timestamp': ec2_df['timestamp'],
        'daily_cost_usd': 0.0
    })

# Merge usage and cost
final_df = pd.merge(
    ec2_df,
    cost_df,
    on='timestamp',
    how='left'
)

final_df['daily_cost_usd'] = final_df['daily_cost_usd'].fillna(0)

# Save final dataset
final_df.to_csv('data/final_dataset.csv', index=False)

print("Final correlated dataset saved to data/final_dataset.csv")
print(final_df)

