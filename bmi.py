# bmi.py
# Mayte Pacheco, 04/20/2017

def bmi(inches,pounds):
    bmi= ((pounds)*(39.3700787**2/2.20462262)/((inches)**2))
    return (bmi)
def category (index):
        if index < 18.5:
            return 'Underweight'
        elif index < 25:
            return 'Normal'
        elif index < 30:
            return 'Overweight'
        else:
            return 'Obese'








# solution must be above this comment

# do not change any part of the code below
def main():
    height = float( input("enter height in inches: ") )
    weight = float( input("enter weight in pounds: ") )
    bodyMassIndex = bmi(height, weight)
    bmiCat = category(bodyMassIndex)
    allCats = ['Underweight','Normal','Overweight','Obese']
    if bmiCat in allCats:
        print("BMI is {0:.1f}: {1}".format(bodyMassIndex, bmiCat))
    else: print ("Category error:",bmiCat,'\n  must be one of ',allCats)

main()
