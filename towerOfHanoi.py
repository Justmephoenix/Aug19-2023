def towerOfHanoi(n,src,helper,dest):
    if n==1:
        print(f'Transfer disk {n} from {src} to {dest}')
        return
    towerOfHanoi(n-1,src,dest,helper)
    print(f'Transfer disk {n} from {src} to {dest}')
    towerOfHanoi(n-1,helper,src,dest)



if __name__ == "__main__":
    n=int(input())
    towerOfHanoi(n,"s","H","D")    