#import packages
import pandas as pd  # The as keyword lets you shorten the name of the import package

original = pd.read_csv("simple_retail.csv")             # Load the .csv file - It is important to note that you have to include the extension as well. 
                                                        # If you do not specify a path, Python will assume the file is in the same directory as the code file you a running.
                                                        # Documentation for pandas.readcsv() https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

print(original)                                         # Prints the dataframe we just created. If we view the variable explorer we can also see the dataframe. 

#From here we can see that the dataframe consists of 541909 entries with these attributes: 0) Index 1)InvoiceNo 2) Description 3) Quantity 4) Invoice Date 5) UnitPrice 6) ConstomerID  7)Country 


# Right now the data is sorted by InvoiceNo and Index. Let's try sorting by UnitPrice 
# We can follow this documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html to sort

sort_by_price = original.sort_values(by=['UnitPrice'])
print("\n Sorted list by UnitPrice \n")
print(sort_by_price)                                    # Unfortunately you won't see prices on the console unless you meddle with the settings a bit, but you can see that the dataset has clearly been changed. (you can open this in variable explorer to confirm)

# Let's say we want to export this new dataframe and store it. 
# Again documentation if you need can be found here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html

sort_by_price.to_csv("simple_retail_sorted.csv")
