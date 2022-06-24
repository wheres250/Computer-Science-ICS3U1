"""
Author: Kvin Nguyen , Working Solo
Date: 06/15/2022
Description: Research Bin
"""
import csv
def research_data():
    """
    Args:

    Returns:
    """
#Processing
    # enter the entry into a CSV file
    with open('research.csv', 'w', newline='') as csvfile:
        myFile = csv.writer(csvfile, delimiter=' ')
        myFile.writerow( [ "Entry Date" , "Course" , "Course Chapter" , "Topic" ] )
        save = "research"
        #Import
        while True:
            date = input(" What day is it today? Ex: 06/14/2022: ")
            # user will state what course the research is for
            course = input(" What course is the research for? Ex: Computer Science , Functions , Accounting :  ")
            # user will state what chapter the research is for
            chapter = input(" What chapter are you researching about? Ex: Chapter 8 : ")
            # user will explain search or topic
            topic = input(" Please input your topic that you would like to save into the database for later research. : ")
            # requests if the user would like to save the topic 
            save = input(" Would you like to save? y/n: ")  
            if save.lower() == "y":
                myFile.writerow([ date , course , chapter , topic])
                print("Saved.")
                break
            else:
                # requests if the user would like to make a second entry
                save = input("Would you like to make another entry? y/n: ")
                print("Continue.")
                if save.lower() == "n":
                    break
research_data()
#Output
    # bin will be sorted by user's choice:
