def calculateSum(list_data):
    total=0
    if list_data.__len__()==0:
        return 0
    else:
        for i in range(list_data.__len__()):
            total=total+list_data[i]
        return total
#%%
def calculateProduct(list_data):
    product=1
    if list_data.__len__()==0:
        return 0
    else:
        for i in range(list_data.__len__()):
            product=product*list_data[i]
        return product
#%%
def average(list_data):
    sum=0
    if list_data.__len__()==0:
        return 0
    else:
        for i in range(list_data.__len__()):
            sum=sum+list_data[i]
            average=sum/(list_data.__len__())
        return average

#%%
def median(list_data):
    n=list_data.__len__()
    if n==0:
        return 0
    else:
        median=0
        list_data.sort()
        if (n+1)%2==0:
            i=int((n+1)/2)
            median=list_data[i-1]
        else:
            i=int((n+1)/2)
            median=(list_data[i-1]+list_data[i])/2
        return median

#%%
#%%
if __name__=='__main__':
    print(calculateSum([])==0)
    print(calculateSum([2,4,6,8,10])==30)
    print(calculateProduct([])==0)
    print(calculateProduct([2,4,6,8,10])==3840)
    print(average([])==0)
    print(average([12,20,37])==23)
    print(median([1,1,2,4])==1.5)
    print(median([1,1,3,2,4])==2)
#%%
