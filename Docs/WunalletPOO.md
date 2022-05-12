# Documentación de Clases

---

## Usuario

### Generalidades

### Atributos

- \+ ArrayList<Cuenta> listaDeInscritos : Una lista que contendrá objetos tipo Cuenta, los cuales corresponden a las cuentas que tiene inscritas el usuario ante su entidad bancaria.

### Métodos
- Inscribir(int cc, int nroCuenta, String tipoDeCuenta, String nombreBanco)


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

--- 

## Banco

### Generalidades

### Atributos

- \- static ArrayList<Banco> listaDeBancos: Lista con todos los objetos Banco que se han creado.

- \- String nombreBanco : El nombre del Banco

- \- ArrayList<Cuenta> listaDeCuentas: Lista con todos los objetos de tipo Cuenta que tiene asociadas un Banco.

###  Métodos

\+ extraerCuenta(int cc, int nroCuenta, String tipoDeCuenta){

    - **Funcionamiento:**

    Recorre iterativamente la listaDeCuentas del Banco, buscando una Cuenta cuyos atributos coincidan con los 3 parámetros. De ser así retorna el objeto, o en caso contrario, retorna Null

    - **Retorno:** Void

---
