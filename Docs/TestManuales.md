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
    - juanPerez

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

    - Seleccione el tipo de cuenta: **3**

        - **Usted seleccionó corriente**
    
    - Seleccione el número de cuenta: **23**

    - Seleccione el número de cedula: **10**

        - **Las cuentas inscritas del usuario 10 son: 23**

---

- ### **Caso 3: (El número de cuenta exite en el banco):** 

    - Seleccione de que banco es la cuenta que desea inscribir: **2**

        - **Usted seleccionó PooBanco**

    - Seleccione el tipo de cuenta: **1**

        - **Usted seleccionó bajomonto**

    - Seleccione el número de cuenta: **69**

    - Seleccione el número de cedula: **98**

        - **Las cuentas inscritas del usuario 10 son: 23 69**


---
- ### **¿Que usuario desea usar?**
    - hernestoPerez

    **No tendrá cuentas inscritas**
---

---
## Funcionalidad romperTopes
---


- ## ***¿Que usuario desea realizar?***
    - juanPerez
---
---
- ### **Caso 1: (No tiene cuentas de bajo monto):**
    - Esta funcionalidad no está habilitada para tus cuentas.
---
---
- ## ***¿Que usuario desea realizar?***
    - hernestoPerez
---

- ### **Caso 1: (No tiene cuentas de bajo monto):**
    -  
        - **¡Recuerde! El procedimiento de romper topes consiste en transformar su cuenta de tipo Bajo monto, a una cuenta de ahorros convencional, eliminando las limitaciones de este tipo de cuentas. Este proceso tiene un costo de 15.000 pesos que pagará una única vez.**
    - Para continuar seleccione la cuenta de bajo monto que desea transformar: **1**

        - **Tu solicitud ha sido aprobada, se descontarÃ¡ 15.000 de tu saldo para realizar el proceso. Espera un momento...**

        - **Tu cuenta ha sido actualizada y ahora no tiene topes.** 

        - **Tu nueva cuenta de ahorros ahora tiene un saldo de: \<SaldoCuentaAhorros\>.**
    
---
## Funcionalidad solicitarCredito
---

---
- ## ***¿Que usuario desea realizar?***
    - juanPerez
---


- ### **Caso 1: (Aprovación del crédito):** 
**NOTA:** Todos los usuarios inician sin ningún crédito.

- Seleccione de que banco es la cuenta que desea inscribir: **2**
    - 

- Seleccione de que banco es la cuenta que desea inscribir: **1**
    - **Usted selecciono Unalombia que tiene una tasa de interés de 1.6 anual**
- Las cuentas que tiene asociadas son: 

    - **1. Cuenta 89**
    
    - **2. Cuenta 23**

- Ingrese el monto en pesos a solicitar **3000**

- Ingrese el plazo en meses del crédito **12**

    - **Tu solicitud de crÃ©dito ha sido aprobada y tu saldo actual es: 13000,0**
---

---
- ### **Caso 2: (Error porque ya se tiene un crédito):**

- 
    -**El usuario 10 ya tiene un crédito activo**


---
- ## ***¿Que usuario desea realizar?***
    - hernestoPerez
---

- ### **Caso 3: (La cuota tentativa del crédito supera la capacidadDeEndeudamiento):**

- Seleccione de que banco es la cuenta que desea inscribir: **3**

    - **Usted selecciono QuitaVivienda que tiene una tasa de interés de 36.0 anual**

    - **Las cuentas que tiene asociadas son:**
            
        **1. Cuenta 69**
            
        **2. Cuenta 26**
    
- Seleccione la cuenta de la que desea guardar el crédito: **1**

- Ingrese el monto en pesos a solicitar: **100.000**

- Ingrese el plazo en meses del crédito: **12**

    - **Credito rechazado por falta de capacidad de endeudamiento**

<!-- 
capacidadEndeudamiento = 1'000.000 * 0,2 ==> 200.000
(1+((banco.getTasaInteresAnual()/12)*plazo))*monto
(1+((36/12)*12))*100.000 = 3.700.000

cuotaTentativa = 3.700.000/12 = 308.833

 -->


---
## Funcionalidad transferir
---

---
- ## ***¿Que usuario desea realizar?***
    - juanPerez
---

- ### **Caso 1: (Pago de crédito):**
    - 
        - **Selecciona el producto de origen que quieres usar:**
            
            **1. Cuenta 89**

            **2. Cuenta 23**
    - Seleccione la cuenta de la cual quiere realizar una transferencia: **1**
        - **Usted eligio la cuenta 89**
    
    - Selecciona quÃ© tipo de transferencia quieres hacer
        1. Pagar credito
        2. Transferencia a otra cuenta: **1**
    
    - Selecionaste: pagar credito
        Tu crédito es de 3000.0 y pagarás una cuota de 875.0.
        1. Sí
        2. Volver al menú de funcionalidades.
        
        **Sí**
        
        **- Tu pago ha sido exitoso. Tu credito restante es de 1250.0**

---

- ### **Caso 2: (Transferencia):**
    - 
        - **Selecciona el producto de origen que quieres usar:**
            
            **1. Cuenta 89**

            **2. Cuenta 23**
    - Seleccione la cuenta de la cual quiere realizar una transferencia: **1**
        - **Usted eligio la cuenta 89**
    
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

         - **Entrada: 3**

        - **Usted selecciono QuitaVivienda**
        
    - Ingrese el número de cuenta de destino:
---


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
    **1**
    - juanPerez

---

- ### **Caso 1: (El número de cuenta NO exite en el banco):**
    - **1**
    - Seleccione de que banco es la cuenta que desea inscribir: **1**

        - **Usted seleccionó Unalombia**

    - Seleccione el tipo de cuenta: **1**

        - **Usted seleccionó bajomonto**

    - Seleccione el número de cuenta: **69**

        - **Numero de cuenta 1 no existe en el banco: Unalombia**

---

- ### **Caso 2: (El número de cuenta exite en el banco):** 
    - **1**
    - Seleccione de que banco es la cuenta que desea inscribir: **1**

        - **Usted seleccionó Unalombia**

    - Seleccione el tipo de cuenta: **3**

        - **Usted seleccionó corriente**
    
    - Seleccione el número de cuenta: **23**

    - Seleccione el número de cedula: **10**

        - **Las cuentas inscritas del usuario 10 son: 23**

---

- ### **Caso 3: (El número de cuenta exite en el banco):** 
    **1**
    - Seleccione de que banco es la cuenta que desea inscribir: **2**

        - **Usted seleccionó PooBanco**

    - Seleccione el tipo de cuenta: **1**

        - **Usted seleccionó bajomonto**

    - Seleccione el número de cuenta: **69**

    - Seleccione el número de cedula: **98**

        - **Las cuentas inscritas del usuario 10 son: 23 69**


---
- ### **¿Que usuario desea usar?**
    - hernestoPerez

    **No tendrá cuentas inscritas**
---

---
## Funcionalidad romperTopes
---


- ## ***¿Que usuario desea realizar?***
    - juanPerez
---
---
- ### **Caso 1: (No tiene cuentas de bajo monto):**
    - Esta funcionalidad no está habilitada para tus cuentas.
---
---
- ## ***¿Que usuario desea realizar?***
    - hernestoPerez
---

- ### **Caso 1: (No tiene cuentas de bajo monto):**
    -  
        - **¡Recuerde! El procedimiento de romper topes consiste en transformar su cuenta de tipo Bajo monto, a una cuenta de ahorros convencional, eliminando las limitaciones de este tipo de cuentas. Este proceso tiene un costo de 15.000 pesos que pagará una única vez.**
    - Para continuar seleccione la cuenta de bajo monto que desea transformar: **1**

        - **Tu solicitud ha sido aprobada, se descontarÃ¡ 15.000 de tu saldo para realizar el proceso. Espera un momento...**

        - **Tu cuenta ha sido actualizada y ahora no tiene topes.** 

        - **Tu nueva cuenta de ahorros ahora tiene un saldo de: \<SaldoCuentaAhorros\>.**
    
---
## Funcionalidad solicitarCredito
---

---
- ## ***¿Que usuario desea realizar?***
    - juanPerez
---


- ### **Caso 1: (Aprovación del crédito):** 
**NOTA:** Todos los usuarios inician sin ningún crédito.

- Seleccione de que banco es la cuenta que desea inscribir: **2**
    - 

- Seleccione de que banco es la cuenta que desea inscribir: **1**
    - **Usted selecciono Unalombia que tiene una tasa de interés de 1.6 anual**
- Las cuentas que tiene asociadas son: 

    - **1. Cuenta 89**
    
    - **2. Cuenta 23**

- Ingrese el monto en pesos a solicitar **3000**

- Ingrese el plazo en meses del crédito **12**

    - **Tu solicitud de crÃ©dito ha sido aprobada y tu saldo actual es: 13000,0**
---

---
- ### **Caso 2: (Error porque ya se tiene un crédito):**

- 
    -**El usuario 10 ya tiene un crédito activo**


---
- ## ***¿Que usuario desea realizar?***
    - hernestoPerez
---

- ### **Caso 3: (La cuota tentativa del crédito supera la capacidadDeEndeudamiento):**

- Seleccione de que banco es la cuenta que desea inscribir: **3**

    - **Usted selecciono QuitaVivienda que tiene una tasa de interés de 36.0 anual**

    - **Las cuentas que tiene asociadas son:**
            
        **1. Cuenta 69**
            
        **2. Cuenta 26**
    
- Seleccione la cuenta de la que desea guardar el crédito: **1**

- Ingrese el monto en pesos a solicitar: **100.000**

- Ingrese el plazo en meses del crédito: **12**

    - **Credito rechazado por falta de capacidad de endeudamiento**

<!-- 
capacidadEndeudamiento = 1'000.000 * 0,2 ==> 200.000
(1+((banco.getTasaInteresAnual()/12)*plazo))*monto
(1+((36/12)*12))*100.000 = 3.700.000

cuotaTentativa = 3.700.000/12 = 308.833

 -->


---
## Funcionalidad transferir
---

---
- ## ***¿Que usuario desea realizar?***
    - juanPerez
---

- ### **Caso 1: (Transferencia: Pago crédito):**
    - 
        - **Selecciona el producto de origen que quieres usar:**
            
            **1. Cuenta 89**

            **2. Cuenta 23**
    - Seleccione la cuenta de la cual quiere realizar una transferencia: **1**
        - **Usted eligio la cuenta 89**
    
    - Selecciona quÃ© tipo de transferencia quieres hacer
        1. Pagar credito
        2. Transferencia a otra cuenta

        : **1**
    
    - Selecionaste: pagar credito
        Tu crÃ©dito es de 3000.0 y pagarÃ¡s una cuota de 875.0.
        1. Sí
        2. Volver al menú de funcionalidades.
        
        **Sí**
        
        **- Tu pago ha sido exitoso. Tu credito restante es de 1250.0**

---
---
- ## ***¿Que usuario desea realizar?***
    - hernestoPerez
---

- ### **Caso 2: (Transferencia a otra cuenta):**

    - 


---




## Secuencia rápida

Secuencia:


------------------------------------------ inscribir cuentas --------------------------------------

**1** - Selección de usuario

1

1

1

69

------NoExiste----

1

1

3

23

10

---
1

2

1

69

98

-------------------------------------------- Romper Topes ---------------------------------

2-------------------- Caso error ------------------------------

**7**---------------- Cambiar de usuario -----------------------

**2** - Selección de usuario

2

1

2

1

--------------------------------------------- Solicitar credito -------------------------------------

**7**---------------- Cambiar de usuario -----------------------

**1** - Selección de usuario

3

2

1

3000

12

3 -------------------- Caso error ------------------------------

**7**---------------- Cambiar de usuario -----------------------

**2** - Selección de usuario

3

3

1

100000

12 -------------------- Caso error ------------------------------


------------------------------------------------- Transferir -----------------------------------------

**7**---------------- Cambiar de usuario -----------------------

**1** - Selección de usuario

5

1

1

1

**7**---------------- Cambiar de usuario -----------------------

**2** - Selección de usuario

5

1

1 ------No tienes ningÃºn crÃ©dito activo para pagar.--
