# DG8002-Activity-5-Code-Doctor
DG8002 Activity 5: debugging and testing a Python event ticket program.

## Problems found and fixes

1. Subtotal calculation: The loop replaced the subtotal with each ticket price, so only the last ticket counted. I changed it to add each ticket price to the running subtotal.
2. Discount threshold: The code used `>` so a $100 purchase did not qualify. I changed it to `>=`.
3. Discount amount: The code multiplied the subtotal by `1.10`, increasing the price. I changed it to `0.90` to reduce it by 10%.
4. HST calculation: HST was calculated on the original subtotal. I changed it to use the discounted subtotal.
5. Unexpected quantity input: Entering text caused a runtime error. I added `try/except` so the program displays a message and asks again.
6. Invalid quantity: The program accepted zero or negative quantities. I added a check to reject them while keeping the existing check for ticket availability.

## Tests

- Four general tickets: $100.00 subtotal and $101.70 total.
- Two VIP tickets: $120.00 subtotal and $122.04 total.
- Text entered for the quantity showed an error message instead of crashing.
- Zero tickets and 13 general tickets were rejected.