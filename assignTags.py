import pandas as pd
import numpy as np
import ast
import unidecode

# data from xlsx sheet with tags for subcategories and the required columns: 
#    Category: the category name
#    Subcategory: the subcategory name
#    Tags: comma-separated (", ") tags to be assigned to merchants that have been
#              labelled with Subcategory
tags = pd.read_excel("C:/Users/james/Desktop/assignTags/tags.xlsx")
tags["subcat_id"] = tags.apply(lambda row: (row["Category"], row["Subcategory"]), axis=1)
tags = tags.set_index("subcat_id")
tags = tags.to_dict('index') 
for k, v in tags.items():
    v["Tags"] = ast.literal_eval(v["Tags"])
    
# distinct_elements: returns a list of distinct strings that is a superset of newElements.
#   Case is ignored--all newElements are lowercase. Accents are removed using
#   unidecode.
# List(of Str) List(of Str)--> List (of Str)
def distinct_elements(newElements, existingElements):
    lowerNewElements = [x.lower() for x in newElements]
    lowerExistingElements = [x.lower() for x in existingElements]
    combineDistinctElements = list(set(lowerNewElements + lowerExistingElements))
    removeAccents = [unidecode.unidecode(x) for x in combineDistinctElements]
    return removeAccents
        
# data from xlsx sheet with subcategory labels assigned to merchants
# and required columns:
#    Brand_Name: the merchant's name
#    Category: the merchant's category
#    Subcategories: comma-seperated (", ") subcategory labels assigned to the merchant
#    Existing_Tags: list of existing tags for the merchant
merchants = pd.read_excel("C:/Users/james/Desktop/assignTags/merchants.xlsx")
merchants["Tags"] = np.empty((len(merchants), 0)).tolist()
merchants = merchants.to_dict('index') 
for k, v in merchants.items():
    null_subcat_id = (v["Category"], np.nan)
    v["Tags"] += tags[null_subcat_id]["Tags"]
    if type(v["Subcategories"]) is str:
        v["Subcategories"] = v["Subcategories"].split(", ")
        for subcategory in v["Subcategories"]:
            subcat_id = (v["Category"], subcategory)
            v["Tags"] += tags[subcat_id]["Tags"]
    v["Existing_Tags"] = ast.literal_eval(v["Existing_Tags"])
    v["Tags"] = distinct_elements(v["Tags"], v["Existing_Tags"])

merchants = pd.DataFrame.from_dict(merchants, 'index')
merchants.to_csv('assigned tags.csv')