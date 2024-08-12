The following is a description of one way to solve this cipher. There are multiple solve paths, but I anticipate that there is much overlap with the path described below.
* If necessary, do some research about the homophonic cipher.
* Open up a tool such as Notepad++ that has a find and replace function. Excel's VLOOKUP function is another handy tool for the same purpose.
* Using the crib in the description, look for double letters in positions three and four of a five letter word. Double 128 occurs twice. Assume 128 is 'z' and find and replace all instances of 128 with 'z'.
* Reconstruct the word pizza in two places, using find and replace each time to reveal more of the message.
* Notice a two-letter word earlier in the message that ends with 'p'.
* Try 175 = u (to make the word 'up').
* This creates some three-letter words that end with 'u'. The most likely English word is 'you'.
* Try 139 = y and 189 = o (to make the word 'you').
* Try 030 = o and 018 = u (to make another word 'you').
* The description text mentions "congratulations". There's also the following pattern near the top of the message: 100|o|132|123|157|013|042|u|000|a|172|001
* If participants try CONGRATULATE here, the task suddenly becomes so much easier, as they will have decrypted about ten percent of the message. There are other ways into the message, such as linking the information in the description about the flag being towards the bottom of the message, and the pattern 190|u|197|016|y (=CURLY) also towards the bottom of the message. Participants could make educated guesses in many other parts of the message at this point.
* The flag, spelled out in the message like this: 'pecan open curly bracket messy underscore hackers underscore safety underscore issue close curly bracket' can be reconstructed to pecan{messy_hackers_safety_issue}.

> to all the members of my illustrious cybercriminal gang i would like to congratulate you on your excellent work in the operations you have conducted in the past few months. its amazing how many people have weak passwords and leave themselves open to people like us. it continues to surprise me that people cannot be bothered to make use of multifactor authentication. as for patching applications and operating systems, there are still some companies out there that think that patching is too burdensome. they do not seem to know about the essential eight despite all the government advertising these people leave themselves wide open to your highly skilled procedures. unfortunately there is something that we need to address specifically there is a health and safety issue that i would like to raise with you. the operations floor is often a huge mess. last time i visited i saw a dozen pizza boxes, many still containing a slice or two of cold pizza. frankly i was quite disgusted by the sight of it. meanwhile the soft drink bottles were piled up in the corner rather than being placed in the recycling bins out the back. crumbs from potato chips were all over the floor. if you are looking for a flag for some kind of competition that is taking place this weekend then take note of the following pecan open curly bracket messy underscore hackers underscore safety underscore issue close curly bracket. please keep this place clean and tidy with the same level of dedication with which you carry out your nefarious operations.

200 numbers were selected to represent letters A to Z because some software (Cryptool 2.0 and some large language models) can automatically break this cipher when there are only 100 numbers. I am not aware of any software, readily available today, that can break the cipher when there are 200 numbers used.

This challenge requires some patience, logical thinking, knowledge of various features of the English language. With sufficient time, a homophonic cipher like this can be broken without a crib. However, to give the PECAN+ participants a chance of breaking the cipher within a reasonbable time frame, some cribs have been provided, and spaces have been retained.

Ideally, challenge participants will keep track of what substitutions they are trying, so that they can backtrack when they realise that they've made some false assumptions.

Homophonic ciphers are rarely used these days, but it is not inconceivable for a criminal gang to implement an old cryptosystem for some communications.
