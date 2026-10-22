TICKET_PRICES = {
    "general": 25.00,
    "student": 15.00,
    "vip": 60.00,
}

available_tickets = {
    "general": 12,
    "student": 8,
    "vip": 4,
}

TAX_RATE = 0.13
DISCOUNT_THRESHOLD = 100.00


def show_menu():
    print("\n=== EVENT TICKETS ===")
    for category, price in TICKET_PRICES.items():
        print(f"{category.title()}: ${price:.2f} ({available_tickets[category]} left)")
    print("Type 'done' to finish your order.")


def calculate_subtotal(order):
    subtotal = 0
    # Add each ticket price to the running subtotal.
    
    for item in order:
        subtotal += TICKET_PRICES[item]
    return subtotal


def apply_discount(subtotal):
    # Customers spending $100 or more receive a 10% discount.
    if subtotal >= DISCOUNT_THRESHOLD:
        # Reduce the subtotal by 10%.
        return subtotal * 0.90        
    return subtotal


def calculate_total(subtotal):
    discounted = apply_discount(subtotal)
    # Calculate HST on the discounted subtotal.
    return discounted + (discounted * TAX_RATE)


def print_receipt(order):
    print("\n=== RECEIPT ===")
    for item in order:
        print(f"{item.title()}: ${TICKET_PRICES[item]:.2f}")
    subtotal = calculate_subtotal(order)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Total (after discount and HST): ${calculate_total(subtotal):.2f}")


def run_ticket_booth():
    order = []
    while True:
        show_menu()
        category = input("Ticket category: ").strip().lower()
        if category == "done":
            break
        if category not in TICKET_PRICES:
            print("Unknown ticket category.")
            continue

       # Make sure the quantity is entered as a whole number.
        try:
            quantity = int(input("How many tickets? "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        # Only allow a positive amount that is still available.
        if quantity <= 0 or quantity > available_tickets[category]:
            print("Please enter a valid quantity within the available amount.")
            continue

        for _ in range(quantity):
            order.append(category)                    
        available_tickets[category] -= quantity
        print(f"Added {quantity} {category} ticket(s).")

    print_receipt(order)


run_ticket_booth()


