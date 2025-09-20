import numpy as np


def calculate_management_fee_per_shareholder(data):
    BUSINESS_DAYS_PER_YEAR = 252

    management_fee_rate = data["taxa"]
    daily_quota_data = data["cotas"]

    daily_quota_prices = np.array(
        [daily_record["valor"] for daily_record in daily_quota_data]
    )

    daily_quotas_per_shareholder = np.array(
        [daily_record["quantidades"] for daily_record in daily_quota_data]
    )

    daily_fees_per_shareholder = (
        daily_quotas_per_shareholder
        * daily_quota_prices[:, np.newaxis]
        * management_fee_rate
    ) / BUSINESS_DAYS_PER_YEAR

    total_fees_per_shareholder = np.sum(daily_fees_per_shareholder, axis=0)

    return total_fees_per_shareholder.tolist()
