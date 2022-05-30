# Documentación Capa Gráfica

## Banquero

### Generalidades

Funcionalidades que ejecutará:

1. Inscribir cuenta
2. Romper topes
3. Solicitar crédito
4. Ver historial de transacciones
5. Transferir

### Estado inicial

### Atributos

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
***SolicitarCredito.VerificacionCreditoActivo***

Se verifica que el usario ya no tenga un credito activo, si el usuario tiene un crédito activo entonces se mostará en pantalla "El usuario " \<Cc usuario\>" ya tiene un crédito activo".

---
***SolicitarCredito.SeleccionBanco***

Con qué banco desea solicitar el crédito:

- UNALombia \<tasa de interés del banco\>
- POOBanco \<tasa de interés del banco\>
- QuitaVivienda \<tasa de interés del banco\> **Nota** El 36% de Daniel

---

***SolicitarCredito.SolicitarCuenta***

En que cuenta desa guardar el credito

1. Cuenta x

2. Cuenta y  // Opcional

3. Cuenta z // Opcional

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
***VerHistorial.SeleccionCuenta***

Para continuar seleccione la cuenta a consultar

1. Cuenta x
\<2. Cuenta y \> // Opcional
\<3. Cuenta z \> // Opcional

(Leer entrada, que corresponderá al índice + 1 de la lista cuentasAsociadas) 

0. Volver al menú de funcionalidades 

---
***VerHistorial.Historial.SinHistorial***
No tiene transacciones por mostrar.

9. Salida segura
0. Volver al menú de funcionalidades.
---
***VerHistorial.Historial.ConHistorial***

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

Tu pago ha sido rechazado ya que no cuentas con saldo suficiente o  tu producto de origen no permite mover el valor indicado.

9. Salida segura
0. Volver al menú de funcionalidades.

---
***Transferir.PagarCredito.ConCredito.Aprobacion***

Tu pago ha sido exitoso. Tu credito restante es de \< Deuda - Pago \>.

9. Salida segura
0. Volver al menú de funcionalidades.

---
***Transferir.OtraCuenta.SeleccionStatusDeInscripcion***

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
***Transferir.OtraCuenta.Inscritas.Error***

La cuenta inscrita que ha seleccionado ya no está disponible, por lo tanto será eliminada de su lista de cuentas inscritas.

0. Volver al menú de funcionalidades.

---
***Transferir.OtraCuenta.Inscritas.IngresoValor***

Digite el valor que desea transferir

\---------------

0. Volver al menú de funcionalidades.

---
***Transferir.OtraCuenta.Inscritas.Rechazo***

Hubo un error en la operación. Verifique que su cuenta de origen tenga y permita mover el saldo indicado.

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

### Funcionalidades/Métodos

#### - inscribirCuenta(Usuario usuario)

**Funcionamiento:**

1. Se muestra la pantalla InscribirCuenta.SeleccionBanco donde el entero ingresado por el usuario es el índice + 1 del nombre
contenido en la lista Banco.listaBancos. Este nombre se debe extraer de la lista y asignársele a la variable nombreBanco.

2. Se muestra la pantalla InscribirCuenta.SeleccionTipoCuenta, donde el entero que ingrese el usuario determinará el String que se
le asignará a la variable tipoCuenta (puede ser ahorro, bajo monto o corriente).

3. Desde la pantalla InscribirCuenta.IngresoNumeroCuenta se asigna el entero que ingresó el usuario a la variable nroCuenta.

4. Desde InscribirCuenta.IngresoCedula se asigna el entero que ingresó el usuario a la variable cc(cédula).

5. Se realiza el llamado al método de usuario inscribir(int cc, int nroCuenta, String tipoCuenta, String nombreBanco)

    1. En caso de que falle el método se muestra la pantalla InscribirCuenta.Error

    2. En caso de que la inscripción sea exitosa se muestra la pantalla InscribirCuenta.Aprobacion

#### - romperTopes(Usuario usuario)

**Funcionamiento:**

1. 


#### - solicitarCredito(Usuario usuario)

**Funcionamiento:**



#### - verHistorial(Usuario usuario)

**Funcionamiento:**

1. Se imprime la lista de cuentas asociadas al usuario con la pantalla VerHistorial.SeleccionCuenta. La selección del usuario es el índice + 1 de la lista cuentasAsociadas del usuario. Esta cuenta se asignará a la variable cuenta.

2. Se llama al método verHistorial de la clase cuenta ejecutándolo desde la cuenta seleccionada en el paso anterior.
    
    Dependiendo de si la cuenta tiene o no transacciones por mostrar, se mostrará

    1. VerHistorial.Historial.SinHistorial en caso de que el Array esté vacío

    2. VerHistorial.Historial.ConHistorial en caso de que el Array tenga transacciones.

    

#### - transferencia(Usuario usuario)

**Funcionamiento:**

1. Imprime los atributos importantes de cada cuenta en la lista cuentasAsociadas y asigna la cuenta que corresponde al indice 
seleccionado en una variable cuentaOrigen

2. Se selecciona el tipo de transferencia que se desea hacer

    1. Selección de pago de crédito

        Se verifica que el usuario tenga un crédito Activo

        1. Si no tiene, se muestra la pantalla Transferir.PagarCredito.SinCredito

        2. Si tiene, se muestra la pantalla Transferir.PagarCredito.ConCredito preguntando si se confirma el pago

            En caso de confirmación se ejecuta el método abstracto de la clase Cuenta que tiene como firma 
            transferencia(Credito credito)

            1. Si la transferencia no se pudo realizar por falta de saldo en la cuenta de origen, se mostrará la pantalla
            Transferir.PagarCredito.ConCredito.Rechazo

            2. Si la transferencia se realiza exitosamente se muestra la pantalla Transferir.PagarCredito.ConCredito.Aprobacion


    2. Transferencia a otra cuenta

        Se muestra la pantalla Transferir.OtraCuenta.SeleccionStatusDeInscripcion
        
        1. Si se seleccionan cuentas inscritas, se muestra la pantalla Transferir.OtraCuenta.Inscritas. El entero ingresado en la
        interfaz es el índice + 1 de la lista listaInscritos. Este índice se usará para extraer el objeto de tipo Cuenta
        correspondiente y asignarlo a la variable cuentaDestino. 

        Es necesario revisar que exista la cuenta seleccionada en la listaCuentas del banco. De no ser así, significa que la cuenta
        ya no existe para el banco (pasó de bajo monto a ahorro) y por lo tanto se mostrará la pantalla
        Transferir.OtraCuenta.Inscritas.Error y se eliminará de la listaInscritos del usuario dicha cuenta.

            Luego desde la pantalla Transferir.OtraCuenta.Inscritas.IngresoValor se asigna el float ingresado a la variable 
            valorTransferencia.

            Se llama al método abstracto de la clase Cuenta que tiene como firma 
            transferir(Cuenta cuentaDestino, float valorTransferencia)

            1. Si la transferencia se rechaza se muestra la pantalla Transferir.OtraCuenta.Inscritas.Rechazo

            2. Si la transferencia se aprueba se muestra la pantalla Transferir.OtraCuenta.Inscritas.Aprobacion

        2. Si se selecciona cuentas no inscritas se mostrará la pantalla Transferir.OtraCuenta.NoInscritas.SeleccionBanco. La
        selección del usuario es el índice + 1 de la lista listaBancos de la clase Banco, que contiene los nombres de los bancos. 
        Luego se llama al método estático extraerBanco(String nombreBanco) que retornará el objeto tipo Banco y este se debe
        asociar a la variable bancoDestino.

            Luego se muestra la pantalla Transferir.OtraCuenta.NoInscritas.IngresoNumeroCuenta, y el entero ingresado se asignará a la 
            variable nroCuentaDestino.

            Posteriormente se muestra la pantalla Transferir.OtraCuenta.NoInscritas.IngresoValor, y el float ingresado se asignará a
            la variable valorTransferencia

            Se llama al método abstracto de Cuenta con firma
            transferir(Cuenta cuentaDestino, float valorTransferencia)

            1. En caso de que falle el método se mostrará la pantalla Transferir.OtraCuenta.NoInscritas.Rechazo

            2. En caso de que se transfiera exitosamente se mostrará la pantalla Transferir.OtraCuenta.NoInscritas.Aprobacion

