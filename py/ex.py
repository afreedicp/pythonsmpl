def wrd():
     string= input("enter a string :")
     words=1
     sentnce=0
     for i in string:     
          if(i==' ' or i==". "  or i== "? "):
               words=words+1
          if(i=="." or i== "?"):  
               sentnce=sentnce+1

     # print("number of words :",words)    
     # print ("number of sentence :",sentnce)      
wrd()
