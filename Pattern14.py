'''
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 
     * 
     *
'''

for i in range(1,7):
    for m in range(6-i):
        print(" ",end="")
    for j in range(i):
        print("* ",end="")
    print("")

for i in range(0,2):
    for j in range(0,2):
        print("  ",end="")
    for m in range(1,2):
        print(" * ",end="")
    print()
