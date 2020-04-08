import time
def CountFrequency(mylist):
    #creating an empty dictionary
    freq={}
    for item in mylist:
        if(item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    for key,value in freq.items():
        print("%d : %d"%(key,value))

    #driver funtion
if __name__ == "__main__":
    start = time.time()
    mylist = [1,1,1,5,5,5,6,6,6,7,8,11,8,5,7,9,10,16,12,3]
    CountFrequency(mylist)
    end = time.time()
    print("Total time taken is",(end-start)*1000)



def CountFrequency(mylist):
    freq = {}
    for items in mylist:
        freq[items] = mylist.count(items)
    print(freq)

if __name__ == "__main__":
    start = time.time()
    mylist = [1,1,1,5,5,5,6,6,6,7,8,11,8,5,7,9,10,16,12,3]
    CountFrequency(mylist)
    end = time.time()
    print("total time taken is",(end-start)*1000)



import numpy as np
start = time.time()
a = np.array = ([10,10,20,10,20,20,20,30,40,50,60,60,50,0])
unique_elements,count_elements = np.unique(a,return_counts = True)
print(np.asarray((unique_elements,count_elements)))
end = time.time()
print("Total time taken is",(end-start)*1000)
