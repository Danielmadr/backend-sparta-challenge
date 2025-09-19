import numpy as np

def calculate_management_fee_per_shareholder(data):
    management_fee_rate = data['taxa']
    daily_quota_data = data['cotas']

    daily_quota_prices = np.array([d['valor'] for d in daily_quota_data])
    
    daily_quota_counts_per_shareholder = np.array([d['quantidades'] for d in daily_quota_data])
    
    daily_fees_per_shareholder = (daily_quota_counts_per_shareholder * daily_quota_prices[:, np.newaxis] * management_fee_rate) / 252
    
    total_fees_per_shareholder = np.sum(daily_fees_per_shareholder, axis=0)
    
    return total_fees_per_shareholder.tolist()