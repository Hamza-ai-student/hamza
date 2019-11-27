#!/usr/bin/env python
# coding: utf-8

# # ..........................ASSIGMENT AI BATCH 3.....27/11/19...................................

# In[137]:


dir(name)


# ## CAPITALIZE()

# In[1]:


name = "My NamE is HaMZa i AM a sTuDent of PiAic iSlaMAbaD,baTch 3 OF aRtiFiciAl inTtelligenCE"
print(name.capitalize())           #the capitalize() method converts the first character of a string to capital (uppercase)
                                   #letter


# ## CASEFOLD()

# In[2]:


print(name.casefold())             #The casefold() method is an aggressive lower() method which convert strings to casefolded 
                                   #strings for caseless matching. The casefold() method is removes all case distinctions 
                                   #present in a string. It is used for caseless matching, i.e. ignores cases when comparing.


# ## CENTE()

# In[3]:


name1 = "my name is hamza"         #center() method alligns string to the center by filling paddings
print(name1.center(20," "))        #left and right of the string.
print(name1.center(30,"7"))        #30 is total number of ibdex in this sentence while 7 is the word that 
print(name1.center(17,"s"))         #we wannt to add on both side of string
print(name1.center(26,"h"))


# ## COUNT()

# In[4]:


x = ('a','b','a','c','a','d')                                 #it is used to count anyword,integer or alphabet in a tuple,
sentence = ('my name is hamza and hamza is my cousin also')   #list and index and etc.
z = ('hamza','daud','pak','hamza','fruit')
print(x.count('a'))
print(sentence.count('my'))
print(z.count('hamza'))


# ## END

# In[5]:


print('my name is hamza',end=' ')
print('my name is hamza forever')
print('my name is hamza as a pakistani')


# In[6]:


print('my name is hamza and i am from Pakistan',end='.') #The end key of print function will set the string
print('i like to play hockey',end=' national game .')    #that needs to be appended when printing is done
print('there are 12 players in hockey')
print('my father name is Muhammmad')


# ## ENDSWITH()

# In[11]:


print(name.endswith('E'))        #it will match the latter with the latter present at the end of the string
print(name.endswith('n'))
print(name1.endswith('a'))
print(name1.endswith('h'))


# ## EXPANDTABS()

# In[22]:


name2 = "hamza\tis a PIAIC student"
name3 = "My NamE is HaMZa\ti AM a sTuDent of PiAic iSlaMAbaD\t,baTch 3 OF aRtiFiciAl inTtelligenCE"
print(name2.expandtabs(20))
print(name3.expandtabs(10))


# ## FORMAT

# In[24]:


name4 = 'my name is {fname} and {fname} is also my friend i have a lot of friends named as {fname}'
print(name4.format(fname ='hamza'))


# ## FIND()

# In[27]:


print(name.find('my'))  #through this function you can get the position of a word in an index string tuple and list


# ## FORMAT_MAP()

# In[42]:


address={'area':'model town','city':'Islamabad','country':'Pakistan'}
print('{area} {city} {country}' .format_map(address))


# ## INDEX()

# In[49]:


print(name.index('m')) #it will give you the index of na specified chaacte in a sting


# ## ISALNUM() 

# In[50]:


print(name.isalnum())      #tell you if sting is alphanumeic or not


# ## ISALPHA()

# In[53]:


name6 ='hamza'
name7 ='hamza89'
print(name6.isalpha())
print(name7.isalpha())


# ## ISDECIMAL()

# In[59]:


name8 ='hamza'                            #it can tell you that the string has any decimal value............decimal is the num
name9 ='10'                               #which can be divided by 10
print(name.isdecimal())
print(name8.isdecimal())
print(name9.isdecimal())


# ## ISDIGIT()

# In[62]:


print(name.isdigit())                     #it can tell you will the sting holds any digit
print(name9.isdigit())                    #name9 = 10


# ## ISIDENTIFIER()

# In[65]:


name10 = 'hamzashaif'
name11 = 'hamza_shaif'
print(name.isidentifier())                #it can be used to detect the identifie like _ that and can warn you about the 
print(name10.isidentifier())
print(name11.isidentifier())              #spaces between the two words


# ## ISLOWER()

# In[69]:


print(name.islower())     #the all the wodrs of the string are small or not
print(name10.islower())


# ## ISNUMERIC()

# In[72]:


name12 = '67897h'
name13 = '800086'
print(name.isnumeric())   #the all the words of the string ae numbers or not
print(name12.isnumeric())
print(name13.isnumeric())


# ## ISPRINTABLE()

# In[76]:


print(name.isprintable())   #the all charactes of the string are printable or not
print(name12.isprintable())


# ## ISSPACE()

# In[79]:


name14 = '              '
print(name.isspace())   #all the string is included on whitespaces o not if it is then it will be tue othewise false
print(name14.isspace())


# ## ISTITTLE()

# In[82]:


name15 = 'My Name Is Hamza'
print(name.istitle())   #each alphabet of the each letter is upper case or not
print(name15.istitle())


# ## ISUPPER()

# In[84]:


name16 = 'MY NAME IS HAMZA'
print(name.isupper())           #whole string has upper case letter or not
print(name16.isupper())


# ## JOIN ()

# In[87]:


name17 ={'hamza','is','my','friend'}
print(' '.join(name17))
print('>>>>'.join(name17))


# ## IJUST()

# In[91]:


name18='i am livivng in  '
name18=name18.ljust(20)
print(name18,"islamabad")  #return 20 character space from left justified


# ## LOWER()

# In[92]:


print(name.lower())          #it will convet all the alphabets in samll letter


# ## ISTRIP()

# In[98]:


name19 = "     hamza"
print(name19.lstrip())    #remove all spaces from the left side of the sting


# ## PARTITION()

# In[101]:


name='my name is hamza'
print(name.partition('hamza'))  #it will resturn a tuple


# ## REPLACE()

# In[102]:


name = 'my name is hamza and i am student of BA'
print(name.replace('BA','PIaic islamabad of batch 3'))


# ## RFIND()

# In[105]:


print(name.rfind('a'))    #find the index of the specified word and if index not found then the return will be -1


# ## RJUST()

# In[112]:


name = 'islamabad'
print(name.rjust(25))


# ## RPASRTITIOM()

# In[116]:


name = "My NamE is HaMZa i AM a sTuDent of PiAic iSlaMAbaD,baTch 3 OF aRtiFiciAl inTtelligenCE"
print(name.rpartition('sTuDent'))     #split the specified wod into an  r index


# ## RSPLIT()

# In[118]:


print(name.rsplit())        #convet string into list


# ## RSTRIP()

# In[120]:


print(name.rstrip())


# ## SPLIT()

# In[122]:


print(name.split())


# ## SPLITLINES

# In[124]:


print(name.splitlines())


# ## STARTSWITH()

# In[127]:


print(name.startswith('start '))   #it will tell you the first letter of sting will be this or not\
print(name.startswith('My'))


# ## Strip()

# In[128]:


print(name.strip())


# ## swapcase()

# In[129]:


print(name.swapcase())     #it will convet upper case letter into lower case letter and lower case letter into
                           #upper case letter


# ## tittle()

# In[131]:


print(name.title())       #convet first letter of each wod in the sting into upper case letter 


# ## upper()

# In[133]:


print(name.upper())  #convert all the letters of the sting into the upper case letter


# ## zfill()

# In[136]:


name25 = 'hamza'
print(name25.zfill(7)) #add zero into the sting afte the total the wods inthe string


# # ____________________ERRORS_______________________

# In[ ]:


#1)flush function......
#2)file function......
#3)sep function.......
#4)translate function............
   #if any one will guide me about these 3 functions then it will help me a lot
                         #regads hamza

