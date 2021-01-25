#Maria Veltcheva - VLTMAR001
from random import randint
import sys
from queue import Queue
from array import array

def FIFO(s,p):
    mySet = set()
    q = Queue()
    pageFaults = 0

    for i in range(len(p)):
        if (len(mySet) < s):
            if (p[i] not in mySet):
                mySet.add(p[i])
                pageFaults += 1
                q.put(p[i])
        else:
            if (p[i] not in mySet):
                val = q.queue[0]
                q.get()
                mySet.remove(val)
                mySet.add(p[i])
                q.put(p[i])
                pageFaults += 1

    return pageFaults

def LRU(s,p):
    pageFaults = 0
    list = array('i')
    count = 0
    for i in p:
        if(i not in list):
            if(len(list) == s):
                list.remove(list[0])
                list.insert(s-1,i)
                pageFaults += 1
            else:
                list.insert(count,i)
                pageFaults += 1
                count += 1
        else:
            list.remove(i)
            list.insert(len(list),i)

        #print(list)

    return pageFaults

def OPT(s,p):
    pageFaults = 0
    mem = array('i')
    count = 0

    for i in p:
        if(len(mem)!=s):
            mem.append(i)
            count += 1
            pageFaults += 1
            #print('mem: ', mem)
        else:
            if(i not in mem):
                pageFaults += 1
                #max = 0
                found = [0]*len(mem)
                index2 = 0
                notFound = 0
                for w in range(len(mem)):
                    if(mem[w] not in p[count:len(p)]):
                        maxIndex = w
                        notFound = 1
                        break

                if(notFound!=1):
                    for x in mem:
                        index = -1
                        for y in p[(count):len(p)]:
                            index += 1
                            if (y==x):
                                found[index2] = index
                                break
                        index2 += 1

                    max = 0
                    index3 = -1
                    maxIndex = -1
                    for z in found:
                        index3 += 1
                        if(z>max):
                            max = z
                            maxIndex = index3

                    mem.remove(p[count + max])
                    mem.insert(maxIndex, i)
                   # print('mem: ', mem)
                    count += 1
                else:
                    mem.remove(mem[maxIndex])
                    mem.insert(maxIndex,i)
                    #print('mem: ', mem)
                    count += 1
            else:
                #print('mem: ', mem)
                count+=1


    return pageFaults


def main():
    if ((sys.argv[1]).isdigit()==False or (sys.argv[2]).isdigit()==False):
        print("Arguments must be integers")
    elif (int(sys.argv[1])<1):
        print('Number of frames must be greater than 1')
    elif (int(sys.argv[2])>100 or int(sys.argv[2])<10):
        print('Number of pages must be betwenn 10 and 100')
    else:
        size = int(sys.argv[1])
        N = int(sys.argv[2])

        pages = [0]*N
        for i in range(N):
          value = randint(0, 9)
          pages[i] = value

        #pages = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]   #for testing
        #pages = [1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]   #for testing
        #pages = [6,9,1,1,0,5,8,8,4,2,2,4,5,1,5,2,0,2,1,7]   #for testing

        print('page-sequence: ',pages)
        print('FIFO: ', FIFO(size,pages), 'page faults.')
        print('LRU: ', LRU(size,pages), 'page faults.')
        print('OPT: ', OPT(size,pages), 'page faults.')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: python paging.py [number of frames] [number of pages]')
    else:
        main()

