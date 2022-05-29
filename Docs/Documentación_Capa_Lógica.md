# Documentación de Clases

---

## Plantilla

### Generalidades

### Atributos

### Métodos


---

## Usuario

### Generalidades

### Atributos

- \- ArrayList<Cuenta> listaDeInscritos : Una lista que contendrá objetos tipo Cuenta, los cuales corresponden a las cuentas que tiene inscritas el usuario ante su entidad bancaria.

- \- float ingresosMensuales : Valor de ingresos mensuales que tiene el usuario.

- \- Credito creditoActivo : Null en caso de que el usuario no tenga un crédito asociado, o el objeto de tipo Credito que tenga 
asociado

- \- int cedula : Identificador único del usuario.

- \- ArrayList<String> bancosAsociados : Nombres de los bancos a los cuales el usuario está asociado (mediante créditos o cuentas).

- \- ArrayList<Cuenta> cuentasAsociadas : Lista de cuentas que tiene el usuario con algún banco

### Métodos

#### + Inscribir(int cc, int nroCuenta, String tipoDeCuenta, String nombreBanco)

- **Idea de código:**

    >```
    >bancoDestino = Banco.extraerBanco(nombreBanco);
    >cuentaDestio = bancoDestino.extraerCuenta;
    >this.listaInscritos.add(cuentaDestino);
    >```

- **Funcionamiento:** 

    Usará el método de la clase Banco 'extraerBanco(nombreBanco)' para primero verificar si el nombre del banco existe, y de ser así se le retornará el objeto Banco que tiene dicho nombre.

    Una vez que se tenga acceso al objeto tipo Banco, se accederá a su lista de cuentas para buscar alguna cuenta en la que los demás parámetros coincidan mediante el método de clase 'extraerCuenta(int cc, int nroCuenta, String tipoDeCuenta)'. Si hay alguna cuenta la retornará, de lo contrario retorne Null. En caso de darse el retorno, se debe añadir a la listaDeInscritos del usuario.

- **Retorno:** Void



#### + solicitarCredito(Banco banco, float monto, int plazo)

- **Funcionamiento:** 
    
    Desde la interfaz el usuario escoge un banco (la lista de todos los bancos disponibles se obtiene del atributo estático
    listaBancos), una vez escogido se pasa como primer parámetro de este método.

    Luego se chequeará si el usuario tiene asociado un perfil crediticio en su atributo perfilCrediticio, o en caso contrario, se
    creará.

    Verificado el perfil, se simulará el crédito el cual retornará la cuota mensual tentativa. Si la cuota mensual supera la
    capacidad de endeudamiento el crédito se rechazará. En caso contrario, se continua revisando el comportamiento de pago, que si
    es mayor o igual a 2, permitirá finalmente crear el crédito.

    Una vez creado se le asignará al atributo de usuario 'creditoActivo' el objeto, y se añadirá el crédito a la listaCreditos 
    del Banco mediante un llamado al método añadirCredito(Credito credito) de banco.
    

- **Retorno:** Void

#### + removerCuentaAsociada(Cuenta cuenta)



- **Funcionamiento:** 
    
    Desde la interfaz el usuario escoge un banco (la lista de todos los bancos disponibles se obtiene del atributo estático
    listaBancos), una vez escogido se pasa como primer parámetro de este método.

    Luego se chequeará si el usuario tiene asociado un perfil crediticio en su atributo perfilCrediticio, o en caso contrario, se
    creará.

    Verificado el perfil, se simulará el crédito el cual retornará la cuota mensual tentativa. Si la cuota mensual supera la
    capacidad de endeudamiento el crédito se rechazará. En caso contrario, se continua revisando el comportamiento de pago, que si
    es mayor o igual a 2, permitirá finalmente crear el crédito.

    Una vez creado se le asignará al atributo de usuario 'creditoActivo' el objeto, y se añadirá el crédito a la listaCreditos 
    del Banco mediante un llamado al método añadirCredito(Credito credito) de banco.
    

- **Retorno:** Void
--- 

## PerfilCrediticio

### Generalidades

### Atributos

- \- Usuario usuario : Usuario a quién pertenece el perfil crediticio

- \- float nivelEndeudamiento: Corresponde al 20% de los ingresos mensuales.

- \- enum[] comportamientoDePago: Entero entre 1 y 3 (representando bueno, malo y regular). Se debe definir mediante una elección
aleatoria en el constructor.

###  Métodos

#### + Constructor(Usuario usuario)

- **Funcionamiento:**

    Será invocado en caso de que al solicitarse un crédito el usuario no tenga perfil crediticio. Se le deberá pasar como
    parámetros solamente el usuario de donde se extraerá los ingrsos mensuales para calcular su nivel de endeudamiento, y
    el comportamiento de pago medido de 1 a 3, se fijará de forma aleatoria.

- **Retorno:** Void

---
## Transacción 

### Generalidades
Son objetos sin métodos cuyo fin es encapsular en sus atributos toda la información que describe cada transacción.

### Atributos

- \- Cuenta cuentaOrigen: 

- \- Cuenta cuentaDestino: 

- \- String nombreBanco: 

- \- float valorTransaccion: 


### Métodos

#### public toString()

- **Funcionamiento:**

    1. Verificar si cuentaDestino no es un Null. En este caso se retornará el String

    ```java
    return "Transferencia de " + cuentaOrigen.getTitular() + " desde la cuenta " + cuentaOrigen.getNroCuenta() + " a " + 
    " cuentaDestino.getTitular() + " a la cuenta " + cuentaDestino. getNroCuenta() + " por valor de " + \<Valor\> + "."
    
    ```

    2. Para pago de créditos.

    ```java
    return "Tranferencia "+ cuentaOrigen.getTitular() + " desde la cuenta " + cuentaOrigen.getNroCuenta() + " a " + getNombreBanco() + " por valor de " + getValorTransaccion() + "." 
    ```    

- **Retorno:** String

---
## Banco

### Generalidades

### Atributos

- \- static ArrayList<Banco> listaDeBancos: Lista con todos los objetos Banco que se han creado.

- \- String nombreBanco : El nombre del Banco

- \- ArrayList<Cuenta> listaCuentas: Lista con todos los objetos de tipo Cuenta que tiene asociadas un Banco. 

- \- ArrayList<Credito> listaCreditos: Lista con todos los objetos de tipo Credito que tiene asociadas un Banco.

- \- final float TasaInteresAnual: Interés anual que manejan los créditos del banco.

###  Métodos

#### - extraerCuenta(int cc, int nroCuenta, String tipoDeCuenta)

- **Funcionamiento:**

    Recorre iterativamente la listaDeCuentas del Banco, buscando una Cuenta cuyos atributos coincidan con los 3 parámetros. De ser así retorna el objeto, o en caso contrario, retorna Null

- **Retorno:** Cuenta (o Null si no hay cuenta)

#### - añadirCredito(Credito credito){

- **Funcionamiento:**

    Añade un crédito a la listaCreditos del banco.

- **Retorno:** Void

---

## Credito

### Generalidades

-
-
-

### Atributos

- Banco banco: Banco que tendrá asociado el crédito

- Usuario titular: Titular del crédito

- float Deuda: Cálculo resultante de considerar el interes del banco, el plazo, y el monto.

- float cuotaMensual: Deuda dividido plazo.


### Métodos

#### + Constructor(Titular, Banco, Monto, Plazo){
    
- **Funcionamiento:**

- **Retorno:** Void

#### + static simularCredito(Banco banco, float monto, int plazo)

    
- **Funcionamiento:**

    Es un método estático que se ejecutará para verificar si, al solicitar un crédito, la cuota mensual esperada no supera la capacidad de endeudamiento del usuario.

    El método tomará la tasa de interes anual del banco, y hará el siguiente cálculo

    Deuda = (1+((tasaInteresAnual/12)*plazoEnMeses))*monto

    Es decir, el monto que pide, más el interés aplicado a ese monto multiplicado por el plazo del crédito.

    Una vez calculada la deuda, se retornará el valor de cada cuota, es decir Deuda/Plazo.

- **Retorno:** Void

---

## Abstract Cuenta

### Generalidades

### Atributos

- \- Usuario titular : Titular de la cuenta

- \- Banco banco: Banco asociado

- \- float saldo : Saldo de la cuenta

- \- int nroCuenta : El número de la cuenta

- \- String tipoDeCuenta : El tipo de la cuenta

- \- ArrayList[Transaccion] historialTransferencia : Historial de todas las transacciones realizadas con la cuenta

### Métodos

#### + verHistorial()

- **Funcionamiento:** 
    
    *Nota: El método se ejecuta sin parámetros*

    1. Al ser ejecutado desde la cuenta origen, se iterará sobre la lista historialTransferencia e imprimiendo cada uno de los
    objetos que ya estarán formateados por el método toString()


- **Retorno:** Void

#### abstract - transferir(Cuenta cuentaDestino, float valorTransferencia);

- **Funcionamiento:**

Ejecutará las comprobaciones y actualizaciones de saldo correspondientes al realizar una transferencia. Este proceso depende del
tipo de cuenta que lo ejecute, y por eso debe ser un método abstracto.

Este método se ejecuta como cuentaOrigen.transferir(cuentaDestino, valorTransferencia)
    
- **Retorno:** Boolean

#### abstract - transferir(Credito credito);

- **Funcionamiento:**

Ejecutará las comprobaciones y actualizaciones de saldo correspondientes al realizar el pago de un crédito. Este proceso depende del
tipo de cuenta que lo ejecute, y por eso debe ser un método abstracto.

Este método se ejecuta como cuentaOrigen.transferir(cuentaDestino, valorTransferencia)

- **Retorno:** Boolean
---

## Corriente extends Cuenta

### Generalidades

### Atributos

- \- static final float capacidadSobregiro : Cantidad máxima en la que puede sobregirarse la cuenta
- \- float sobregiroActual : Cantidad actual que ha sido sobregirada

### Métodos

#### + transferir(Cuenta cuentaDestino, float valorTransferencia);

- **Funcionamiento:**

1. Verificar si valorTransferencia <= saldoCuentaOrigen + sobregiroActual

2. En caso de haber usado la capacidad de sobregiro, se setea el atributo sobregiroActual con la cantidad valorTransferencia-saldo
Esto se debe comprobar con un if, si valorTransferencia-saldo>0.

3. Realiza los ajustos de saldo a ambas cuentas mediante 

    ```java
    this.restarSaldo(_)
    cuentaDestino.sumarSaldo(_)
    ```

4. Crea el objeto de tipo Transaccion llamando al constructor Transaccion(Cuenta cuentaOrigen, Cuenta cuentaDestino,
float valorTransaccion) 

5. Agrega el objeto creado en el paso anterior a la lista historialTransferencia de la cuentaOrigen

- **Retorno:** Boolean

#### + transferir(Credito credito);

- **Funcionamiento:**

1. Verificar si cuotaMensual <= saldoCuentaOrigen + sobregiroActual

2. En caso de haber usado la capacidad de sobregiro, se setea el atributo sobregiroActual con la cantidad valorTransferencia-saldo
Esto se debe comprobar con un if, si valorTransferencia-saldo>0.

3. Realiza los ajustos de saldo a la cuentaOrigen y al Credito

    ```java
    this.restarSaldo(cuotaMensual)
    credito.setDeuda(credito.getDeuda()-credito.getCuotaMensual())
    ```

4. Crea el objeto de tipo Transaccion llamando al constructor Transaccion(Cuenta cuentaOrigen, String nombreBanco,
float valorTransaccion) 

5. Agrega el objeto creado en el paso anterior a la lista historialTransferencia de la cuentaOrigen

- **Retorno:** Boolean

---

## Ahorros extends Cuenta

### Generalidades

### Atributos

- \# float tasaDeInteres : Tasa de interes ganada sobre el saldo de la cuenta

### Métodos

#### + transferir(Cuenta cuentaDestino, float valorTransferencia);

- **Funcionamiento:**

1. Verificar si valorTransferencia <= saldoCuentaOrigen

3. Realiza los ajustos de saldo a ambas cuentas mediante 

    ```java
    this.restarSaldo(_)
    cuentaDestino.sumarSaldo(_)
    ```

4. Crea el objeto de tipo Transaccion llamando al constructor Transaccion(Cuenta cuentaOrigen, Cuenta cuentaDestino,
float valorTransaccion) 

5. Agrega el objeto creado en el paso anterior a la lista historialTransferencia de la cuentaOrigen

- **Retorno:** Boolean


#### + transferir(Credito credito);

- **Funcionamiento:**

1. Verificar si cuotaMensual <= saldoCuentaOrigen

3. Realiza los ajustos de saldo a la cuentaOrigen y al Credito

    ```java
    this.restarSaldo(cuotaMensual)
    credito.setDeuda(credito.getDeuda()-credito.getCuotaMensual())
    ```

4. Crea el objeto de tipo Transaccion llamando al constructor Transaccion(Cuenta cuentaOrigen, String nombreBanco,
float valorTransaccion) 

5. Agrega el objeto creado en el paso anterior a la lista historialTransferencia de la cuentaOrigen

- **Retorno:** Boolean

---

## BajoMonto extends Cuenta

### Generalidades

### Atributos

- \- limiteMensual : Dinero máximo que se puede transferir por mes.

- \- acumuladorTransferencia : Contador de cuánto dinero se ha transferido de la cuenta durante el mes.

### Métodos

#### + transferir(Cuenta cuentaDestino, float valorTransferencia);

- **Funcionamiento:**

1. Verificar si valorTransferencia <= saldoCuentaOrigen

2. Verificar si valorTransferencia + acumuladorTransferencia <= limiteMensual

3. Realiza los ajustos de saldo a ambas cuentas mediante 

    ```java
    this.restarSaldo(_)
    cuentaDestino.sumarSaldo(_)
    ```

4. Crea el objeto de tipo Transaccion llamando al constructor Transaccion(Cuenta cuentaOrigen, Cuenta cuentaDestino,
float valorTransaccion) 

5. Agrega el objeto creado en el paso anterior a la lista historialTransferencia de la cuentaOrigen

- **Retorno:** Boolean

#### + transferir(Credito credito);

- **Funcionamiento:**

1. Verificar si cuotaMensual <= saldoCuentaOrigen

2. Verificar si cuotaMensual + acumuladorTransferencia <= limiteMensual

3. Realiza los ajustos de saldo a la cuentaOrigen y al Credito

    ```java
    this.restarSaldo(cuotaMensual)
    credito.setDeuda(credito.getDeuda()-credito.getCuotaMensual())
    ```

4. Crea el objeto de tipo Transaccion llamando al constructor Transaccion(Cuenta cuentaOrigen, String nombreBanco,
float valorTransaccion) 

5. Agrega el objeto creado en el paso anterior a la lista historialTransferencia de la cuentaOrigen

- **Retorno:** Boolean

#### + romperTopes();

- **Funcionamiento:**

1. Se debe verificar que el saldo de la cuenta sea mayor o igual a 15.000 pesos, que es el costo de rompe
2. Se creará un nuevo objeto de tipo Ahorro asignado a la variable nuevaCuentaAhorro
    ```java
    Ahorro nuevaCuentaAhorro = new Ahorro(this.getTitular(), this.getBanco(), this.getSaldo(), this.getNroCuenta(), "Ahorro",
    this.getHistorialTransferencia(), this.getTasaInteres())
    ```

- **Retorno:** Boolean

---

## interface Gestor 

### Generalidades

- La interfaz Gestor almacena todas las operaciones que modifican el estado de una cuenta. Será implementada por la clase abstracta
Cuenta

### Atributos

- static final float SOBREGIROMAXIMOCIERRE = 0 : Representa que para cerrar una cuenta se puede tener un sobregiro máximo de 0 pesos
(no se puede deber al banco).

- static final float SALDOMAXIMOCIERRE = 0 : Para cerrar una cuenta es necesario que no tenga saldo.

### Métodos

#### default + eliminarCuenta()

- **Funcionamiento:**

cuenta.eliminarCuenta()
1. Toma el objeto tipo Usuario que hay en el atributo titular de la cuenta, para remover la cuenta que invoca el método de la lista de cuentasAsociadas que tiene el usuario

```java
// ver https://www.geeksforgeeks.org/remove-element-arraylist-java/

import java.util.ArrayList;
import java.util.List;

usuario = this.getTitular()
usuario.cuentasAsociadas.remove(this)

```

- **Retorno:** Boolean

#### default + sumarSaldo(float Valor);

- **Funcionamiento:**
    ```java
    this.setSaldo(this.getSaldo() + valor)
    ```

- **Retorno:** Void

#### default + restarSaldo(float Valor);

- **Funcionamiento:**
    ```java
    this.setSaldo(this.getSaldo() - valor)
    ```

- **Retorno:**  Void
