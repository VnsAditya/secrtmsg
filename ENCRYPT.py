#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 00:38:57 2018

@author: audi
"""
''' This code is used to encrypt the message 
'''
#take alphabet as a variable and store the values

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

#key is the secret key used to encrypt the message

key = int(input("enter a value 0-26 :"))

#make a variable newmessge to store the message 

newMessage = ''
#take the input frm the user
Message = input("please enter a Message :")
#for loop is used to repeat the char in message
for character in Message:
#if is used to check wheter the chars are in alph are not    
 if character in alphabet:
#find the position of the char     
  position = alphabet.find(character)
#print(position)
#to add the key value to the position
  newPosition =  (position + key) % 52
#print(newPosition)
#to show the value in the position
  newCharacter = alphabet[newPosition]
#print ("The new character is : ",newCharacter)
#this stores the new msg 
  newMessage += newCharacter
#checks the symbols nd print thm  
 else:
  newMessage += character     
#the message is printed  
print("THE MESSAGE IS ENCRYPTED",newMessage)

""" THE MESSAGE IS ENCRYPTED LOL """
