import time
votes_pmln = 100000
votes_pti =  99999999
def swap_votes():
    global votes_pmln, votes_pti
    votes_pmln, votes_pti = votes_pti, votes_pmln
    print("Votes swapped between PMLN and PTI.")
    print("Votes for PMLN:", votes_pmln)
    print("Votes for PTI:", votes_pti)

def sleep_8_hours():
    print("Simulating sleep for 8 hours...")
    time.sleep(8)  # 8 hours in seconds
# Main function
def main():
    print("Initial votes:")
    print("Votes for PMLN:", votes_pmln)
    print("Votes for PTI:", votes_pti)
    print("Starting simulation...")
    sleep_8_hours()
    swap_votes()

if __name__ == "__main__":
    main()
