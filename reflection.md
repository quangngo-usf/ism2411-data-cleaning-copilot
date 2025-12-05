
# Reflection

## What Copilot Generated
For this project, I learned how to clean data using Python and how to use GitHub Copilot to help me write functions more efficiently. I used Copilot mainly to generate the basic structure of my functions, and then I edited the code to make it match the assignment requirements. For example, Copilot gave me simple versions of the load_data, handle_missing_values, save_clean_data  and clean_column_names functions, but I added error handling, additional cleaning steps, and comments to make the code more complete.

## What I Modified
After Copilot generated the initial functions, I made several changes to make the code clearer and more accurate. I renamed some variables so they were easier to understand, and I simplified some of Copilot’s logic so the steps were more direct. I also added my own conditions, like checking if a file exists and making sure columns like “price” and “quantity” actually exist before cleaning them. These changes were needed to avoid errors, match the style of the assignment, and make sure the script worked correctly with the messy dataset.

## What I Learned
This assignment taught me how important it is to validate and clean real-world data before using it. Even simple problems like extra spaces, inconsistent column names, or negative numbers can cause errors later. I learned how to standardize column names, convert columns safely, drop invalid rows, and write a repeatable cleaning pipeline. I also learned that data cleaning is always step-by-step: small, consistent transformations lead to a much cleaner final dataset.

## What I Learned About Copilot
I also learned that Copilot is a helpful tool, but not something I can rely on blindly. It is great at generating boilerplate code and suggesting common patterns, but it does not always understand the specific requirements of an assignment. For example, Copilot kept suggesting to “fill missing values with zero,” which would have caused incorrect results in sales data. I had to override those suggestions and choose a more appropriate rule. 

