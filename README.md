# CBN_Automation

In this project we will be reading the agent file which given by the client where we have to map the client personal mobile number based on his email or his name with brand name or company name
Then we have to validate that the matched number don't have any duplicates if it has duplicates if name or license id is same means we should ignore or otherwise we have to remove that particular number
Then remaining records we should automatically asign the file for each person who are going to work in manual

step 1:  Run the db connection code 
step 2 : Enter the url of client url sheet it will automatically read the dataframe file and its file name and sheet name
step 3 : run the column checking code ( it will detect the needed columns and it will create the required state file from db for Matching
step 4: run the matching code . it has certain rules it will autmotically match based on user email or user name with brand name or address
step 5: check duplicates
step 6: Allocate file to Manual workers
step 7: write the matched mobile numbers in phone matched column  to the same input sheet and manual workers name as well in assign column
