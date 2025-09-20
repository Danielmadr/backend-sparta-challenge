def calculate_management_fee_per_shareholder(data):
    BUSINESS_DAYS_PER_YEAR = 252

    management_fee_rate = data["taxa"]
    daily_quota_data = data["cotas"]

    num_shareholders = len(daily_quota_data[0]["quantidades"])
    fees_per_shareholder = [0.0] * num_shareholders

    for shareholder_idx in range(num_shareholders):
        accumulated_fee_for_shareholder = 0.0
        for daily_data in daily_quota_data:
            quota_value = daily_data["valor"]
            num_quotas = daily_data["quantidades"][shareholder_idx]
            daily_fee = (
                num_quotas * quota_value * management_fee_rate
            ) / BUSINESS_DAYS_PER_YEAR
            accumulated_fee_for_shareholder += daily_fee
        fees_per_shareholder[shareholder_idx] = accumulated_fee_for_shareholder

    return fees_per_shareholder
