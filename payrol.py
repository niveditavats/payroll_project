# header for Salary slip
print("ABC Technologies Pay Stub for the Month of July - 2022")

#input parameters
relationship_status = input('Please mention if you are married or Single?: "M" for married and "S" for Single:  \n')
monthly_hour_worked = int(input("How many hours you have worked for the month?: "))
labour_rate : int(input("What is your wage per hour?: "))

#Salary parameters to be credited
base_salary = 8000
bonus = 0
annual_salary = base_salary*12
total_income = base_salary + bonus
print(f"Base salary = ${base_salary}")
print(f"Bonus = ${bonus}")
print(f"GROSS INCOME: ${total_income}")

#variables for Deductions mentioned below
print("BEFORE TAX DEDUCTION:")
adjustment = 0
inv_deduction = 1500
dental_plus = 0
flexmed = 0
catchups = 0
total_deduction = adjustment +inv_deduction + dental_plus + flexmed + catchups

#Tax brackets as per annual salary
brac_one = .1
brac_two = .12
brac_three = .22
brac_four= .24

#Pre tax deduction details
print(f'Adjustments "Medical, Parking Deduction, etc.": ${adjustment}')
print(f'401K Deduction: ${inv_deduction}')
print(f'Dental Plus deduction: ${dental_plus}')
print(f'FLEXMED for "Vision, Medicine and CYRO" deductions: ${flexmed}')
print(f'403b"Catch-ups" deduction: ${catchups}')
print(f'Total deductions: ${total_deduction}')

gross_income = total_income - total_deduction

print(f'FED TAXABLE GROSS: ${gross_income}')

# Conditional expression for choosing tax bracket as per gross salary
if annual_salary < 10275:
    tax_ded = gross_income * brac_one
elif annual_salary > 10275 and annual_salary < 41775:
    tax_ded = gross_income * brac_two
elif annual_salary > 41775 and annual_salary < 89075:
    tax_ded = gross_income * brac_three
elif annual_salary > 89075 and annual_salary < 170050:
    tax_ded = gross_income * brac_four
print(tax_ded)

#Medicare and social security rates:
medicare = .0145
social_security = .062

# Calculation of total tax deductions:
print("TOTAL TAXES")

w_exemptions = 0
fed_withholding = tax_ded
fed_med = gross_income * medicare
fed_oasdi = gross_income * social_security
total_tax = w_exemptions + fed_withholding +  fed_med + fed_oasdi
after_tax_income = gross_income - total_tax

# Tax deduction details:
print(f'W4 Exemptions "DEFAULT": ${w_exemptions}')
print(f'Fed Withholding "24%": ${fed_withholding}')
print(f'Fed MED/EE "1.45%": ${fed_med}')
print(f'Fed OASDI/EE "6.2%": ${fed_oasdi}')
print(f'Total Tax Deduction: ${total_tax}')

print(f'AFTER TAX INCOME: ${after_tax_income}')

#Calculation of After tax deductions:
print("AFTER TAX DEDUCTIONS:")
group_life_insurance = 0
supplemental_life_salary = 0
long_term_disability = 60
total_aftertax_deduction = group_life_insurance + supplemental_life_salary + long_term_disability
net_income = after_tax_income - total_aftertax_deduction

#writing after tax deduction  details
print(f'Group Life insurance: ${group_life_insurance}')
print(f'Supplemental Life 3X Salary: ${supplemental_life_salary}')
print(f'Long Term Disability: ${long_term_disability}')

#Calculation of Net salary calculation
print(f"NET INCOME: ${net_income}")
