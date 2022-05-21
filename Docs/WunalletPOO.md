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

- \- boolean conDeuda : Si tiene algún crédito activo.

- \- int cedula : Identificador único del usuario.

- \- ArrayList<String> bancosAsociados : Nombres de los bancos a los cuales el usuario está asociado (mediante créditos o cuentas).

### Métodos

#### Inscribir(int cc, int nroCuenta, String tipoDeCuenta, String nombreBanco)


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

- verHistorial()


    - **Idea de código:**

    - **Funcionamiento:** 

    1. El método se ejecuta sin parámetros
    2. Muestra en pantalla los bancos asociados al usuario. Esto lo hace imprimiendo todos los string de la lista bancosAsociados.
    3. La selección anterior se asignará a una variable que luego pasará como parámetro al método de clase 
    extraerBanco(String nombreBanco) de la clase Banco.
    4. Muesta en pantalla las cuentas del usuario asociadas a ese banco en un formato de <Tipo de cuenta>. Lo hace llamando al 
    método extraerCuenta(int cc) que retornará un arrayList de cuentas y a cada cuenta se le obtiene su atributo tipoDeCuenta 
    mediante un get.
    5. En base al objeto seleccionado en el paso anterior, se ejecuta el método solicitarHistorial(). Se formateará la salida
    con una iteración que extraiga y retorne la información de las tuplas en forma de String: 
    **NOTA**: En el segundo elemento de la tupla puede ir un objeto cuenta o un String con el nombre del Banco. Es necesario hacer
    un if que verifique qué tipo es y muestre su respectivo mensaje

    Ejemplos de mensaje
    
    Para transferencias
    Transferencia de <nroCuentaOrigen> a <nroCuentaDestino> por valor de <valor>.

    Para pago de créditos
    Transferencia de <nroCuentaOrigen> a <nombreBanco> por valor de <valor>.


    - **Retorno:** Void


- solicitarCredito(Banco banco, float monto, int plazo)

    - **Funcionamiento:** 
    
    Desde la interfaz el usuario escoge un banco (la lista de todos los bancos disponibles se obtiene del atributo estático
    listaBancos), una vez escogido se pasa como primer parámetro de este método.

    Luego se chequeará si el usuario tiene asociado un perfil crediticio en su atributo perfilCrediticio, o en caso contrario, se
    creará.

    Verificado el perfil, se simulará el crédito el cual retornará la cuota mensual tentativa. Si la cuota mensual supera la
    capacidad de endeudamiento el crédito se rechazará. En caso contrario, se continua revisando el comportamiento de pago, que si
    es mayor o igual a 2, permitirá finalmente crear el crédito.

    Una vez creado se le asignará al atributo de usuario 'conDeuda' un true, y se añadirá el crédito a la listaCreditos del Banco
    mediante un llamado al método añadirCredito(Credito credito) de banco.
    
--- 

## PerfilCrediticio

### Generalidades

### Atributos

- \- Usuario usuario : Usuario a quién pertenece el perfil crediticio

- \- float nivelEndeudamiento: Corresponde al 20% de los ingresos mensuales.

- \- enum[] comportamientoDePago: Entero entre 1 y 3 (representando bueno, malo y regular). Se debe definir mediante una elección
aleatoria en el constructor.

###  Métodos

- \+ Constructor(Usuario usuario)

    - **Funcionamiento:**

    Será invocado en caso de que al solicitarse un crédito el usuario no tenga perfil crediticio. Se le deberá pasar como
    parámetros solamente el usuario de donde se extraerá los ingrsos mensuales para calcular su nivel de endeudamiento, y
    el comportamiento de pago medido de 1 a 3, se fijará de forma aleatoria.

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

\+ extraerCuenta(int cc, int nroCuenta, String tipoDeCuenta){

    - **Funcionamiento:**

    Recorre iterativamente la listaDeCuentas del Banco, buscando una Cuenta cuyos atributos coincidan con los 3 parámetros. De ser así retorna el objeto, o en caso contrario, retorna Null

    - **Retorno:** Cuenta (o Null si no hay cuenta)

\+ añadirCredito(Credito credito){

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

\+ Constructor(Titular, Banco, Monto, Plazo){
    
    - **Funcionamiento:**

\+ static simularCredito(Banco banco, float monto, int plazo)

    
    - **Funcionamiento:**

    Es un método estático que se ejecutará para verificar si, al solicitar un crédito, la cuota mensual esperada no supera la capacidad de endeudamiento del usuario.

    El método tomará la tasa de interes anual del banco, y hará el siguiente cálculo

    Deuda = (1+((tasaInteresAnual/12)*plazoEnMeses))*monto

    Es decir, el monto que pide, más el interés aplicado a ese monto multiplicado por el plazo del crédito.

    Una vez calculada la deuda, se retornará el valor de cada cuota, es decir Deuda/Plazo.

---

## Abstract Cuenta

### Generalidades

### Atributos

- \- Usuario titular : Titular de la cuenta

- \- Banco banco: Banco asociado

- \- float saldo : Saldo de la cuenta

- \- int nroCuenta : El número de la cuenta

- \- String tipoDeCuenta : El tipo de la cuenta


### Métodos

- transferir()

---

## Corriente extends Cuenta

### Generalidades

### Atributos

- \- float Sobregiro : Cantidad máxima en la que puede sobregirarse la cuenta

### Métodos

\+ transferir(Banco banco, int nroCuenta, float cantidadTransferir, String tipo )

---

## Ahorros extends Cuenta

### Generalidades

### Atributos

- \- float tasaDeInteres : Tasa de interes ganada sobre el saldo de la cuenta

### Métodos

\+ transferir(Banco banco, int nroCuenta, float cantidadTransferir, String tipo )

---

## BajoMonto extends Cuenta

### Generalidades

### Atributos

- \- limiteMensual : Dinero máximo que se puede transferir por mes.

- \- acumuladorTransferencia : Contador de cuánto dinero se ha transferido de la cuenta durante el mes.

### Métodos

\+ transferir(Banco banco, int nroCuenta, float cantidadTransferir, String tipo )
---
