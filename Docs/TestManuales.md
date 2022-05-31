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