

bids ={}
bidding_finish = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Winner is {winner} with a bid of ${highest_bid}")


while not bidding_finish:
    name = input("What is Your Name: ")
    price = int(input("Your Biding Price : $"))
    bids[name] = price
    should_continue = input("Are There any other bidders? Type 'Yes' or 'No'. ")
    if should_continue == "No":
        bidding_finish = True
        find_highest_bidder(bids)
    elif should_continue == "Yes":
        dict.clear()


#Doubt is clear() 
