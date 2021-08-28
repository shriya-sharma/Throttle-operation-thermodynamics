import numpy as np

P2 = 0.1
T2 = 0

def thermo_tables(T_01, Cp_01, H_sat_01, S_sat_01, liq_index, vap_index):
    vals_01 = np.zeros((23, 4))

    for i in range(23):
        vals_01[i][0] = T_01[i]
        vals_01[i][1] = Cp_01[i]

    vals_01[liq_index][2] = H_sat_01[0]
    vals_01[vap_index][2] = H_sat_01[1]
    vals_01[liq_index][3] = S_sat_01[0]
    vals_01[vap_index][3] = S_sat_01[1]

    for i in range(liq_index):
        vals_01[liq_index - 1 - i][2] = vals_01[liq_index - i][2] - ((vals_01[liq_index - i][1] + vals_01[liq_index - 1 - i][1]) * (vals_01[liq_index - i][0] - vals_01[liq_index - 1 - i][0]))/2
        vals_01[liq_index - 1 - i][3] = vals_01[liq_index - i][3] - (((vals_01[liq_index - i][1] / vals_01[liq_index - i][0]) + (vals_01[liq_index - 1 - i][1] / vals_01[liq_index - 1 - i][0])) *
                                                    (vals_01[liq_index - i][0] - vals_01[liq_index - 1 - i][0]))/2

    for i in range(vap_index, 22):
        vals_01[i + 1][2] = vals_01[i][2] + ((vals_01[i + 1][1] + vals_01[i][1]) * (vals_01[i + 1][0] - vals_01[i][0])) / 2
        vals_01[i + 1][3] = vals_01[i][3] + (((vals_01[i + 1][1] / vals_01[i + 1][0]) + (vals_01[i][1] / vals_01[i][0])) *
                                              (vals_01[i + 1][0] - vals_01[i][0])) / 2

    vals_01[:, 2] = np.around(vals_01[:, 2], 1)
    vals_01[:, 3] = np.around(vals_01[:, 3], 3)

    return vals_01

def create_table(vals, T_sat, H_sat, S_sat):
    table = {}
    for i in range(23):
        if vals[i][0] == T_sat:
            if str(vals[i][0]) not in table.keys():
                table[str(vals[i][0])] = {
                    "cp": vals[i][1],
                    "enthalpy": vals[i][2],
                    "entropy": vals[i][3]
                    }
                continue

        table[vals[i][0]] = {
            "cp": vals[i][1],
            "enthalpy": vals[i][2],
            "entropy": vals[i][3]
            }
    table['T_sat'] = T_sat
    table['H_sat'] = H_sat
    table['S_sat'] = S_sat
    return table

'''
Enthalpy - Entropy values at Pressure = 0.1 and different temperatures.
'''

H_sat_01 = [16770.1, 39202.7]
S_sat_01 = [218.485, 300.764]

T_01 = [200.00, 210.00, 220.00, 230.00, 240.00, 250.00, 260.00, 270.00, 272.64, 272.64, 280.00, 290.00, 300.00,
        310.00, 320.00, 330.00, 340.00, 350.00, 360.00, 370.00, 380.00, 390.00, 400.00]

Cp_01 = [118.87, 120.28, 121.98, 123.94, 126.13, 128.54, 131.15, 133.95, 134.73, 94.82, 96.22, 98.31, 100.54, 102.86,
         105.25, 107.68, 110.13, 112.61, 115.1, 117.59, 120.09, 122.57, 125.04]

vals_01 = thermo_tables(T_01, Cp_01, H_sat_01, S_sat_01, liq_index = 8, vap_index = 9)
table_01 = create_table(vals_01, 272.64, H_sat_01, S_sat_01)

'''
Enthalpy - Entropy values at Pressure = 1.4 and different temperatures.
'''

H_sat_14 = [31450.9, 46891.0]
S_sat_14 = [263.868, 305.738]

T_14 = [200.00, 210.00, 220.00, 230.00, 240.00, 250.00, 260.00, 270.00, 280.00, 290.00, 300.00, 310.00, 320.00, 330.00,
        340.00, 350.00, 360.00, 368.760, 368.760, 370.00, 380.00, 390.00, 400.00]

Cp_14 = [118.76, 120.15, 121.83, 123.75, 125.91, 128.28, 130.84, 133.59, 136.52, 139.63, 142.95, 146.49, 150.29, 154.41,
         158.95, 164.06, 170.09, 176.63, 150.15, 148.90, 142.82, 140.36, 139.56]

vals_14 = thermo_tables(T_14, Cp_14, H_sat_14, S_sat_14, liq_index = 17, vap_index = 18)
table_14 = create_table(vals_14, 368.76, H_sat_14, S_sat_14)

'''
Enthalpy - Entropy values at Pressure = 1.6 and different temperatures.
'''

H_sat_16 = [32665.2, 47338.3]
S_sat_16 = [267.065, 306.130]

T_16 = [200.000, 210.000, 220.000, 230.000, 240.000, 250.000, 260.000, 270.000, 280.000, 290.000, 300.000, 310.000, 320.000, 330.000,
        340.000, 350.000, 360.000, 370.000, 375.61, 375.61, 380.000, 390.000, 400.000]

Cp_16 = [118.74, 120.13, 121.8, 123.73, 125.88, 128.24, 130.8, 133.53, 136.45, 139.55, 142.85, 146.37, 150.14, 154.21, 158.69, 163.71,
         169.56, 176.87, 182.10, 159.3, 153.78, 147.2, 144.38]

vals_16 = thermo_tables(T_16, Cp_16, H_sat_16, S_sat_16, liq_index = 18, vap_index = 19)
table_16 = create_table(vals_16, 375.61, H_sat_16, S_sat_16)

'''
Linear interpolations
'''

def find_T_limits(T, table):
    for temperature in table.keys():
        temperature = float(temperature)
        if temperature < T:
          T_prev = temperature
        if temperature > T:
          T_next = temperature
          break
    return T_prev, T_next

def linear_interpolate_enthalpy(T_prev, T_next, table, T):
    value = ((table[T_next]['enthalpy'] - table[T_prev]['enthalpy']) * (T - float(T_prev))) / (float(T_next) - float(T_prev)) + table[T_prev]['enthalpy']
    return value

def linear_interpolate_entropy(T_prev, T_next, table, T):
    value = ((table[T_next]['entropy'] - table[T_prev]['entropy']) * (T - float(T_prev))) / (float(T_next) - float(T_prev)) + table[T_prev]['entropy']
    return value


def find_T_limits_wrt_H(H, table):
    for temp in table.keys():
        try:
            if table[temp]['enthalpy'] < H:
                T_prev = temp
            if table[temp]['enthalpy'] > H:
                T_next = temp
                break
        except:
            continue
    return T_prev, T_next

def linear_interpolate_temp_wrt_enthalpy(T_prev, T_next, table, H):
    value = ((float(T_next) - float(T_prev)) * (H - table[T_prev]['enthalpy'])) / (table[T_next]['enthalpy'] - table[T_prev]['enthalpy']) + float(T_prev)
    return value


def find_T_limits_wrt_S(S, table):
    for temp in table.keys():
        try:
            if table[temp]['entropy'] < S:
                T_prev = temp
            if table[temp]['entropy'] > S:
                T_next = temp
                break
        except:
            continue
    return T_prev, T_next

def linear_interpolate_temp_wrt_entropy(T_prev, T_next, table, S):
    value = ((float(T_next) - float(T_prev)) * (S - table[T_prev]['entropy'])) / (table[T_next]['entropy'] - table[T_prev]['entropy']) + float(T_prev)
    return value


def sup(P, T, table_14, table_16, table_01):
    if P == 1.4:
        table = table_14
    elif P == 1.6:
        table = table_16

    if T in table.keys():
        H1 = table[T]['enthalpy']
        S1 = table[T]['entropy']
    else:
        try:
            T_prev, T_next = find_T_limits(T, table)
        except:
            return print("Final value of temperature {} K not found in thermo table".format(T))
        H1 = linear_interpolate_enthalpy(T_prev, T_next, table, T)
        S1 = linear_interpolate_entropy(T_prev, T_next, table, T)

    H_sat_l = table_01['H_sat'][0]
    H_sat_v = table_01['H_sat'][1]

    S_sat_l = table_01['S_sat'][0]
    S_sat_v = table_01['S_sat'][1]

    H_sat_l_initial = table['H_sat'][0]
    H_sat_v_initial = table['H_sat'][1]

    S_sat_l_initial = table['S_sat'][0]
    S_sat_v_initial = table['S_sat'][1]

    if T < table['T_sat']:

        print("When Del(H) = 0")
        H2 = H1
        if H2 > H_sat_l and H2 < H_sat_v:
            T2 = table_01['T_sat']
            x2 = (H2 - H_sat_l) / (H_sat_v - H_sat_l)
            print("Temperature of exit stream: ", T2, "K")
            print("Quality of exit stream: ", x2)
            print("Phase of exit stream: Liquid vapor coexistence ")

        if H2 <= H_sat_l or H2 >= H_sat_v:
            T2 = 0
            for temp in table_01.keys():
                try:
                    if H2 == table_01[temp]['enthalpy']:
                        T2 = float(temp)
                except:
                    pass
            if T2 == 0:
                try:
                    T_prev, T_next = find_T_limits_wrt_H(H2, table_01)
                except:
                    return print("Final value of enthalpy {} J J not found in thermo table".format(H2))
                T2 = linear_interpolate_temp_wrt_enthalpy(T_prev, T_next, table_01, H2)

            print("Temperature of exit stream: ", T2, "K")

            if H2 <= H_sat_l:
                if T2 == table_01['T_sat']:
                    print("Phase of exit stream: Saturated Liquid")
                else:
                    print("Phase of exit stream: Sub-Cooled Liquid ")
            else:
                if T2 == table_01['T_sat']:
                    print("Phase of exit stream: Saturated Vapor")
                else:
                    print("Phase of exit stream: Super-Heated Vapor")


        print("\nFor maximum attainable work, Del(S) = 0")

        S2 = S1
        if S2 > S_sat_l and S2 < S_sat_v:
            T2 = table_01['T_sat']
            x2 = (S2 - S_sat_l) / (S_sat_v - S_sat_l)
            H2 = x2 * H_sat_v + (1 - x2) * H_sat_l
            print("Maximum attainable work (H2 - H1): ", H2 - H1, "J")
            print("Temperature of exit stream: ", T2, "K")
            print("Quality of exit stream: ", x2)
            print("Phase of exit stream: Liquid vapor coexistence ")

        if S2 <= S_sat_l or S2 >= S_sat_v:
            T2 = 0
            H2 = 0
            for temp in table_01.keys():
                try:
                    if S2 == table_01[temp]['entropy']:
                        T2 = float(temp)
                        H2 = table_01[temp]['enthalpy']
                except:
                    pass
            if T2 == 0:
                try:
                    T_prev, T_next = find_T_limits_wrt_S(S2, table_01)
                except:
                    return print("Final value of entropy {} J not found in thermo table".format(S2))
                T2 = linear_interpolate_temp_wrt_entropy(T_prev, T_next, table_01, S2)
                H2 = linear_interpolate_enthalpy(T_prev, T_next, table_01, T2)

            print("Maximum attainable work (H2 - H1): ", H2 - H1, "J")
            print("Temperature of exit stream: ", T2, "K")

            if S2 <= S_sat_l:
                if T2 == table_01['T_sat']:
                    print("Phase of exit stream: Saturated Liquid")
                else:
                    print("Phase of exit stream: Sub-Cooled Liquid ")
            else:
                if T2 == table_01['T_sat']:
                    print("Phase of exit stream: Saturated Vapor")
                else:
                    print("Phase of exit stream: Super-Heated Vapor")


    if T == table['T_sat']:
        x1 = float(input("Enter the quality (since T1 = Tsat): "))
        print("")

        H1 = x1 * H_sat_v_initial + (1 - x1) * H_sat_l_initial
        S1 = x1 * S_sat_v_initial + (1 - x1) * S_sat_l_initial

        print("When Del(H) = 0")
        H2 = H1
        if H2 > H_sat_l and H2 < H_sat_v:
            T2 = table_01['T_sat']
            x2 = (H2 - H_sat_l) / (H_sat_v - H_sat_l)
            print("Temperature of exit stream: ", T2, "K")
            print("Quality of exit stream: ", x2)
            print("Phase of exit stream: Liquid vapor coexistence ")

        if H2 >= H_sat_v:
            T2 = 0
            for temp in table_01.keys():
                try:
                    if H2 == table_01[temp]['enthalpy']:
                        T2 = float(temp)
                except:
                    pass
            if T2 == 0:
                try:
                    T_prev, T_next = find_T_limits_wrt_H(H2, table_01)
                except:
                    return print("Final value of enthalpy {} J not found in thermo table".format(H2))
                T2 = linear_interpolate_temp_wrt_enthalpy(T_prev, T_next, table_01, H2)

            print("Temperature of exit stream: ", T2, "K")

            if T2 == table_01['T_sat']:
                print("Phase of exit stream: Saturated Vapor")
            else:
                print("Phase of exit stream: Super-Heated Vapor")


        print("\nFor maximum attainable work, Del(S) = 0")
        S2 = S1
        if S2 > S_sat_l and S2 < S_sat_v:
            T2 = table_01['T_sat']
            x2 = (S2 - S_sat_l) / (S_sat_v - S_sat_l)
            H2 = x2 * H_sat_v + (1 - x2) * H_sat_l
            print("Maximum attainable work (H2 - H1): ", H2 - H1, "J")
            print("Temperature of exit stream: ", T2, "K")
            print("Quality of exit stream: ", x2)
            print("Phase of exit stream: Liquid vapor coexistence ")

        if S2 >= S_sat_v:
            T2 = 0
            H2 = 0
            for temp in table_01.keys():
                try:
                    if S2 == table_01[temp]['entropy']:
                        T2 = float(temp)
                        H2 = table_01[temp]['enthalpy']
                except:
                    pass
            if T2 == 0:
                try:
                    T_prev, T_next = find_T_limits_wrt_S(S2, table_01)
                except:
                    return print("Final value of entropy {} J not found in thermo table".format(S2))
                T2 = linear_interpolate_temp_wrt_entropy(T_prev, T_next, table_01, S2)
                H2 = linear_interpolate_enthalpy(T_prev, T_next, table_01, T2)

            print("Maximum attainable work (H2 - H1): ", H2 - H1, "J")
            print("Temperature of exit stream: ", T2, "K")

            if T2 == table_01['T_sat']:
                print("Phase of exit stream: Saturated Vapor")
            else:
                print("Phase of exit stream: Super-Heated Vapor")


    if T1 > table['T_sat']:

        print("When Del(H) = 0")
        H2 = H1
        T2 = 0
        for temp in table_01.keys():
            try:
                if H2 == table_01[temp]['enthalpy']:
                    T2 = float(temp)
            except:
                pass
        if T2 == 0:
            try:
                T_prev, T_next = find_T_limits_wrt_H(H2, table_01)
            except:
                return print("Final value of enthalpy {} J not found in thermo table".format(H2))
            T2 = linear_interpolate_temp_wrt_enthalpy(T_prev, T_next, table_01, H2)

        print("Temperature of exit stream: ", T2, "K")
        print("Phase of exit stream: Super-Heated Vapor")

        print("\nFor maximum attainable work, Del(S) = 0")
        S2 = S1
        T2 = 0 # let
        H2 = 0 # let
        for temp in table_01.keys():
            try:
                if S2 == table_01[temp]['entropy']:
                    T2 = float(temp)
                    H2 = table_01[temp]['enthalpy']
            except:
                pass
        if T2 == 0:
            try:
                T_prev, T_next = find_T_limits_wrt_S(S2, table_01)
            except:
                return print("Final value of entropy {} J not found in thermo table".format(S2))
            T2 = linear_interpolate_temp_wrt_entropy(T_prev, T_next, table_01, S2)
            H2 = linear_interpolate_enthalpy(T_prev, T_next, table_01, T2)

        print("Maximum attainable work (H2 - H1): ", H2 - H1, "J")
        print("Temperature of exit stream: ", T2, "K")
        print("Phase of exit stream: Super-Heated Vapor")


P1 = float(input("\nEnter the inlet pressure (in MPa) : "))
T1 = float(input("Enter the inlet temperature (in K): "))
print("")
if P1 not in [1.4, 1.6]:
    print("Invalid value of pressure (must be 1.4 or 1.6 MPa)")
elif T1 < 200 or T1 > 400:
    print("Invalid value of temperature (must be between 200 to 400 K)")
else:
    sup(P1, T1, table_14, table_16, table_01)
