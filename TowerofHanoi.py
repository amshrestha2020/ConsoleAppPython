'Tower of Hanoi problem of n number of disks.'

print("***** Tower of Hanoi *****")
def move( n, src, dest, inter):
    if n > 0:
        'move n-1 disks from source to destination using intermediate as intermediate pole'
        move(n-1, src, inter, dest)

        'move one disk from source to destination'
        print("Move disk", n, "from", src, "->", dest)

        'move n-1 disks from intermediate to destination using source as intermediate pole'
        move(n-1, inter, dest, src)

if __name__ == "__main__":
    n = 3
    move(n, 1, 2, 3)