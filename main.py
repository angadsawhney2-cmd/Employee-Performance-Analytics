"""
Purpose:
This program calculates different employee performance
measurements using an employee dataset and a user inputted selection. These measurements include employee
productivity, attendance reliability, customer service performance, bonus
eligibility, and overall employee performance.

"""
 

employee_dataset = [
    ["EmployeeID", "Name", "Age", "Department", "MonthlySales", 
    "AttendancePercentage", "OvertimeHours", "CustomerSatisfaction"],
    [401, "Alice Brown", 24, "Sales", 45000, 96, 12, 88],
    [402, "Brian Lee", 37, "Marketing", 30000, 85, 5, 75],
    [403, "Catherine Smith", 29, "Sales", 52000, 98, 18, 92],
    [404, "Daniel Wilson", 45, "Support", 25000, 80, 10, 70],
    [405, "Emma Johnson", 31, "Sales", 61000, 99, 20, 95],
    [406, "Frank Harris", 52, "Finance", 28000, 88, 4, 72],
    [407, "Grace Martin", 26, "Support", 22000, 91, 14, 85],
    [408, "Henry Clark", 33, "Marketing", 39000, 94, 8, 80],
    [409, "Isabella Young", 41, "Sales", 48000, 97, 16, 90],
    [410, "Jack Walker", 58, "Finance", 20000, 76, 2, 65]
] #Original Dataset

# Controls the menu system and calls the appropriate function based on the user's menu selection
def main(employee_dataset):
    """
    Input: 
        a nested list containing employee information.

    Output:
        Displays the menu, calls the selected calculation function, and prints
        the updated employee dataset. The function stops when the user selects
        option 6.
    """
    productivity_score_status = False 
    attendance_score_status = False 
    service_score_status = False 
    employee_bonus_status = False
    overall_employee_score_status = False 
    productivity_score_selection = "1" 
    attendance_score_selection = "2" 
    service_score_selection = "3"
    employee_bonus_selection = "4"
    overall_employee_score_selection = "5"
    program_quit_selection = "6"
    while True: 
        choice = menu()
        if input_checker(choice) == False: 
                    continue 
        else: 
            if choice == program_quit_selection:
                print() 
                print("Program exited")
                break

            elif choice == productivity_score_selection: 
                if productivity_score_status == False: 
                        productivity_score_status = True
                        calculate_productivity_score(employee_dataset)
                else:
                     print() 
                     print("Cannot pick the same option twice")
                     print("Please pick again")

            elif choice == attendance_score_selection: 
                 if attendance_score_status == False: 
                        attendance_score_status = True
                        calculate_reliability_score(employee_dataset)
                 else: 
                        print()
                        print("Cannot pick the same option twice")
                        print("Please pick again")

            elif choice == service_score_selection:
                  if service_score_status == False: 
                        service_score_status = True
                        calculate_service_performance(employee_dataset)
                  else: 
                        print()
                        print("Cannot pick the same option twice")
                        print("Please pick again")

            elif choice == employee_bonus_selection:
                  if employee_bonus_status == False:
                        employee_bonus_status = True
                        calculate_bonus_assessment(employee_dataset)
                  else:
                        print() 
                        print("Cannot pick the same option twice")
                        print("Please pick again") 
            elif choice == overall_employee_score_selection: 
                 if overall_employee_score_status == False:
                           overall_employee_score_status = True
                           calculate_overall_employee_performance_score(employee_dataset)
                 else: 
                      print()
                      print("Cannot pick the same option twice")
                      print("Please pick again") 
                       
           
# Displays the program menu and asks the user to select an option.
def menu(): 
    """
    Input:
        A menu choice entered by the user.

    Output:
        Returns the user's menu choice as a string.
    """

    print()
    print("======Perform X======")
    print()
    print("1. Calculate Employee Productivity Score") 
    print("2. Calculate Attendance Reliability Score") 
    print("3. Calculate Customer Service Performance Index")
    print("4. Calculate Employee Bonus Eligibility")
    print("5. Calculate Overall Employee Performance Score")
    print("6. Exit")
    user_choice = input("Enter your choice (1-6): ")
    return(user_choice)

# Checking whether the user's selected menu is valid.
def input_checker(choice): 
    """
    Input:
        The menu chosen by the user.

    Output:
        Returns True when the choice is between 1 and 6.
        Returns False and displays an error message when the choice is invalid.
    """
    Valid = True 
    valid_inputs = ["1","2","3","4","5","6"]
    if choice not in valid_inputs: 
        print()
        print("Invalid input")
        print("Please try again")
        Valid = False 
        return Valid 
    else: 
        return Valid
            
#------------------------------------------------------------PRODUCTIVITY SCORE CODE----------------------------------------------------------------------------------  

#The main function to calculate raw productiviy score and then use the helper function (perfom_producitiviy_changes) to provide the final producvitivy score which it appends to the dataset and prints it out. 
def calculate_productivity_score(dataset): 
    """
    Input/Parameter:Takes the provided dataset as an input
    Output: Appends a new column to the dataset with the final productivity score and prints the updated dataset 
    """
    sales_divisor = 1000
    overtime_hours_multiplier = 2 
    dataset[0].append("ProductivityScore")

    for employee_stats in dataset[1:]:
            monthly_sales = employee_stats[4] 
            overtime_hours = employee_stats[6]
            raw_productivity_score = (monthly_sales/sales_divisor) + (overtime_hours*overtime_hours_multiplier) 
            final_productiviy_score = perfom_productivity_changes(employee_stats, raw_productivity_score, monthly_sales)
            employee_stats.append(final_productiviy_score)

    for employee_stats in dataset: 
        print(employee_stats) 


#A helper function to alter the raw productiviy score based on the extended conditions and rounds it to 2 decimals 
def perfom_productivity_changes(employee_stats, raw_productivity_score, monthly_sales):
    """
    Input/Parameters: Takes the inner list of the dataset for a given employee, the raw productivity score and monthly sales from main function 
    Output: Returns the final productiviy score to the main function 

    """
    monthly_sales_boundary = 50000
    attendance_percentage_boundary = 85 
    max_productivity_score = 100 
    productivity_increase_percentage = 1.1 
    productivity_decrease_percentage = 0.85
    decimal_rounding_place = 2 
    attendance_percentage = employee_stats[5] 
    final_productivity_score = raw_productivity_score

    if monthly_sales >=monthly_sales_boundary:
        final_productivity_score = final_productivity_score*productivity_increase_percentage
    if attendance_percentage <attendance_percentage_boundary: 
        final_productivity_score = final_productivity_score*productivity_decrease_percentage 
    if final_productivity_score>max_productivity_score: 
        final_productivity_score = max_productivity_score
    final_productivity_score = round(final_productivity_score, decimal_rounding_place)

    return final_productivity_score


#------------------------------------------------------------RELIABILITY SCORE CODE----------------------------------------------------------------------------------  

#Helper Function that Calculates the reliability score based on a single employee.
def calculate_reliability(attendance, overtime): #helper function
    """
    Calculates the reliability score for one employee.
    Input:
        attendance - employee's attendance percentage
        overtime - employee's overtime hours
    Output:
        Returns the reliability score rounded to two decimal pieces 
    """
    attendance_threshold= 95
    bonus_points = 5
    overtime_multiplier = 0.5
    overtime_limit = 15
    reliability_multiplier = 0.05
    reliability_exceed = 100
    decimal_pieces_assigned = 2
    reliability_score = attendance + (overtime * overtime_multiplier) #Formula
    if attendance >= attendance_threshold:
        reliability_score = reliability_score + bonus_points #add five bonus points in rs
    if overtime >= overtime_limit:
        reliability_score = reliability_score + (reliability_score * reliability_multiplier) #increase rs by 5%
    if reliability_score > reliability_exceed:
        reliability_score = reliability_exceed #set rs to 100 if rs exceeds the limit
    return round(reliability_score, decimal_pieces_assigned) #round to two decimal pieces

#Primary Function that Calculates and Appends the reliability scores of all employees in the Employee Dataset.
def calculate_reliability_score(employee_dataset):
    """
    Calculates the reliability store for each employee in a dataset.
    Input:
        employee_dataset = a list containing the complete information of each employee.
    Output:
        prints out the updated list which also contains the reliability score of each employee.
    """
    first_index = 0
    second_index = 1
    attendance_index = employee_dataset[first_index].index("AttendancePercentage") #define attendance
    overtime_index = employee_dataset[first_index].index("OvertimeHours") #define overtime
    employee_dataset[first_index].append("ReliabilityScore") #implement reliability score in the list

    for row in employee_dataset[second_index:]: #from the second index to final
        attendancePercentage = row[attendance_index]
        overtimeHours = row[overtime_index]

        reliability_score = calculate_reliability(attendancePercentage, overtimeHours) #call helper function
        row.append(reliability_score) #add reliability score to last index of the lists

    for row in employee_dataset:
        print(row) #print updated list with rs

#------------------------------------------------------------CUSTOMER SERVICE SCORE CODE----------------------------------------------------------------------------------  

# This section is to ensure that the program has no magic numbers sir.
Customer_Satisfaction_Weight = 0.7
Attendance_Weight = 0.3
Senior_Age = 50
Senior_Bonus = 1.03
Support_Bonus = 1.05
Excellent_Score_Minimum = 90
Good_Score_Minimum = 75
Good_Score_Maximum = 89.99
Needed_Decimal_Places = 2

# Helper function for calculating items in data set
def calculations_for_items (customer_satisfaction, attendance_percentage, age, department):
    """ 
    
    A helper function which will calculate the service performance index (also rounded into 2 decimal places), give bonuses determined by the certain age and department of an employee. 
    It will then give the service performance index a classification. Then the function returns both the service performance index and its classification.

    """
    service_performance_index = customer_satisfaction * Customer_Satisfaction_Weight + attendance_percentage * Attendance_Weight
    
    

    # This will give bonuses to the service perfromance index and also classify each employee's Service performance index
    if age >= Senior_Age:
        service_performance_index *= Senior_Bonus 
    if department == "Support":
        service_performance_index *= Support_Bonus
    service_performance_index = round(service_performance_index, Needed_Decimal_Places)
    if service_performance_index >= Excellent_Score_Minimum:
            classification = "Excellent"
    elif service_performance_index >= Good_Score_Minimum and service_performance_index <= Good_Score_Maximum: 
            classification = "Good"
    elif service_performance_index < Good_Score_Minimum:
            classification = "Needs Improvement"
    return service_performance_index, classification


# Main function to find items needed, calls for helper function for calculations, and to add the calculated values into the list
def calculate_service_performance(dataset):
    """

    This function adds "service performance index" and "ServiceClassification" into the the list. Then it gives the required items for calculations and calls for the helper function
    to return values for the service performance index and the classification.
    The values are then appended to the list.

    """
    #This will update the data set adding two new categories
    dataset[0].append("ServicePerformanceIndex") 
    dataset[0].append("ServiceClassification")

    for items in dataset[1:]: #Identifying items needed for calculations
        customer_satisfaction = items[7]
        attendance_percentage = items[5]
        age = items[2]
        department = items[3]

        service_performance_index, classification = calculations_for_items(customer_satisfaction, attendance_percentage, age, department) #Calling helper function to calculate calssifications and service performance index

        items.append(service_performance_index)
        items.append(classification)

    for row in dataset:
        print(row)


#------------------------------------------------------------BONUS SCORE CODE----------------------------------------------------------------------------------  

#A helper function that calculates the bonus score, rounds it to 2 decimal places and returns the value to the other helper function and the main function.
def calculate_bonus_score(MonthlySales, AttendancePercentage):
    """
    Input: Takes MonthlySales and AttendancePercentage from the nested list in the dataset 
    Output: BonusScore
    """
    Sales_per_bonus_point = 2000
    RawScore = ((MonthlySales / Sales_per_bonus_point) + AttendancePercentage)
    rounding_decimal_place = 2
    BonusScore = round(RawScore, rounding_decimal_place)
    return BonusScore

#Helper function that helps determines the bonus level and returns it to the main function
def calculate_bonus_level(BonusScore, OvertimeHours, CustomerSatisfaction):
    """
    Input: Takes the BonusScore from the previous helper function plus the OvertimeHours and CustomerSatisfaction values from the nested list in the dataset 
    Output: Bonuslevel classification 
    """
    levelscore = round(BonusScore)

    #Base classification of Bonus level
    Standard_score_threshold = 100
    Performance_score_threshold = 130
    if levelscore <= Standard_score_threshold:
        BonusLevel = "Standard Bonus"
    elif Standard_score_threshold <= levelscore <= Performance_score_threshold:
        BonusLevel = "Performance Bonus"
    elif levelscore > Performance_score_threshold:
        BonusLevel = "Executive Bonus"

    #High Overtime Adjustment
    min_overtimehours_for_boost = 15
    if OvertimeHours >= min_overtimehours_for_boost:
        if BonusLevel == "Standard Bonus":
            BonusLevel = "Performance Bonus"
        elif BonusLevel == "Performance Bonus":
            BonusLevel = "Executive Bonus"
        elif BonusLevel == "Executive Bonus":
            BonusLevel = "Executive Bonus"

    #low customer satisfaction rule
    min_customersatisfaction_threshold = 70
    if CustomerSatisfaction < min_customersatisfaction_threshold:
        BonusLevel = "Standard Bonus"

    return BonusLevel

#Main function that processes the dataset/employee records, appends the bonus score and level from the other helper functions, and prints the upated dataset
def calculate_bonus_assessment(dataset):
    """
    Input:Takes the provided dataset as an input
    Output:Appends 2 new columns (bonus score and bonus level) to the dataset with the calculated values for each nested list and prints the new dataset
    
    """
    
    #appends the column headers
    dataset[0].append("BonusScore")
    dataset[0].append("BonusLevel")

    #processes bonus score and bonuslevel values over each data rows.
    for stat_row in dataset[1:]:
            MonthlySales = stat_row[4]
            AttendancePercentage = stat_row[5]
            OvertimeHours = stat_row[6]
            CustomerSatisfaction = stat_row[7]

            BonusScore = calculate_bonus_score(MonthlySales, AttendancePercentage)
            stat_row.append(BonusScore)

            BonusLevel = calculate_bonus_level(BonusScore, OvertimeHours, CustomerSatisfaction)

            stat_row.append(BonusLevel)

    #prints updated dataset
    for row in dataset:
        print(row)


def calculate_overall_employee_performance_score(dataset):
    """
    Input: Takes the provided dataset as an input.
    Output: Verifies required columns, calculates the Overall Employee Performance Score (OEPS), 
            adds the OEPS and OEPSClassification columns, and prints the updated dataset.
    """
    headers = dataset[0]
    
    # Verify prerequisite columns exist
    #not necessary since we alr have the status true thingy for our options 
    if ("ProductivityScore" not in headers or "ReliabilityScore" not in headers or 
        "ServicePerformanceIndex" not in headers or "BonusScore" not in headers):

        print("Error: Required metrics are missing.")
        print("Please run the previous menu options to calculate these values first.")
        return
        
    productivity_idx = 0
    reliability_idx = 0
    customer_service_idx = 0
    bonus_idx = 0
    
    for i in range(len(headers)):
        if headers[i] == "ProductivityScore":
            productivity_idx = i
        elif headers[i] == "ReliabilityScore":
            reliability_idx = i
        elif headers[i] == "ServicePerformanceIndex":
            customer_service_idx = i
        elif headers[i] == "BonusScore":
            bonus_idx = i
            
    dataset[0].append("OEPS")
    dataset[0].append("OEPSClassification")
    
    for row in dataset[1:]:
        #Use existing calculated values only
        productivity_score = row[productivity_idx]
        reliability_score = row[reliability_idx]
        customer_service_score = row[customer_service_idx]
        bonus_score = row[bonus_idx]
        
        #Calculate OEPS using the given formula
        productivity_weight = 0.35
        reliability_weight = 0.25
        customer_service_weight = 0.20
        bonus_weight = 0.20 
        oeps = (productivity_score * productivity_weight) + (reliability_score * reliability_weight) + (customer_service_score * customer_service_weight) + (bonus_score * bonus_weight)
        
        # Format OEPS values to two decimal places
        rounding_place = 2
        oeps = round(oeps, rounding_place)
        
        # Determine classification
        Outstanding_threshold = 85
        Strong_threshold = 70
        satisfactory_threshold = 50

        if oeps >= Outstanding_threshold:
            oeps_classification = "Outstanding Employee"
        elif oeps >= Strong_threshold: 
            oeps_classification = "Strong Performer"
        elif oeps >= satisfactory_threshold: 
            oeps_classification = "Satisfactory Performer"
        else:            
            oeps_classification = "Needs Improvement"
            
        row.append(oeps)
        row.append(oeps_classification)
        
    #Print the updated dataset
    print("Overall Employee Performance Scores Calculated:")
    for row in dataset:
        print(row)
     
     



main(employee_dataset)
