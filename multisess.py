# SpamX Multiple String Generator 

from pyrogram import Client

import tgcrypto

ID = int(input(" \n Send Api Id To Generate String Sessions: "))

HASH = str(input(" \n Send Api Hash To Generate String Sessions: "))

try:

     number_to_add = int(input(" \n Enter number of accounts you want to generate string:"))

     whom = input(" \n Enter Your Username or User id so, Client can forward all sessions to you else press enter: ")

     for i in range(number_to_add):

            Badnam = Client(name="Badnam", api_id=ID, api_hash=HASH, in_memory=True)

            Badnam.start()

            s = Badnam.export_session_string()

            sess = str(s)

            if whom:

                id = Badnam.get_users(whom).id

                Badnam.send_message(id, f"**Pyrogram String Session** \n\n `{sess}` \n\n © @itz_Badnam")

            else:

                Badnam.send_message("me", f"**Pyrogram String Session** \n\n `{sess}` \n\n © @Itz_Badnam")

       

     if whom:

           print(f"All Session has been sent to {whom}")

     else:

         print("All Sessions has been sent to saved message")

         

except Exception as a:

   print(a)    
