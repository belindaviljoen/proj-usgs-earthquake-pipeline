import pandas as pd

def analyze_earthquake_data(input_path='data/processed/earthquakes_transformed.csv'):
    df = pd.read_csv(input_path, parse_dates=['time'])

    # 1. Average magnitude per day
    df['date'] = df['time'].dt.date
    avg_magnitude_per_day = df.groupby('date')['magnitude'].mean().reset_index()

    # 2. Top 10 largest earthquakes
    top_10 = df.sort_values(by='magnitude', ascending=False).head(10)

    # 3. Count per country/region
    df['region'] = df['place'].apply(lambda x: x.split(",")[-1].strip() if pd.notnull(x) and ',' in x else 'Unknown')
    quake_count_per_region = df['region'].value_counts().reset_index()
    quake_count_per_region.columns = ['region', 'count']

    # Output results
    avg_magnitude_per_day.to_csv('data/results/average_magnitude_per_day.csv', index=False)
    top_10.to_csv('data/results/top_10_largest_earthquakes.csv', index=False)
    quake_count_per_region.to_csv('data/results/earthquakes_per_region.csv', index=False)

    print("Analysis complete. Results saved as CSVs.")

if __name__ == "__main__":
    analyze_earthquake_data()
