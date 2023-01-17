"""
    (a) The recommended daily allowance (RDA) of the trace metal magnesium is
            410 mg/day for males. Express this quantity in \mu g/day
    (b) For adults, the RDA of the amino acid lysine is 12 mg per kg of body weight.
            How many grams per day should a 75 kg adult receive?
    (c) A typical multivitamin tablet can contain 2.0 mg of vitamin B_2 (riboflavin),
            and the RDA is 0.0030 g/day. 
            How many such tablets should a person take each day to get the proper amount 
            of this vitamin, if he gets none from other sources?
    (d) The RDA for the trace element selenium is 0.000070 g/day. Express this dose in 
            mg/day    
"""
# import necessary conversion functions
from milligram_microgram import milligram_microgram
from milligrams_grams import milligrams_grams 
from grams_milligrams import grams_milligrams

# greek mu constant
mu = u'\u03bc'

# Question a
RDA_milligrams_Mg  = 410

a = milligram_microgram(RDA_milligrams_Mg)
print(f"The trace amount of {RDA_milligrams_Mg}mg is equal to {a}{mu}g")

# Question b
RDA_amino_acid_lysine_milligrams_per_kg = 12
adult_weight = 75
RDA_amino_acid_lysine_total_mg = adult_weight * RDA_amino_acid_lysine_milligrams_per_kg

b = milligrams_grams(RDA_amino_acid_lysine_total_mg)
print(f"The total RDA of amino acid lysine in milligrams is {RDA_amino_acid_lysine_total_mg} and in grams is {b}")

# Question c
B_2_tablet_milligrams = 2.0
B_2_RDA_grams = .0030

B_2_RDA_milligrams = grams_milligrams(B_2_RDA_grams)
num_tablets = (B_2_RDA_milligrams / B_2_tablet_milligrams)

print(f"The total number of 2.0mg tablets a person should take is {num_tablets}")

# Question d
Se_RDA_grams = 7e-5
Se_RDA_milligrams = 7e-2

print(f'The RDA of selenium in grams is {Se_RDA_grams} and in milligrams is {Se_RDA_milligrams}')



# creat a conversion file containing all the conversion functions