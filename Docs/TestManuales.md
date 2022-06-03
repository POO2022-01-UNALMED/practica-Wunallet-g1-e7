# Testeo manual de las funcionalidades

### Creación de algunos bancos

```java
Banco Unalombia = new Banco("Unalombia",(float)1.6);
Banco PooBanco = new Banco("PooBanco",(float)2.5);
Banco QuitaVivienda = new Banco("QuitaVivienda",(float)36.0);
```

---
### Creación de algunos usuarios
---
	
```java
Usuario juanPerez = new Usuario(null,1000000,10,null);

Usuario hernestoPerez = new Usuario(null,1000000,98,null);
```

---
### Creación de algunas cuentas
---
<!-- 
//	Ahorro(int nroCuenta, Usuario titular,float saldo,Banco banco,String tipoDeCuenta,float tasaDeInteres)
//	BajoMonto(int nroCuenta, Usuario titular,float saldo,Banco banco,String tipoDeCuenta,float tasaDeInteres,float limiteMensual,float acumuladorTransferencia) 
//	Corriente(int nroCuenta, Usuario titular,float saldo,Banco banco,String tipoDeCuenta,float sobregiroActual) -->

```java
Cuenta cuenta1 = new Ahorro(89,juanPerez, (float)10000.0 ,QuitaVivienda,"ahorro",(float)36.0);

Cuenta cuenta2 = new BajoMonto(69,hernestoPerez, (float)1000000.0,PooBanco, "bajoMonto", (float)5.0,(float)3000000.0,(float)3000000.0);

Cuenta cuenta3 = new Corriente(23,juanPerez,(float)50000000.0,Unalombia,"corriente",(float)2000000);

Cuenta cuenta4 = new BajoMonto(26,hernestoPerez, (float)6000000.0,Unalombia, "bajoMonto", (float)5000.0,(float)3000.0,(float)3000.0);

```
	
---
## Funcionalidad inscribir cuenta
---
- ### **¿Que usuario desea realizar?**
    El primer usuario con **C: 10** quiere inscribir una cuenta

    - **Primera selección: 1**
    
    - **Seleección de la funcionalidad: 1**
---

- ### **Caso 1: (El número de cuenta NO exite en el banco):**

    - Seleccione de que banco es la cuenta que desea inscribir: **1**

        - **Usted seleccionó Unalombia**

    - Seleccione el tipo de cuenta: **1**

        - **Usted seleccionó bajomonto**

    - Seleccione el número de cuenta: **69**

        - **Numero de cuenta 1 no existe en el banco: Unalombia**

---

- ### **Caso 2: (El número de cuenta exite en el banco):** 
        
    - Seleccione de que banco es la cuenta que desea inscribir: **1**

        - **Usted seleccionó Unalombia**

    - Seleccione el tipo de cuenta: **1**

        - **Usted seleccionó bajoMonto**
    
    - Seleccione el número de cuenta: **26**

    - Seleccione el número de cedula: **98**

        - **Las cuentas inscritas del usuario 10 son: 26**

---

- ### **Caso 3: (El número de cuenta exite en el banco):** 

    - Seleccione de que banco es la cuenta que desea inscribir: **2**

        - **Usted seleccionó PooBanco**

    - Seleccione el tipo de cuenta: **1**

        - **Usted seleccionó bajomonto**

    - Seleccione el número de cuenta: **69**

    - Seleccione el número de cedula: **98**

        - **Las cuentas inscritas del usuario 10 son: 26 69**


---
- ### **¿Que usuario desea usar?**
    - hernestoPerez

    **No tendrá cuentas inscritas**
---



---
## Funcionalidad romperTopes
---


- ## ***¿Que usuario desea realizar?***
    El primer usuario con **C: 10** quiere romper topes a sus cuentas

    - juanPerez
---
---
- ### **Caso 1: (No tiene cuentas de bajo monto):**
    - Esta funcionalidad no está habilitada para tus cuentas.
---
---
- ## ***¿Que usuario desea realizar?***
    El segundo usuario con **C: 98** quiere romper topes a sus cuentas
    - hernestoPerez

    - **Seleección de la funcionalidad: 2**
---

- ### **Caso 1: (Si tiene cuentas de bajo monto):**
    -  
        - **¡Recuerde! El procedimiento de romper topes consiste en transformar su cuenta de tipo Bajo monto, a una cuenta de ahorros convencional, eliminando las limitaciones de este tipo de cuentas. Este proceso tiene un costo de 15.000 pesos que pagará una única vez.**
    - Para continuar seleccione la cuenta de bajo monto que desea transformar: **1**

        - **Tu solicitud ha sido aprobada, se descontarÃ¡ 15.000 de tu saldo para realizar el proceso. Espera un momento...**

        - **Tu cuenta ha sido actualizada y ahora no tiene topes.** 

        - **Tu nueva cuenta de ahorros ahora tiene un saldo de: \<SaldoCuentaAhorros\>.**
    
---
## Funcionalidad solicitarCredito
---
Nota: Puede que los pasos que se crean a continuación no se ejecuten en el sistema de manera similar si no se deseliazila, esto se debe a que se tienen una comprobación aleatoria (Ver documentación, asignación de ***comportamientoPago***)

---
- ## ***¿Que usuario desea realizar?***
    
    El segundo usuario con **C: 10** solicitar un crédito
    
    - juanPerez

    - **Seleección de la funcionalidad: 3**
---


- ### **Caso 1: (Aprovación del crédito):** 
**NOTA:** Todos los usuarios inician sin ningún crédito.

- Seleccione de que banco es la cuenta que desea inscribir: **1**
    - **Usted selecciono Unalombia que tiene una tasa de interés de 1.6 anual**

- Las cuentas que tiene asociadas son: 

    - **1. Cuenta 89**
    
    - **2. Cuenta 23**

    Entrada **2**

- Ingrese el monto en pesos a solicitar **3000**
    - **R / Usted ingresó 3000.0**
- Ingrese el plazo en meses del crédito **12**

    - **Tu solicitud de crÃ©dito ha sido aprobada y tu saldo actual es: 50003000,0**
---

---
- ### **Caso 2: (Error porque ya se tiene un crédito):**
    Si el usuario con **CC : 10**, intenta pedir otro crédito, se imprimirá.
- 
    -**El usuario 10 ya tiene un crédito activo**


---
- ## ***¿Que usuario desea realizar?***
    El segundo usuario con **C: 98** quiere solicitar un crédito

    - hernestoPerez
    - **Seleección de la funcionalidad: 3**
---

- ### **Caso 3: (La cuota tentativa del crédito supera la capacidadDeEndeudamiento):**

- Seleccione de que banco es la cuenta que desea inscribir: **3**

    - **Usted selecciono QuitaVivienda que tiene una tasa de interés de 36.0 anual**

    - **Las cuentas que tiene asociadas son:**
            
        **1. Cuenta 26**
        **2. Cuenta 69**
            
    
- Seleccione la cuenta de la que desea guardar el crédito: **1**

- Ingrese el monto en pesos a solicitar: **900.000**

- Ingrese el plazo en meses del crédito: **2**

    - **Credito rechazado por falta de capacidad de endeudamiento**

<!-- 
capacidadEndeudamiento = 6'000.000 * 0,2 ==> 1.200.000

(1+((banco.getTasaInteresAnual()/12)*plazo))*monto
(1+((36/12)*12))*100.000 = 3.700.000

cuotaTentativa = 3.700.000/12 = 308.833

 -->


---
## Funcionalidad transferir
---

---
- ## ***¿Que usuario desea realizar?***
    El primer usuario con **C: 10** transferir
    
    - juanPerez
    - **Seleección de la funcionalidad: 5**

---

- ### **Caso 1: (Pago de crédito):**
    - 
        - **Selecciona el producto de origen que quieres usar:**
            
            **1. Cuenta 89**

            **2. Cuenta 23**
    - Seleccione la cuenta de la cual quiere realizar una transferencia: **1**
        - **Usted eligio la cuenta 89**
    
    - Selecciona qué tipo de transferencia quieres hacer
        1. Pagar credito
        2. Transferencia a otra cuenta: **1**
    
    - Selecionaste: pagar credito
        Tu crédito es de 3000.0 y pagarás una cuota de 650.0.
        1. Sí
        2. Volver al menú de funcionalidades.
        
        **Sí**
        
        **- Tu pago ha sido exitoso. Tu credito restante es de 1700.0**
        **R / Tu cuenta quedó con un saldo de 9350.0**

---

---
- ## ***¿Que usuario desea realizar?***
    El segundo usuario con **C: 98** transferir
    
    - hernestoPerez
    - **Seleección de la funcionalidad: 5**

---

- ### **Caso 2: (Transferencia):**
    - 
        - **Selecciona el producto de origen que quieres usar:**
            
            **1. Cuenta 26**

            **2. Cuenta 69**
    - Seleccione la cuenta de la cual quiere realizar una transferencia: **2**
        - **Usted eligio la cuenta 69**
    
    - Selecciona que tipo de transferencia quieres hacer
        
        \1. Pagar credito
        
        \2. Transferencia a otra cuenta: 
        
        Entrada: **2**
    
    - Selecionaste: tranferir a otra cuenta.

        Selecciona a qué tipo de cuenta quieres transferir:
        
        \1. Cuentas inscritas
        
        \2. Cuentas no inscritas
        
        Entrada: **2**
    
    - Selecionaste: cuentas no inscritas.

        Seleección del banco
        
        \1. Unalombia
        
        \2. PooBanco
        
        \3. QuitaVivienda
        
        Seleccione de qué banco es la cuenta que desea inscribir: 

         - **Entrada: 1**

        - **Usted selecciono Unalombia**
        
    - Ingrese el número de cuenta de destino: **26**
        - **El número de la cuenta ingresado es: 26**
    
    - Ingrese el valor a transferir - Cuentas no inscritas: **984.000**
        - **El valor a transferir ingresado: 984000.0**

        **Envio exitoso. El saldo de su cuenta es de 1000.0.**

        **Quedaste con un saldo de: 1000.0**

---
---
- ## ***¿Que usuario desea realizar?***
    El primer usuario con **C: 10** transferir a una cuenta inscrita
    
    - juanPerez
    - **Seleección de la funcionalidad: 5**

---

- ### **Caso 3: (Transferencia a cuenta inscrita):**

- **Selecciona el producto de origen que quieres usar:**
            
    **1. Cuenta 89**

    **2. Cuenta 23**
    - Seleccione la cuenta de la cual quiere realizar una transferencia: **1**

    - Selecciona qué tipo de transferencia quieres hacer

    **1. Pagar credito**
    **2. Transferencia a otra cuenta**

    Entrada: **2**

    - Seleccione a qué tipo de cuenta quieres transferir:

    **1. Cuentas inscritas**
    **2. Cuentas no inscritas**

    Entrada: **1**

    - Seleccion cuenta destino
    **1. Cuenta 26**
    **2. Cuenta 69**

    Entrada: **1**

    - **Digite el valor que desea transferir: 9000**

    - **R / Valor ingresado: 9000.0**
    
---



## Funcionalidad ver historial

- ## ***¿Que usuario desea realizar?***
    El primer usuario con **C: 10** quiere romper topes a sus cuentas

    - juanPerez

    - Selección de funcionalidad: **4**
---
s
    - Las cuentas que teiene asociadas son: 
    **1.Cuenta 89**
    **2.Cuenta 23**
    Entrada: **89**


    



# Secuencia

## Funcionalidad inscribir cuenta.

**Seleccion usuario**
- 1

**Selección funcionalidad**
- 1
---
- 1
- 1
- 26
- 98
--

---
- Seliazar : - 6
---

**Seleccion usuario**
- 1

**Selección funcionalidad**
- 1
---
- 2
- 1
- 69
- 98
---

---
- Seliazar : - 6
---

## Funcionalidad romper topes.

**Seleccion usuario**
- 2

**Selección funcionalidad**
- 2

---
- 1
---

---
- Seliazar : - 6
---

## Funcionalidad solicitar credito.

**Seleccion usuario**
- 1

**Selección funcionalidad**
- 3
---
- 1
- 2
- 3000
- 12
---

---
- Seliazar : - 6
---

**Seleccion usuario**
- 2

**Selección funcionalidad**
- 3
---
- 1
- 900000
- 2
---

---
- Seliazar : - 6
---

## Funcionalidad transferir.

**Seleccion usuario**
- 10

**Selección funcionalidad**
- 5

---
- 1
- 1
- 1
---
---
- Seliazar : - 6
---
