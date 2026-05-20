#Konstanter
sigma = 5.67*10**(-8) #W/(m^2K^4), Stefan-Boltzmann-konstanten
I_sol = 1361 #W/m^2, lysintensiteten fra sola
alfa = 0.30 # albedo, andel reflektert av skyer og jordoverflate
epsilon = 0.90
 # emissivitet, andel infrarød stråling fra jorda som blir 
                # absorbert av atmosfæren pga drivhusgasser.

# Gjennomsnittlig effektiv solinnstråling på jorda 
I_sol_eff = I_sol/4 *(1-alfa)

#Utstrålt effekt fra jorda (strålingsbalanse)
U_jord = I_sol_eff/(1-0.5*epsilon)
U_atm = 0.5*U_jord

#Temperaturen til jordkloden
T_jord = (U_jord/sigma)**(1/4) # Stefan-Boltzmanns lov
T_jord_C = T_jord - 273 # Temperaturen på jorda målt i Celsius

T_atm = (U_atm/sigma)**(1/4) # Stefan-Boltzmanns lov
T_atm_C = T_atm - 273 # Temperaturen på jorda målt i Celsius

print("Temperaturen på jordoverflata er", round(T_jord_C, 1), "grader Celsius.")
print("Temperaturen til jordatmosfæren er", round(T_atm_C, 1), "grader Celsius.")

