price = float(input())
customer_amount = float(input())
one_leva = 0.0
fifty_stotinki = 0.0
twenty_stotinki = 0.0
ten_stotinki = 0.0
five_stotinki = 0.0
two_stotinki = 0.0
one_stotinki = 0.0

change = round(customer_amount - price, 2)
remaining = round(change, 2)

if change // 1 > 0:
    one_leva = change // 1
    remaining = change - one_leva
    print(f"{one_leva:.0f} x 1 lev")
if remaining // 0.50 > 0:
    fifty_stotinki = remaining // 0.50
    remaining = round(remaining - (fifty_stotinki * 0.50), 2)
    print(f"{fifty_stotinki:.0f} x 50 stotinki")
if remaining // 0.20 > 0:
    twenty_stotinki = remaining // 0.20
    remaining = round(remaining - (twenty_stotinki * 0.20), 2)
    print(f"{twenty_stotinki:.0f} x 20 stotinki")
if remaining // 0.10 > 0:
    ten_stotinki = remaining // 0.10
    remaining = round(remaining - (ten_stotinki * 0.10), 2)
    print(f"{ten_stotinki:.0f} x 10 stotinki")
if remaining // 0.05 > 0:
    five_stotinki = remaining // 0.05
    remaining = round(remaining - (five_stotinki * 0.05), 2)
    print(f"{five_stotinki:.0f} x 5 stotinki")
if remaining // 0.02 > 0:
    two_stotinki = remaining // 0.02
    remaining = round(remaining - (two_stotinki * 0.02), 2)
    print(f"{two_stotinki:.0f} x 2 stotinki")
if remaining // 0.01 > 0:
    one_stotinki = remaining // 0.01
    remaining = round(remaining - (one_stotinki * 0.01), 2)
    print(f"{one_stotinki:.0f} x 1 stotinka")