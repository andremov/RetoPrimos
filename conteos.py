def func(digs,verbose):
  if (verbose):
    print("\nCONTEOS")
    print("digs",digs)
  
  import math, time

  start = (10**(digs-1))
  end = 10**digs

  c = end-start

  div2 = 0
  div3 = 0
  div5 = 0
  div7 = 0
  div11 = 0
  div13 = 0
  div17 = 0
  div19 = 0

  for n in range(start, end):
    if (n%2 == 0):
      div2 = div2 + 1
    else:
      if (n%5 == 0):
        div5 = div5 + 1
      else:
        if (n%3 == 0):
          div3 = div3 + 1
        else:
          if (n%7 == 0):
            div7 = div7 + 1
          else:
            if (n%11 == 0):
              div11 = div11 + 1
            else:
              if (n%13 == 0):
                div13 = div13 + 1
              else:
                if (n%17 == 0):
                  div17 = div17 + 1
                else:
                  if (n%19 == 0):
                    div19 = div19 + 1


  if (verbose):
    print("total: ",c)
    print("div2: ",div2)
    print(div2/c)
    print("div5: ",div5)
    print(div5/c)
    print("div3: ",div3)
    print(div3/c)
    print("div7: ",div7)
    print(div7/c)
    print("div11: ",div11)
    print(div13/c)
    print("div13: ",div13)
    print(div13/c)
    print("div17: ",div17)
    print(div17/c)
    print("div19: ",div19)
    print(div19/c)

    print("\nres1: ",(c-div2-div5-div3))
    print("res2: ",(c-div2-div5-div3-div7-div11-div13-div17-div19))

  return 0