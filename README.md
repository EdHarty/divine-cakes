DIVINE CAKES

Divine cakes is a python command line programme that provides an automated data solution for a fictional bakery.
Divine cakes is a local Bakery that provides the community with freshly baked goods. The bakery wants to collect data on seven of it's most popular cakes to improve profits. This has to be done in an efficient manner. 

The most popular cakes include:

-Strawberry Gateau

-Red Velvet

-Mocha

-Rocky Road

-Mint Chocolate

-Lemon Drizzle

-Carrot Cake


![image](https://user-images.githubusercontent.com/88341568/161153751-d7cc1608-9af4-48ea-962f-83f1b5470910.png)


Staff arrive early in the morning to bake the stock in advance. If there is a particular cake that has sold out, more of that cake has to be made to meet demand. 
If stock is left over, they are discarded at the end of the day.
The aim of the command line programme is to (a) gather the bakery's sales figures, (b) calculate what is left over to give the bakery insight into how many of each cake should be made on a given business day. The primary outcomes are to reduce waste, improve efficiency and improve profitability of the bakery through the use of the python programme. This will also helo to predict sales in the future. In order to achieve this goal the python programme was linked with Google sheets so that the data could be pushed and pulled from the spreadsheet.

<img width="941" alt="screens" src="https://user-images.githubusercontent.com/88341568/161206516-22d352ec-ff85-404c-9cd9-1cd385827f5d.png">


TABLE OF CONTENTS

(1) Plan:

     objectives

(2) Features:
     
     Welcome message
     
     Instructions
     
     Data automation
     
     Error Message

(3) Testing:
 
     Python
      
     Manual testing
      
     Bugs
      
(4) Deployment:
     
     Heroku
     
(5) Credits

Plan:


<img width="505" alt="plan" src="https://user-images.githubusercontent.com/88341568/161161458-9836166e-8c09-4022-939b-c16249565af5.png">

Objectives:

I wanted to create a command line python programme that was easy to understand and navigate. I wanted the user to be able to input data into the terminal and for this data to also be represented on a google sheet. I set up an Aplication User Interface (API) to make it possible for the applications to share data.

<img width="948" alt="api" src="https://user-images.githubusercontent.com/88341568/161210139-149e1d04-5646-482e-99ec-d6efbd96a9ce.png">

I used the Code Institue template that contains the necessary front-end files to give users a way to interact with the project in a mock terminal on a web page.

<img width="951" alt="template" src="https://user-images.githubusercontent.com/88341568/161212059-3015965a-c6f1-4629-b59b-a0050149661f.png">

The aim of the programme is to gather the sales figures from the user and input these figures to the sales sheet, it will also calculate the surplus figures and revise the surplus sheet accordingly. I wanted the programme to represent the average amount of each of the cakes sold in the last 7 days in order to predict how many cakes to bake for the next day. The averages will then be seen in the stock sheet. Finally, I wanted the code to validate the user input.

Features:

Welcome message:

This first message you will see is a greeting welcoming the user to the programme.

<img width="467" alt="welcome" src="https://user-images.githubusercontent.com/88341568/161216452-b496cd7c-6e9b-4ebe-9075-8e279de70cbb.png">

Instructions:

Instructions on how to input the figures will be displayed with an example of the correct format to input the data.

<img width="461" alt="instuctions" src="https://user-images.githubusercontent.com/88341568/161217638-e98d2932-4b54-46ea-ab4c-c19324a4d341.png">

Data Automation:

When the user has input the figures in the correct format, firstly, they will see a message that the figures are valid. The programme will run. The user can see this in real-time in the terminal and in google sheets where the data is automatically updated.

The programme runs as follows:

                              Revising sales worksheet...

                              calculating surplus figures...

                              calculating stock figures...

                              Revising stock worksheet...

After each of the above, the user the user will also be able to see that the action has been confirmed and a link to google sheets to view this action.

<img width="664" alt="data auto" src="https://user-images.githubusercontent.com/88341568/161221213-97eb408f-99da-4508-b0ea-e6e5289bea64.png">

Error Message:

If invalid input, for example, a string such as tree or less than 7 figures are entered into the terminal an error message is displayed. 

<img width="653" alt="error message1" src="https://user-images.githubusercontent.com/88341568/161223426-9bb7cfb6-d09c-4c85-ae86-27e1cf797942.png">

Testing:

Python:

The python code was tested using the PEP8 validator.

The validator came back with the following results:

<img width="944" alt="pep8" src="https://user-images.githubusercontent.com/88341568/161225675-8e33857e-4428-48d3-9373-75d0648ed984.png">

Manual Testing:

I tested the code in the terminal by entering invalid data as well as entering correct data to see if the google sheets were being updated correctly.

<img width="579" alt="figure error" src="https://user-images.githubusercontent.com/88341568/161227151-4aaa348b-cce6-4eb8-9f6b-8e0057b16be7.png">

<img width="653" alt="error message1" src="https://user-images.githubusercontent.com/88341568/161227210-b50190e9-c7f3-4a84-be66-4995796d0449.png">

Bugs:

The initial surplus calculation had a TypeError - cannot use subtraction operand with a string and integer value. I fixed this using the int method as seen below.

<img width="680" alt="bug" src="https://user-images.githubusercontent.com/88341568/161228487-1598a548-498d-428b-bf7a-cbcff9d0f6d8.png">

Deployment:

           I had to create a list of requirements. This was done by entering pip3 freeze > requirements.txt in the terminal. The requirements.txt file is updated.     

           I then Git commit and Git pushed.

           I created a Heroku account.

           I created a new app and named that app.

           Then in the config vars section I input CREDS in the keys drop-down section and pasted the creds.json file in the value section.

           I added the buildpacks - Heroku Python and Heroku NodeJs to run the apps.

           I then went to the deploy section - selected Github - connect to Github - I searched for my project in my repository - I clicked connect to link Heroku.

           I clicked deploy branch. This installs python and various packages to run in the mock terminal.

           Finally a message to confirm that the was successfully deployed.

<img width="934" alt="deploy" src="https://user-images.githubusercontent.com/88341568/161231416-4f1bb85e-91af-4e73-a1a8-e65c1420fb97.png">


Credits:

https://www.lucidchart.com/pages/

http://pep8online.com/

https://codeinstitute.net/ie/





















      


  




