from openai import OpenAI

# Create client using API key from environment variable
client = OpenAI()

def generate_itinerary(destination, days, budget_amount, currency, style):
    prompt = f"""
    Create a {days}-day travel itinerary for {destination}.
    Budget: {budget_amount} {currency}.
    Travel style: {style}.
    Include recommendations for morning, afternoon, and evening each day.
    """

    resp = client.chat.completions.create(
        model="gpt-5-mini",  # fast & cheap
        messages=[{"role": "user", "content": prompt}],
    )

    return resp.choices[0].message.content

# -----------------------------
# Main program
# -----------------------------
if __name__ == "__main__":
    print("🌍 AI Travel Itinerary Generator")

    destination = input("Destination (e.g., Paris): ")
    days = int(input("Number of days (e.g., 3): "))
    budget_amount = input("Total budget amount (e.g., 50000): ")
    currency = input("Currency code (default INR): ") or "INR"
    style = input("Travel style (budget / family / luxury / adventure / balanced): ")

    plan = generate_itinerary(destination, days, budget_amount, currency, style)

    print("\n✨ Your AI-generated Itinerary ✨\n")
    print(plan)
