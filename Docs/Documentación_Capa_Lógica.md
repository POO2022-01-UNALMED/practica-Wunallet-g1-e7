# Documentación de Clases

## Usuario

### Generalidades

- Toda funcionalidad será ejecutada sobre un usuario, o usando los atributos de este. 
- Es la primera selección que se debe realizar en la interfaz.
- Cuenta como una de las tres clases con las que se debe interactuar en todas las funcionalidades.

### Atributos

- \- ArrayList<Cuenta> listaInscritos : Una lista que contendrá objetos tipo Cuenta, los cuales corresponden a las cuentas que tiene inscritas el usuario ante su entidad bancaria.

- \- float ingresosMensuales : Valor de ingresos mensuales que tiene el usuario.

- \- PerfilCrediticio perfilCrediticio : Perfil crediticio con el que cuenta el usuario.

- \- int cc : Número de identificación del usuario.

- \- Credito creditoActivo : Null en caso de que el usuario no tenga un crédito asociado, o el objeto de tipo Credito que tenga 
asociado.

- \- ArrayList<String> bancosAsociados : Nombres de los bancos a los cuales el usuario está asociado (mediante créditos o cuentas).

- \- ArrayList<Cuenta> cuentasAsociadas : Lista de cuentas que tiene el usuario con algún banco.


### Métodos

#### public Inscribir(int nroCuenta, String nombreBanco)

- **Funcionamiento:** 

    Usará el método de clase Banco 'extraerBanco(nombreBanco)' que retornará el objeto Banco con dicho nombre.

    Una vez que se tenga acceso al objeto tipo Banco, se accederá a su lista de cuentas para buscar alguna cuenta en la que el
    número de cuenta coincida mediante el método de instancia 'extraerCuenta(int nroCuenta)'.
    
    Finalmente se agrega la cuenta a la listaInscritos del usuario.

- **Retorno:** Void


#### public solicitarCredito(Banco banco, float monto, int plazo, Cuenta cuentaSeleccionada)

- **Funcionamiento:** 
    
    Se verificará si el usuario cuenta con un perfil crediticio. De no ser así, se le creará uno y se le asignará a su atributo
    perfilCrediticio.

    Luego se revisarán los atributos del perfilCrediticio y, en caso de que el comportamientoDePago del usuario sea suficientemente
    bueno, se simulará el crédito para retornar la cuota mensual tentativa. Si esta cuota supera la capacidad de endeudamiento del
    usuario el crédito se rechazará. En caso contrario, el crédito será creado y asignado al atributo creditoActivo del usuario.

    Finalmente se sumará el saldo del crédito otorgado al usuario en la cuenta seleeccionada, y se añadirá a la listaCreditos
    del banco mediante un llamado al método añadirCredito(Credito credito) del banco.

    Su retorno será un entero, en base al cual se harán los llamados correspondientes a las pantallas de la interfaz gráfica.
    
- **Retorno:** int


#### public removerCuentaAsociada(Cuenta cuenta)

- **Funcionamiento:** 
    
    Remueve de la lista cuentasAsociadas la cuenta dada en el parámetro.
    
- **Retorno:** Void


#### public removerCuentaInscrita(Cuenta cuenta)

- **Funcionamiento:** 
    
    Remueve de la lista listaInscritos la cuenta dada en el parámetro.
    
- **Retorno:** Void

#### public toString()

- **Funcionamiento:** 

    ```java
	public String toString() {
		StringBuffer texto = new StringBuffer(110);
		texto.append("Las cuentas inscritas del usuario "+ this.getCc() +" son: ");
		for(Cuenta i : this.getListaIncritos()) {
			texto.append(i.getNroCuenta() + " ");
		}
		return texto.toString();
	}
    ```
    
- **Retorno:** String
--- 

## PerfilCreditico

### Generalidades

Clase que contiene la información necesaria para permitir o rechazar una solicitud de crédito. Están asociados a un usuario.

### Atributos

- \- Usuario usuario : Usuario a quién pertenece el perfil crediticio

- \- float capacidadEndeudamiento: Corresponde al 20% de los ingresos mensuales.

- \- comportamientoDePago comportamientoDePago: Entero entre 1 y 3 (representando bueno, malo y regular). Se debe definir mediante
una elección aleatoria en el constructor.

###  Métodos

#### public Constructor(Usuario usuario, float ingresosMensuales, comportamientoDePago nivel)

- **Funcionamiento:**

    Será invocado en caso de que al solicitarse un crédito el usuario no tenga perfil crediticio. 
    
    Asignará a su atributo usuario el usuario enviado como parámetro. También asignará en la capacidadEndeudamiento el 20% de los
    ingresos mensuales del usuario, y finalmente asignará de forma aleatoria el nivel (extraido del enum comportamientoDePago), a su
    comportamientoDePago.

- **Retorno:** Void

---
## Transacción 

### Generalidades

Son objetos sin métodos cuyo fin es encapsular en sus atributos toda la información que describe cada transacción.

### Atributos

- \- Cuenta cuentaOrigen: Cuenta desde la que se realiza la transacción.

- \- Cuenta cuentaDestino: Cuenta a la que se le realiza la transacción.

- \- String nombreBanco: Nombre del banco al que se le realiza el pago del crédito.

- \- float valorTransaccion: Valor de la transacción.


### Métodos

#### public toString()

- **Funcionamiento:**

    1. Verificar si cuentaDestino no es un Null. En este caso se retornará el String

    ```java
    return "Transferencia de " + cuentaOrigen.getTitular() + " desde la cuenta " + cuentaOrigen.getNroCuenta() + " a " + 
    " cuentaDestino.getTitular() + " a la cuenta " + cuentaDestino.getNroCuenta() + " por valor de " + \<Valor\> + "."
    
    ```

    2. Para pago de créditos.

    ```java
    return "Transferencia de "+ cuentaOrigen.getTitular() + " desde la cuenta " + cuentaOrigen.getNroCuenta() + " a " + getNombreBanco() + " por valor de " + getValorTransaccion() + "." 
    ```    

- **Retorno:** String

---
## Banco

### Generalidades

### Atributos

- \- String nombreBanco : El nombre del banco

- \- final float TasaInteresAnual: Interés anual que manejan los créditos del banco.

- \+ static ArrayList<Banco> listaBancos: Lista con todos los objetos Banco que se han creado.

- \- ArrayList<Cuenta> listaCuentas: Lista con todos los objetos de tipo Cuenta que tiene asociadas un Banco. 

- \- ArrayList<Credito> listaCreditos: Lista con todos los objetos de tipo Credito que tiene asociadas un Banco.


###  Métodos

#### public static extraerBanco(String nombreBanco) 

- **Funcionamiento:**

    Recorre iterativamente la listaBancos de la clase Banco, buscando un banco cuyo nombre coincida con el parámetro ingresado. De
    existir retornará el objeto.

- **Retorno:** Banco

#### public extraerCuenta(int nroCuenta)

- **Funcionamiento:**

    Recorre iterativamente la listaDeCuentas del banco desde donde se invoca el método, buscando una cuenta que tenga el numero
    de cuenta ingresado. 

- **Retorno:** Cuenta


#### public añadirCredito(Credito credito)

- **Funcionamiento:**

    Añade un crédito a la listaCreditos del banco.

- **Retorno:** Void

#### public removerCuenta(Cuenta cuenta)

- **Funcionamiento:**

    Remueve la cuenta del parámetro de la listaCuentas del banco.

- **Retorno:** Void

---

## Credito

### Generalidades

Los objetos de esta clase representan los créditos que otorga un banco a un usuario tras una solicitud exitosa.

### Atributos

- \- Usuario titular: Titular del crédito.

- \- Banco banco: Banco que tendrá asociado el crédito.

- \- float deuda: Cálculo resultante de considerar el interes del banco, el plazo, y el monto.

- \- float cuotaMensual: Es el valor que resulta de dividir la deuda inicial entre el plazo.


### Métodos

#### public static simularCredito(Banco banco, float monto, int plazo)
    
- **Funcionamiento:**

    Es un método estático que se ejecutará para verificar si, al solicitar un crédito, la cuota mensual esperada no supera la
    capacidad de endeudamiento del usuario.

    El método tomará la tasa de interes anual del banco, y hará el siguiente cálculo

    Deuda = (1+((tasaInteresAnual/12)*plazoEnMeses))*monto

    Es decir, el monto que pide, más el interés aplicado a ese monto multiplicado por el plazo del crédito.

    Una vez calculada la deuda, se retornará el valor de cada cuota, es decir Deuda/Plazo.

- **Retorno:** float

---

## Abstract Cuenta

### Generalidades

### Atributos

- \# Usuario titular : Titular de la cuenta

- \# Banco banco: Banco asociado

- \# float saldo : Saldo de la cuenta

- \# int nroCuenta : El número de la cuenta

- \# String tipoDeCuenta : El tipo de la cuenta

- \# ArrayList[Transaccion] historialTransferencia : Historial de todas las transacciones realizadas con la cuenta

### Métodos

#### public verHistorial()

- **Funcionamiento:** 

    Al ser ejecutado desde la cuenta origen, iterará sobre la lista historialTransferencia e imprimirá cada uno de los
    objetos ya formateados por el método toString()


- **Retorno:** Void

#### public abstract transferir(Cuenta cuentaDestino, float valorTransferencia)

- **Funcionamiento:**

Ejecutará las comprobaciones y actualizaciones de saldo correspondientes al realizar una transferencia. Este proceso depende del
tipo de cuenta que lo ejecute, y por eso debe ser un método abstracto.
    
- **Retorno:** Boolean

#### public abstract transferir(Credito credito)

- **Funcionamiento:**

Ejecutará las comprobaciones y actualizaciones de saldo correspondientes al realizar el pago de un crédito. Este proceso depende del
tipo de cuenta que lo ejecute, y por eso debe ser un método abstracto.

- **Retorno:** Boolean

#### public sumarSaldo(float valor)

- **Funcionamiento:**

Es un método implementado por requerimiento de la interfaz gestor. Sumará el saldo del parámetro a la cuenta desde la que se invoca el método.

- **Retorno:** Void

#### public restarSaldo(float valor)

- **Funcionamiento:**

Restará el saldo del parámetro a la cuenta desde la que se invoca el método.

- **Reetorno:** Void

---

## Corriente extends Cuenta

### Generalidades

### Atributos

- \- static final float capacidadSobregiro : Cantidad máxima en la que puede sobregirarse la cuenta
- \- float sobregiroActual : Cantidad actual que ha sido sobregirada

### Métodos

#### public transferir(Cuenta cuentaDestino, float valorTransferencia);

- **Funcionamiento:**

1. Verificar si valorTransferencia <= saldoCuentaOrigen + (capacidadSobregiro - sobregiroActual)

2. En caso de haber usado la capacidad de sobregiro, se setea el atributo sobregiroActual con la cantidad valorTransferencia-saldo
Esto se debe comprobar con un if, si valorTransferencia-saldo>0.

3. Realiza los ajustos de saldo a ambas cuentas mediante 

    ```java
    this.restarSaldo(_)
    cuentaDestino.sumarSaldo(_)
    ```

4. Crea el objeto de tipo Transaccion llamando al constructor Transaccion(Cuenta cuentaOrigen, Cuenta cuentaDestino,
float valorTransaccion).

5. Agrega el objeto creado en el paso anterior a la lista historialTransferencia de la cuentaOrigen y cuentaDestino.

- **Retorno:** Boolean

#### + transferir(Credito credito);

- **Funcionamiento:**

1. Verificar si cuotaMensual <= saldoCuentaOrigen + (capacidadSobregiro - sobregiroActual)

2. En caso de haber usado la capacidad de sobregiro, se setea el atributo sobregiroActual con la cantidad cuotaMensual-saldo
Esto se debe comprobar con un if, si cuotaMensual-saldo>0.

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

5. Agrega el objeto creado en el paso anterior a la lista historialTransferencia de la cuentaOrigen y cuentaDestino.

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

## BajoMonto extends Ahorro

### Generalidades

### Atributos

- \- float limiteMensual : Dinero máximo que se puede transferir por mes.

- \- float acumuladorTransferencia : Contador de cuánto dinero se ha transferido de la cuenta durante el mes.

### Métodos

#### + transferir(Cuenta cuentaDestino, float valorTransferencia);

- **Funcionamiento:**

1. Verificar si (valorTransferencia <= saldoCuentaOrigen) && (valorTransferencia + acumuladorTransferencia <= limiteMensual)

2. Realiza los ajustos de saldo a ambas cuentas mediante 

    ```java
    this.restarSaldo(_)
    cuentaDestino.sumarSaldo(_)
    ```

4. Crea el objeto de tipo Transaccion llamando al constructor Transaccion(Cuenta cuentaOrigen, Cuenta cuentaDestino,
float valorTransaccion) 

5. Agrega el objeto creado en el paso anterior a la lista historialTransferencia de la cuentaOrigen y cuentaDestino.

- **Retorno:** Boolean

#### + transferir(Credito credito);

- **Funcionamiento:**

1. Verificar si (cuotaMensual <= saldoCuentaOrigen) && (cuotaMensual + acumuladorTransferencia <= limiteMensual)

2. Realiza los ajustos de saldo a la cuentaOrigen y al Credito

    ```java
    this.restarSaldo(cuotaMensual)
    credito.setDeuda(credito.getDeuda()-credito.getCuotaMensual())
    ```

3. Crea el objeto de tipo Transaccion llamando al constructor Transaccion(Cuenta cuentaOrigen, String nombreBanco,
float valorTransaccion) 

4. Agrega el objeto creado en el paso anterior a la lista historialTransferencia de la cuentaOrigen

- **Retorno:** Boolean

#### + romperTopes();

- **Funcionamiento:**

1. Se debe verificar que el saldo de la cuenta sea mayor a 15.000 pesos, que es el costo de romper los topes.

2. Se creará un nuevo objeto de tipo Ahorro asignado a la variable nuevaCuentaAhorro

    ```java
    Ahorro nuevaCuentaAhorro = new Ahorro(this.getTitular(), this.getBanco(), this.getSaldo(), this.getNroCuenta(), "Ahorro",
    this.getTasaInteres())
    ```

3. Setear el historial de la nueva cuenta con el historial de la cuenta BajoMonto.

- **Retorno:** Boolean

---

## interface Gestor 

### Generalidades

- La interfaz Gestor almacena todas las operaciones que modifican el estado de una cuenta. Será implementada por la clase abstracta
Cuenta

### Atributos

- static final float COSTOROMPERTOPES = 15.000 : Es el costo fijado para actualizar una cuenta de BajoMonto a una de Ahorro

### Métodos

#### public abstract sumarSaldo(float Valor);

- **Funcionamiento:**
    
    Metodo para sumar saldo del producto bancario en que se implementa.

- **Retorno:** Void

#### public abstract restarSaldo(float Valor);

- **Funcionamiento:**

    Metodo para restar saldo del producto bancario en que se implementa.

- **Retorno:**  Void

---

## Enum ComportamientoDePago

### Generalidades

### Atributos

- \- int nivel

### Enum

- BUENO(1)
- REGULAR(2)
- MALO(3)

### Métodos

#### public static randomNivel();

- **Funcionamiento:**

    Método para seleccionar aleatoriamente un nivel del enum.

- **Retorno:**  ComportamientoDePago

---
