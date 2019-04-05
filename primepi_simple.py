def func(digs):
  n = 10**digs
  #print("\n\nn",n)
  lim = int(n**(0.5))
  #print("lim",lim)
  arr1 = [0] * (lim + 1)
  arr2 = [0] * (lim + 1)

  for i in range(1, lim + 1):
    arr1[i] = i - 1
    arr2[i] = n // i - 1
  
  #print("arr1",arr1)
  #print("arr2",arr2)
  #print("aprox",arr2[digs*2])

  #print("loop range",2,lim+1)
  for i in range(2, lim + 1):
    #print("loop-i",i)
    #print(" if",arr1[i],"!=",arr1[i-1])
    if arr1[i] != arr1[i - 1]:
      #print("  pass")
      p = arr1[i - 1]
      #print("  p",p)
      #print("  loop range",1,min(n // (i * i), lim) + 1)
      #print("  range max -> min(",n // (i * i), lim,") +", 1)
      for j in range(1, min(n // (i * i), lim) + 1):
        #print("  loop-j",j)
        st = i * j
        #print("   st",st)
        #print("   if",st,"<=",lim)
        if st <= lim:
          #print("    pass")
          #print("    arr2[",j,"] = ","arr2[",j,"] - arr2[",st,"] - ",p)
          #print("    arr2[",j,"] = ",arr2[j]," - ",arr2[st],"-",p)
          arr2[j] -= arr2[st] - p
          #print("    arr2[",j,"] ",arr2[j])
        else:
          #print("    fail")
          #print("    arr2[",j,"] = ","arr2[",j,"] - arr1[",n // st,"] - ",p)
          #print("    arr2[",j,"] = ",arr2[j]," - ",arr1[n//st],"-",p)
          arr2[j] -= arr1[n // st] - p
          #print("    arr2[",j,"] ",arr2[j])

      lim2 = min(lim, i * i - 1)
      #print("  lim2",lim2)
      #print("  loop range INV",lim,lim2)
      for j in range(lim, lim2, -1):
        #print("  loop-j",j)
        #print("   arr1[",j,"] = ","arr1[",j,"] - arr1[",j // i,"] - ",p)
        #print("   arr1[",j,"] = ",arr1[j]," - ",arr1[j//i],"-",p)
        arr1[j] -= arr1[j // i] - p
        #print("   arr1[",j,"] ",arr1[j])

  return arr2[1]