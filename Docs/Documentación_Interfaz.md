# Documentación capa UI

## Banquero

### Generalidades

- Funcionalidades que ejecutará:

1. Inscribir cuenta
2. Romper topes
3. Solicitar crédito
4. Ver historial de transacciones
5. Transferir

### Estado inicial

### Bancos 

Todos los bancos tienen los 3 tipos de cuentas

- Unalombia
- Poobanco
- QuitaVivienda

### Juan Perez

#### Atributos


### Main

---

¿Qué usuario desea seleccionar?

1. Juan Perez
2. Hernesto Perez

---
¿Qué desea hacer?

1. Inscribir cuenta
2. Romper topes
3. Solicitar crédito
4. Ver historial de transacciones
5. Transferir
9. Salida segura
0. Volver al menú de usuarios

#### Inscribir cuenta

Seleccione de qué banco es la cuenta que desea inscribir

1. Unalombia 
2. PooBanco
3. QuitaVivienda 
0. Volver al menú de funcionalidades 

---
Seleccione el tipo de cuenta

1. Cuenta de bajo monto
2. Cuenta de ahorros
3. Cuenta corriente
0. Volver al menú de funcionalidades 

---
Ingrese el número de cuenta

\--------

(Leer desde la consola)

**Nota** El comportamiento por defecto será rechazar todos los números que se ingresen excepto si es de alguno de los usuarios 
ya creados.


---
Ingrese el número de cédula

\--------

(Leer desde la consola)

**Nota** Rechazará todos los números excepto si es de alguno de los usuarios ya creados.

---
*Interfaz de error*

Esta cuenta no existe, por favor compruebe los datos.

1. Reingresar los datos de inscripcion
9. Salida segura
0. Volver al menú de funcionalidades 

---
*Interfaz de aprobación*

Cuenta inscrita exitosamente.

9. Salida segura
0. Volver al menú de funcionalidades.
---

#### Romper topes

::**NOTA Comprobacion de que existe una cuenta de bajo monto asociada al usuario -> Es necesario implementar este chequeo en 
la lógica!!**::

---
Caso 1 : El usuario no tiene cuenta de bajo monto.

Esta funcionalidad no está habilitada para tus cuentas.

9. Salida segura
0. Volver al menú de funcionalidades.

---
Caso 2 : El usuario tiene una cuenta de bajo monto.

¡Recuerde! El procedimiento de romper topes consiste en transformar su cuenta de tipo Bajo monto, a una cuenta de ahorros
convencional, eliminando las limitaciones de este tipo de cuentas. Este proceso tiene un costo de 15.000 pesos que pagará una única vez.

Para continuar seleccione la cuenta de bajo monto que desea transformar

1. Cuenta x
\<2. Cuenta y \> // Opcional
\<3. Cuenta z \> // Opcional

0. Volver al menú de funcionalidades.

---

Un asesor está verificando tu solicitud.

sleep 3

---
*Interfaz de error*
Tu solicitud ha sido rechazada ya que no cuentas con saldo suficiente en tu cuenta para realizar el proceso.

9. Salida segura
0. Volver al menú de funcionalidades.

---
*Interfaz de aprobación*

Tu solicitud ha sido aprobada, se descontará 15.000 de tu saldo para realizar el proceso. Espera un momento...

sleep 3

Tu cuenta ha sido actualizada y ahora no tiene topes.

9. Salida segura
0. Volver al menú de funcionalidades.


#### Solicitar crédito

---
Caso 1 : El usuario no tiene cuenta de bajo monto.

Esta funcionalidad no está habilitada para tus cuentas.

9. Salida segura
0. Volver al menú de funcionalidades.

---
Caso 2 : El usuario tiene una cuenta de bajo monto.

¡Recuerde! El procedimiento de romper topes consiste en transformar su cuenta de tipo Bajo monto, a una cuenta de ahorros
convencional, eliminando las limitaciones de este tipo de cuentas. Este proceso tiene un costo de 15.000 pesos que pagará una única vez.

Para continuar seleccione la cuenta de bajo monto que desea transformar

1. Cuenta x
\<2. Cuenta y \> // Opcional
\<3. Cuenta z \> // Opcional

0. Volver al menú de funcionalidades.

---

### Atributos

### Métodos

