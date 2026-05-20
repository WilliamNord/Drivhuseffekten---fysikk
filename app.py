from flask import Flask, render_template, request
from math import *

app = Flask(__name__)


sigma = 5.67*10**(-8)
albedo = 0.3
epsilon = 0.73 # 0.78? 0.90?
a = 2.9*10**(-3)


lag = 1

#solkonstanten
U_sol = 1361
U_inn = (U_sol/4) * (1 - albedo)

def stefanBoltzman_U(T):
    # returnerer Utrstråling
    return sigma*T**4

def stefanBoltzman_T(U):
    #returnerer temperatur
    return (U/sigma)**(1/4)

#astronomisk enhet
AU = 1.496*10**11

#solens areal i kvadratmeter
A_sol = 6.09*10**18

#solens temperatur i kelvin
Temp_sol = 5772

# U_sol = stefanBoltzman_U(Temp_sol)
# U_inn = (U_sol*A_sol)/(4*pi*AU**2)


@app.route('/')
def hello_world():

    T_jord = (0)
    innkommende = (U_inn) * (1 - albedo)
    
    while epsilon * stefanBoltzman_U(T_jord) < innkommende:
        print(T_jord - 273.15)
        T_jord += 0.1
    print(U_inn)

    print("stedan2", stefanBoltzman_T(innkommende)-273)
    return f"{T_jord - 273.15}°C"



@app.route('/2', methods=['GET', 'POST'])
def hello_world2():
    T_atm_list = []

    lag = request.form.get('lag', type=int)
    
    U_jord = U_inn #/ (1 - 0.5 * epsilon)

    if lag is not None:
        for i in range(1, lag + 1):
            U_atm = ((0.5)**(i)) * U_jord
            T_atm_list.append(round(stefanBoltzman_T(U_atm) - 273.15))
            U_jord += ((U_atm)*(0.5)**(i))
            
    T_jord = stefanBoltzman_T(U_jord)
    T_jord_C = round(T_jord - 273.15)

    return render_template('index.html', T_jord=T_jord_C, T_atm_list=T_atm_list)

@app.route('/about')
def about():
    return 'This is the about page.'

if __name__ == '__main__':
    app.run(debug=True, port=5005)
