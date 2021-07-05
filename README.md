# First-project
This was an online assignment I completed in April 2020 when I first started programming in python. 
<br>It is a program that bills customers of a rental car company.</br>
<br><h2>The Assignment</h2></br>
The program will compute and display information for a company which rents vehicles to its customers. 
For a specified customer, the program will compute and display the amount of money charged for that customer’s vehicle rental.</br> 
<br>The program will prompt the user to enter the following four items for a given customer (in the specified order):</br>
    <br> a. The customer’s name (a String)
    <br> b. The customer's classification code (a String).
    <br> c. The number of days the vehicle was rented (an integer).
    <br> d. The vehicle's odometer reading at the start of the rental period (an integer).
    <br> e. The vehicle's odometer reading at the end of the rental period (an integer).
<br>It will then process that customer information and display the results.
    The program will compute the amount of money that the customer will be billed, based on the customer's classification code, number of days in the rental period, and number of kilometers driven.
   <br> The program will recognize both upper case and lower case letters for the classification codes; the codes and related information are as follows:
 <br>a. Code 'B' (budget) 
          i. base charge: 40.00 dollars for each day, 
         ii. kilometers driven charge: 0.25 dollars for each kilometer driven.
<br> b. Code 'D' (daily)
    i. base charge: 60.00 dollars for each day,
    ii. kilometers driven charge: no charge if the average number of kilometers driven
        per day is 100 kilometers or less; otherwise, 0.25 dollars for each kilometer driven
        above the 100 kilometer per day limit.
<br>  c. Code 'W' (weekly)
     i. base charge: 190.00 dollars for each week (or fraction of a week),
     ii. kilometers driven charge:
         - There is no additional charge if the average number of kilometers driven 
         per week is 900 kilometers or less;
         - If the average number of kilometers driven per week exceeds 900 kilometers but 
         does not exceed 1500 kilometers, then there is an additional 50.00 dollars charge per week;
         - If the average number of kilometers driven per week exceeds the 1500 kilometer 
         per week limit, then there is an additional 100.00 dollars charge per week plus 
        0.25 dollars for each kilometer driven over the 1500 kilometer per week average.
