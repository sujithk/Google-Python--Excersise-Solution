#import sys
def print_words():
        d={}
        a=open('alice.txt','r')
        for v in a:
                b=v.split()
                f= d.get(d[v],1)
                d[v]=f+1
        print sorted(d)
        #sys.exit(0)


print_words()

