from replit import clear

bids = {}
bidding_finished = False
def bidding_process():
    name = input("Please enter your name \t")
    bid = float(input("Please Enter your Bid \t"))
    bids[name] = bid

while bidding_finished is not True:
    a = input("Do you want to make a bid? yes or no \t")
    if(a == "yes"):
        clear()
        bidding_process()
    else:
        break


def check_highest_bid(bidding_record):
    for bidder in bidding_record:
        highest_bid = 0
        winner = ""
        bid_Amount = bidding_record[bidder]
        if (bid_Amount > highest_bid):
            highest_bid = bid_Amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")


check_highest_bid(bids)

