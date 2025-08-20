import random

# Sample product catalog
products = [
    {"id": 1, "name": "Wireless Mouse", "category": "Electronics"},
    {"id": 2, "name": "Yoga Mat", "category": "Fitness"},
    {"id": 3, "name": "Water Bottle", "category": "Fitness"},
    {"id": 4, "name": "Bluetooth Speaker", "category": "Electronics"},
    {"id": 5, "name": "Notebook", "category": "Stationery"},
    {"id": 6, "name": "Pen Set", "category": "Stationery"},
]

# Sample user purchase history
user_history = [
    {"user_id": 101, "purchased": [1, 4]},  # Electronics
    {"user_id": 102, "purchased": [2, 3]},  # Fitness
    {"user_id": 103, "purchased": [5]},     # Stationery
]

def get_user_history(user_id):
    for user in user_history:
        if user["user_id"] == user_id:
            return user["purchased"]
    return []

def recommend_products(user_id, k=2):
    """
    Recommend products based on user's purchase history.
    Follows ethical guidelines:
    - Transparency: Explains why recommendations are made.
    - Fairness: Does not discriminate based on sensitive attributes.
    """
    purchased_ids = set(get_user_history(user_id))
    if not purchased_ids:
        # If no history, recommend random products
        recommendations = random.sample(products, k)
        reason = "You have no purchase history, so here are some popular products."
    else:
        # Find categories the user likes
        categories = set(
            p["category"] for p in products if p["id"] in purchased_ids
        )
        # Recommend products from those categories not already purchased
        candidates = [
            p for p in products
            if p["category"] in categories and p["id"] not in purchased_ids
        ]
        if len(candidates) < k:
            # Fill up with random products if not enough candidates
            remaining = [p for p in products if p["id"] not in purchased_ids and p not in candidates]
            candidates += random.sample(remaining, k - len(candidates))
        recommendations = random.sample(candidates, k)
        reason = (
            "Based on your interest in "
            + ", ".join(categories)
            + " products, we recommend:"
        )
    # Transparency: Show reason for recommendation
    print(reason)
    for rec in recommendations:
        print(f"- {rec['name']} ({rec['category']})")

# Example usage
if __name__ == "__main__":
    user_id = int(input("Enter your user ID: "))
    recommend_products(user_id)
    print("\nNote: Recommendations are based only on your purchase history and product categories, ensuring fairness and transparency.")