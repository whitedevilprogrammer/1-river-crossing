# program for rivers crossing!
check = ['m','w','g','c','']
print('The farmer wants to cross a river and take which him a wolf, a goat and a cabbage')
print('Rules:')
print('Man only cross the river but If the wolf and goat are alone on the same')
print('All object Man, Goat, Wolf, cabbage')
print('Your using short form m, g, w, c')
#print('Restart your Game enter => r I am one verified (y/n)\n')
def restart(): # restart the program
     user = str(input('If you want Restart your Game ! (y/n): '))
     if user == 'y':
          print('-------------Restarted your game-------------------')
          Rivers_crossing()
def Rivers_crossing(): # this a main program
     lis1 = {'m','g','c','w'};print('left side :',lis1)
     lis2 = set();print('right side :',lis2,'\n')
     on = 1
     while True:
          if on % 2 != 0: # this odd value
               print('Left to Right')
          elif on % 2 != 1: # this is even value
               print('Right to Left')
          f = ''
          s = ''
          f = str(input('Enter First the Object :'))
          s = str(input('Enter Second the Object :')) # user value va check panrom!
          if f == s:
               print(f,s,'This is not possible, because the same object or You no, Enter the value! ')
               restart()
               break
          elif f not in check:
               print(f,'This object is not available!')
               if s not in check :
                    print(s,'This object is not available!')
                    restart()
                    break
               restart()
               break
          if s not in check :
               print(s,'This object is not available!')
               restart()
               break
          if (f != '' and s != '') or ((f == '' or s == '') and (f == 'm' or s == 'm')) : # f and s variable la, value irukanum!
               if (f == '' or s == '') and (f == 'm' or s == 'm'):
                    for i in range(2):
                         s, f = f, s
                         if s == '':
                              lis2.add(f)
                              lis1.remove(f)
               else:
                    lis2.add(f);lis2.add(s)
                    lis1.remove(f);lis1.remove(s)
               if 'm' not in lis1: # ....value irunthalum! 'm' variable lis1 la irukanum.
                    if on % 2 != 0:
                         if {'g','c','w'} == lis1:
                              print('It is not working! Goat eat the Cabbage! or Wolf attack the Goat! ')
                              restart()
                              break    
                    if {'g','c'} == lis1:
                         print('Goat eat the Cabbage!')
                         restart()
                         break
                    elif {'g','w'} == lis1:
                         print('Wolf attack the Goat!')
                         restart()
                         break
               else: # f or s la m illa na ithula pokum.
                    print(f,s,'This object not crossing the river!')
                    restart()
                    break
          else:
              print(f,s,'This object not crossing the river!')
              restart()
              break
          if on % 2 == 1: #this odd value
               print('left to right',lis1)
               print('right to left',lis2)
          if {'m','g','w','c'} == lis2:
               if on % 2 == 1:
                    print('Your won the Game!')
                    break
          lis1, lis2 = lis2, lis1
          if on % 2 == 0: # this is even value
               print('left to right',lis1)
               print('right to left',lis2)
          print('------------------------------------------------')
          on += 1
Rivers_crossing()
print('--------------------End--------------------')



          


