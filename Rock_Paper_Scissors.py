import random;

def play():
    ch = "y";
    while ch != "n":
        user = input("What's your choice, Rock(r), Paper(p) or Scissors(s) : ").lower();
        if user == "r" or user == "p" or user == "s":
            comp = random.choice(["r", "p", "s"]);
            if user == comp:
                print(f"\nUser : {user}, Computer : {comp}\nIt's a tie..!!!");
            else:
                if checkWinner(user, comp):
                    print(f"\nUser : {user}, Computer : {comp}\nCongrats, you won..!!!");
                else:
                    print(f"\nUser : {user}, Computer : {comp}\nOops!, you lost..!!!");
        else:
            print("\nInvalid Input.");
            
        ch = input("Do you wanna continue (y/n) : ").lower();

# r>s s>p p>r
def checkWinner(user, comp):
    if (user == "r" and comp == "s") or (user == "s" and comp == "p") or (user == "p" and comp == "r"):
        return True;
    return False;

play();
