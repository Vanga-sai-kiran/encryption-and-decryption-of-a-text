import random
alfabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
         "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",
         "0","1","2","3","4","5","6","7","8","9","!","~","#","$","%","^","&","*","(",")","_","+","="]

while True:
  direction=input("Type 'encode' to encode word or 'decode' to decode text or 'stop' to exit\n")
  if direction=="stop":
    print("Good Bye!!!\n")
    break 
  
  word=input("enter a word   :  \n").lower()
  shift_number=int(input("enter a shift number :\n"))
  shift_number=shift_number%26
  def ecry_decry(word,shift_number,direction):
       caifer_word=""
       for letter in word:
           position=alfabet.index(letter)
           if direction=="encode":
              new_position=position+shift_number
              caifer_word+=alfabet[new_position]
           else:
              new_position=position-shift_number
              caifer_word+=alfabet[new_position]
       if direction=="encode":
        print(f"The encoded Text will be   :{caifer_word}")
       elif direction=="decode":
          print(f"The decoded text will be   :{caifer_word}")
  
   
  ecry_decry(word,shift_number,direction)

