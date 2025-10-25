# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 21:03:29 2024

@author: Aabir Bhattacharya
"""
#------"may/might/can/could to be added---------
#Input a sentence and detect its tense
sent=input("Enter the sentence: \n")
wordlist=sent.split()
has_truth=False
have_truth=False
had_truth=False
wouldshould_truth=False
ing_truth=False
willshall_truth=False
maymight_truth=False
cancould_truth=False
if("has" in sent):
    has_truth=True
if("have" in sent):
    have_truth=True
if("had" in sent):
    had_truth=True
if("will" in sent or "shall" in sent):
    willshall_truth=True
if("would" in sent or "should" in sent):
    wouldshould_truth=True
if("may" in sent or "might" in sent):
    maymight_truth=True
if("ing" in sent):
    ing_truth=True

tense=""
for word in wordlist:
    #Present Tense Detection
    if (word=="is" or word.endswith("s") or word.endswith("es") 
        or word=="are" or word=="am"):
        tense="Simple Present"
    if(("is" in sent or "are" in sent or "am" in sent) 
       and ing_truth==True):
        tense="Present Continuous"
    if(has_truth==True or have_truth==True):
        tense="Present Perfect"
    if((has_truth==True or have_truth==True) and "been" in sent
       and ing_truth==True):
        tense="Present Perfect Continuous"
    
    #Past Tense Detection
    if (word=="was" or word=="were"):
        tense="Simple Past"
    if(("was" in sent or "were" in sent) and ing_truth==True):
        tense="Past Continuous"
    if(had_truth==True or (wouldshould_truth==True and have_truth==True)):
        tense="Past Perfect"
    if(had_truth==True and "been" in sent and ing_truth==True):
        tense="Past Perfect Continuous"
    
    #Future Tense Detection
    if (word=="will" or word=="shall"):
        tense="Simple Future"
    if((willshall_truth==True or wouldshould_truth==True) and "be" in sent 
       and ing_truth==True):
        tense="Future Continuous"
    if(willshall_truth==True and have_truth==True):
        tense="Future Perfect"
    if((willshall_truth==True or wouldshould_truth==True) 
       and have_truth==True and "been" in sent and ing_truth==True):
        tense="Future Perfect Continuous"
    
print("The tense is: ",tense)
    
        
            