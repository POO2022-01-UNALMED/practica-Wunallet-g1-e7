# Documentación capa UI

## Banquero

### Generalidades

Funcionalidades que ejecutará:

1. Inscribir cuenta
2. Romper topes
3. Solicitar crédito
4. Ver historial de transacciones
5. Transferir

### Estado inicial

### Bancos 

Todos los bancos tienen los 3 tipos de cuentas

- Unalombia
- PooBanco
- QuitaVivienda

### Juan Perez

#### Atributos


### Pantallas

---
***Inicio***

¿Qué usuario desea seleccionar?

1. Juan Perez
2. Hernesto Perez

---
***Inicio.Funcionalidades***

¿Qué desea hacer?

1. Inscribir cuenta
2. Romper topes
3. Solicitar crédito
4. Ver historial de transacciones
5. Transferir
9. Salida segura
0. Volver al menú de usuarios

---
#### Inscribir cuenta
---

***InscribirCuenta.SeleccionBanco***

Seleccione de qué banco es la cuenta que desea inscribir

1. Unalombia 
2. PooBanco
3. QuitaVivienda 
0. Volver al menú de funcionalidades 

---
***InscribirCuenta.SeleccionTipoCuenta***

Seleccione el tipo de cuenta

1. Cuenta de bajo monto
2. Cuenta de ahorros
3. Cuenta corriente
0. Volver al menú de funcionalidades 

---
***InscribirCuenta.IngresoNumeroCuenta***

Ingrese el número de cuenta

\--------

(Leer desde la consola)

**Nota** El comportamiento por defecto será rechazar todos los números que se ingresen excepto si es de alguno de los usuarios 
ya creados.

---
***InscribirCuenta.IngresoCedula***

Ingrese el número de cédula del titular de la cuenta que desea inscribir

\--------

(Leer desde la consola)

**Nota** Rechazará todos los números excepto si es de alguno de los usuarios ya creados.

---
***InscribirCuenta.Error***

Esta cuenta no existe, por favor compruebe los datos.

1. Reingresar los datos de inscripcion
9. Salida segura
0. Volver al menú de funcionalidades 

---
***InscribirCuenta.Aprobacion***

Cuenta inscrita exitosamente.

9. Salida segura
0. Volver al menú de funcionalidades.

---
#### Romper topes

::**NOTA Comprobacion de que existe una cuenta de bajo monto asociada al usuario -> Es necesario implementar este chequeo en 
la lógica!!**::

---
***RomperTopes.SinCuentaBajoMonto***

Esta funcionalidad no está habilitada para tus cuentas.

9. Salida segura
0. Volver al menú de funcionalidades.

---
***RomperTopes.ConCuentaBajoMonto***

¡Recuerde! El procedimiento de romper topes consiste en transformar su cuenta de tipo Bajo monto, a una cuenta de ahorros
convencional, eliminando las limitaciones de este tipo de cuentas. Este proceso tiene un costo de 15.000 pesos que pagará una única vez.

Para continuar seleccione la cuenta de bajo monto que desea transformar

1. Cuenta x
\<2. Cuenta y \> // Opcional
\<3. Cuenta z \> // Opcional

(Leer entrada, que corresponderá al índice + 1 de la lista cuentasAsociadas) 

0. Volver al menú de funcionalidades.

---
***RomperTopes.ConCuentaBajoMonto.Espera***

Un asesor está verificando tu solicitud.

sleep 3

---
***RomperTopes.ConCuentaBajoMonto.Error***

Tu solicitud ha sido rechazada ya que no cuentas con saldo suficiente en tu cuenta para realizar el proceso.

9. Salida segura
0. Volver al menú de funcionalidades.

---
***RomperTopes.ConCuentaBajoMonto.Aprobación***

Tu solicitud ha sido aprobada, se descontará 15.000 de tu saldo para realizar el proceso. Espera un momento...

sleep 3

Tu cuenta ha sido actualizada y ahora no tiene topes.

9. Salida segura
0. Volver al menú de funcionalidades.

---
#### Solicitar crédito
---
***SolicitarCredito.SeleccionBanco***

Con qué banco desea solicitar el crédito:

- UNALombia \<tasa de interés del banco\>
- POOBanco \<tasa de interés del banco\>
- QuitaVivienda \<tasa de interés del banco\> **Nota** El 36% de Daniel

---
***SolicitarCredito.IngresoMonto***

Ingrese el monto en pesos a solicitar:

\------

---
***SolicitarCredito.IngresoPlazos***

Ingrese el plazo en meses del crédito:

\------

---
***SolicitarCredito.Espera***

Un asesor está verificando tu solicitud.

sleep 3

---
***SolicitarCredito.Error***

Tu solicitud de crédito ha sido rechazada.

9. Salida segura
0. Volver al menú de funcionalidades.

---
***SolicitarCredito.Aprobación***

Tu solicitud de crédito ha sido aprobada y tu saldo ha sido actualizado con el monto solicitado.

9. Salida segura
0. Volver al menú de funcionalidades.

---
#### Ver historial de transacciones
---
***VerHistorial.SeleccionBanco***

Seleccione de qué banco es la cuenta que desea consultar

1. \< Banco asociado 1 \>
2. \< Banco asociado 2 \>
3. \< Banco asociado 3 \>

(Leer entrada, que corresponderá al índice + 1 de la lista bancosAsociados)
0. Volver al menú de funcionalidades 

---
***VerHistorial.SeleccionCuenta***

Para continuar seleccione la cuenta a consultar

1. Cuenta x
\<2. Cuenta y \> // Opcional
\<3. Cuenta z \> // Opcional

(Leer entrada, que corresponderá al índice + 1 de la lista cuentasAsociadas) 

0. Volver al menú de funcionalidades 

---
***VerHistorial.Historial***

El historial de transacciones de su cuenta es

Ejemplos de mensaje

Para transferencias
Transferencia de \<nroCuentaOrigen\> a \<nroCuentaDestino\> por valor de <valor>.

Para pago de créditos
Transferencia de \<nroCuentaOrigen\> a \<nombreBanco\> por valor de <valor>.

9. Salida segura
0. Volver al menú de funcionalidades.

---
#### Transferir
---
***Transferir.SeleccionCuentaOrigen***

Selecciona el producto de origen que quieres usar

1. Cuenta 1 de las cuentas asociadas con saldo \<saldo\>
2. Cuenta 2 ....

(Leer entrada, que corresponderá al índice + 1 de la lista cuentasAsociadas) 

0. Volver al menú de funcionalidades.

---
***Transferir.SeleccionTipoTransferencia***

Selecciona qué tipo de transferencia quieres hacer

1. Pagar crédito.
2. Transferencia a otra cuenta.
0. Volver al menú de funcionalidades.

---
***Transferir.PagarCredito.SinCredito***

No tienes ningún crédito activo para pagar.

9. Salida segura
0. Volver al menú de funcionalidades.

---
***Transferir.PagarCredito.ConCredito***

Tu crédito es de \< Deuda \> y pagarás una cuota de \< cuotaMensual \>.

¿Quieres continuar con el pago de tu crédito?

1. Si

0. Volver al menú de funcionalidades.
---
***Transferir.PagarCredito.ConCredito.Espera***

Un asesor está verificando tu solicitud.

sleep 3

---
***Transferir.PagarCredito.ConCredito.Rechazo***

Tu pago ha sido rechazado ya que no cuentas con saldo suficiente en tu producto de origen.

9. Salida segura
0. Volver al menú de funcionalidades.

---
***Transferir.PagarCredito.ConCredito.Aprobacion***

Tu pago ha sido exitoso. Tu credito restante es de \< Deuda - Pago \>.

9. Salida segura
0. Volver al menú de funcionalidades.

---
***Transferir.OtraCuenta.SeleccionTipoInscripcion***

Selecciona a qué tipo de cuenta quieres transferir

1. Cuentas inscritas
2. Cuentas no inscritas
0. Volver al menú de funcionalidades.

---
***Transferir.OtraCuenta.Inscritas***

Seleccione la cuenta de destino

1. Cuenta inscrita 1
2. Cuenta inscrita 2... // Salen del array de listaInscritos

(Leer entrada, que corresponderá al índice + 1 de la lista cuentasAsociadas) 

0. Volver al menú de funcionalidades.

---
***Transferir.OtraCuenta.Inscritas.IngresoValor***

Digite el valor que desea transferir

\---------------

0. Volver al menú de funcionalidades.

---
***Transferir.OtraCuenta.Inscritas.Rechazo***

Envío rechazado. El saldo de su cuenta es insuficiente para realizar el movimiento.

9. Salida segura
0. Volver al menú de funcionalidades.

---
***Transferir.OtraCuenta.Inscritas.Aprobacion***

Envío exitoso. El saldo de su cuenta es de \<saldo - envío \>.

9. Salida segura
0. Volver al menú de funcionalidades.
---
***Transferir.OtraCuenta.NoInscritas.SeleccionBanco***

Seleccione el banco de la cuenta destino:

1. Unalombia 
2. PooBanco
3. QuitaVivienda 

0. Volver al menú de funcionalidades.
---
***Transferir.OtraCuenta.NoInscritas.IngresoNumeroCuenta***

Ingrese el número de cuenta de destino:


0. Volver al menú de funcionalidades.

---
***Transferir.OtraCuenta.NoInscritas.IngresoValor***

Digite el valor que desea transferir

\------

0. Volver al menú de funcionalidades.

---
***Transferir.OtraCuenta.NoInscritas.Rechazo***

Hubo un error en la operación. Verifique que su cuenta de origen tenga y permita mover el saldo indicado, o que la cuenta de 
destino exista.

9. Salida segura
0. Volver al menú de funcionalidades.

---
***Transferir.OtraCuenta.NoInscritas.Aprobacion***

Envío exitoso. El saldo de su cuenta es de \<saldo - envío \>.

9. Salida segura
0. Volver al menú de funcionalidades.
---

### Atributos

### Métodos

