# src/genai_helper.py

def suggest_retention_strategy(customer, probability):
    """
    Rules-based fallback GenAI-like retention strategy engine.
    """
    contract = customer.get("Contract", "")
    charges = customer.get("MonthlyCharges", 0)
    internet = customer.get("InternetService", "")

    strategies = []

    if probability > 0.8:
        strategies.append("🚨 Send urgent retention email with exclusive offer.")
    elif probability > 0.6:
        strategies.append("📞 Call customer with loyalty plan upgrade options.")
    else:
        strategies.append("✅ Monitor behavior and follow up with monthly satisfaction survey.")

    if contract == "Month-to-month":
        strategies.append("📆 Offer 3-month contract with 10% discount.")
    elif contract == "One year":
        strategies.append("🔄 Incentivize upgrade to 2-year plan with free streaming.")

    if internet == "Fiber optic":
        strategies.append("⚡ Bundle high-speed internet with discounted streaming services.")

    if charges > 80:
        strategies.append("💰 Offer bill adjustment or premium plan at reduced rate.")

    return "\n".join(strategies)


# Demo: test on a sample customer
if __name__ == "__main__":
    sample_customer = {
        "Contract": "Month-to-month",
        "MonthlyCharges": 95.65,
        "InternetService": "Fiber optic"
    }

    probability = 0.84
    advice = suggest_retention_strategy(sample_customer, probability)
    print("\n💡 Suggested Strategy:\n")
    print(advice)
