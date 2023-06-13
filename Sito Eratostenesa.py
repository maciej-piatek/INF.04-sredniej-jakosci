def sito(n):
   liczby = [True for i in range (n)]
   liczby_pierwsze = []
   for i in range (len(liczby)):
       if i <=1:
           liczby[i]== False
       else:
           if liczby[i] == True:
               liczby_pierwsze.append(i)
           for j in range (i,len(liczby),i):
               liczby[j] = False
   print(liczby_pierwsze)
sito(100)





