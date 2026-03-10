# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pagos_extra = 1000
mes = 0

while saldo > 0:
    while mes < 12:
        saldo = saldo * (1+tasa/12) - pago_mensual - pagos_extra
        total_pagado = total_pagado + pago_mensual + pagos_extra
        mes = mes + 1
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    mes = mes + 1
print('Total pagado en', mes, 'meses: ', round(total_pagado, 2))

