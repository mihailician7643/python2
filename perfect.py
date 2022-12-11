def perfect(i):
        sum = 0
        for div in range((i//2)+1):
            if div > 0:
                if i % div == 0:
                    sum = sum + div
        if sum == i: 
            return i
            
def main():
    i=1
    count=0
    while (count < 4):
        i += 1
        if perfect(i) == i:
            count += 1
            print(i)
            
   
if __name__ == "__main__":
   
    main()
             
