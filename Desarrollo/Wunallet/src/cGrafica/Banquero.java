package cGrafica;
import java.util.Scanner;

import basedatos.Deserializador;
import gestorAplicacion.infoClientes.Banco;
import gestorAplicacion.infoClientes.PerfilCreditico;
import gestorAplicacion.infoClientes.Usuario;
import gestorAplicacion.infoClientes.comportamientoDePago;
//import gestorAplicacion.personal.Dependiente;
import gestorAplicacion.productosFinancieros.Ahorro;
import gestorAplicacion.productosFinancieros.BajoMonto;
import gestorAplicacion.productosFinancieros.Corriente;
import gestorAplicacion.productosFinancieros.Credito;
import gestorAplicacion.productosFinancieros.Cuenta;

import java.math.BigDecimal;
import java.text.DecimalFormat;
import basedatos.*;


public class Banquero {

	static Scanner sc = new Scanner(System.in);
	
	static long readLong() {
		return sc.nextLong();
	}
	
	static int readInt() {
		return sc.nextInt();
	}
	
	static String readln() {
		sc.nextLine();
		return sc.nextLine();
	}
	
	
	
	public static void main (String args[]) {
	
	
	cargar();
	inicializa();
	
    System.out.println("                                                                    :~^^^^^^~:  :~^^^^^^^^  :~^^^^^^^^");                            
	System.out.println("                                                                    :5PPPPPP5^  :5PPPPPPP~  .YPPPPPPP~");                            
	System.out.println("                                                                     7PPPPPP?    7PPPPPPJ    ~PPPPPPY ");                            
	System.out.println("                                                                     7PPPPPP?    7PPPPPPJ    ~PPPPPPJ ");                            
	System.out.println("                                                                     7PPPPPP?    7PPPPPPJ    ~PPPPPPJ ");                            
	System.out.println("                                                                     7PPPPPP?    7PPPPPPJ    ~PPPPPPJ ");                            
	System.out.println("                                                                     7PPPPPP?    7PPPPPPJ    ~PPPPPPJ ");                            
	System.out.println("                                                                     7PPPPPP?    7PPPPPPJ    ~PPPPPPJ ");                            
	System.out.println("                                                                     JPPPPPPJ    7PPPPPPJ    7PPPPPPY.");                            
	System.out.println("                                                                    !PPPPPPPP7   7PPPPPPJ   ~PPPPPPPP?");                            
	System.out.println("                                                                    ~PPPPPPPP~   7PPPPPPJ   :5PPPPPPP7");                            
	System.out.println("                                                                     ?PPPPPPJ    7PPPPPPJ    7PPPPPPY.");                            
	System.out.println("                                                                     7PPPPPP?    7PPPPPPJ    ~PPPPPPJ ");                            
	System.out.println("                                                                :~?JY5PPPPPP?    7PPPPPPJ    ~PPPPPPJ ");                            
	System.out.println("                                                             :7YPPGP5555PPPPPJ:  7PPPPPPJ    ~PPPPPPJ ");                            
	System.out.println("                                                            !5GPPY!^....^?PPPPY. 7PPPPPPJ    ~PPPPPPJ ");                            
	System.out.println("                                                           ?PP7!!        .5PPPY. 7PPPPPPJ    ~PPPPPPJ ");                            
	System.out.println("                                                          ~P5^         .^JPP5?:  !PPPPPPJ    ~PPPPPPJ ");                            
	System.out.println("                                                          JP~        .:^!7!~^..:.7PPPPPPJ:::.!PPPPPPJ ");                            
	System.out.println("                                                         .5Y.        7P5555555PP5PPPPPPPP55P5PPPPPPPJ ");                            
	System.out.println("                                                          Y5.        7PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPY ");                            
	System.out.println("                                                          ^P!       :5PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP~");                            
	System.out.println("                                                           ~5!      :^^^^^^^^^^75PPPPPPPY^^^^^^^^^^^^^");                            
	System.out.println("                                                            .7?~.:~^.      .^!JPPPPY7?5PP!            ");                            
	System.out.println("                                                              .!?77JYYYYYY5PPGPPY7^.  .:^~:           ");                            
	System.out.println("                                                                 :^!7?JYYYJJ?!^:                      ");                            
	System.out.println("                                                                                                      ");                                                                                                                             
	System.out.println("                                                                                                      ");                                                                                                    
	System.out.println("                                                                                                      ");                                                                                                    
	System.out.println("                                                                                                      ");                                                                                                    
	System.out.println("                                     :J! ^Y~ ~Y^ 	^Y~ :J!     .?J.  ??.      ?J.       ??.     ~Y^     7JJJJ. ^??J??^ ");                  
	System.out.println("                                     :PY 7G? ?G^ 	~G7 ^G7     .5G!  Y5.     :PP^      .55.     7G~     JP~:^   .!G7.. ");                  
	System.out.println("                                     .55.?PJ JP: 	~P7 ^P7     .5P5. Y5.     ^PP!      .Y5.     7P^     JP:      ~P!   ");                  
	System.out.println("                                     .YP:JPY.55: 	~P7 ^P7     .5PP! Y5.     7PP?      .Y5.     7P^     JP:      ~P!   ");                  
	System.out.println("                                      JP~YP5^55. 	~P7 ^P7     .55P5:Y5.     JPPY.     .Y5.     7P^     JP~^^    ~P!   ");                  
	System.out.println("                                      ?P75P5!PY. 	~P7 ^P7     .5J?P7J5.    .5J?P:     .Y5.     7P^     JPJJ?.   ~P!   ");                  
	System.out.println("                                      7P5P755PJ  	~P7 ^P7     .5J:P555.    :P7~P~     .Y5.     7P^     JP:      ~P!   ");                  
	System.out.println("                                      !PP5.JPP?  	~P7 ^P7     .5Y ?PP5.    ~PYJP7     .Y5.     7P^     JP:      ~P!   ");                  
	System.out.println("                                      ~PP? !PP7  	~P7 ^P7     .5Y :5P5.    7P~^5J     .Y5.     7P^     JP:      ~P!   ");                  
	System.out.println("                                      ^PP^ :5P!  	~G7 ^G7     .5Y  ?P5.    J5. Y5.     Y5.     7P^     JP:      ~G!   ");                  
	System.out.println("                                      :PY.  JP~  	:J5Y5Y^     .5Y  :55.   .5J  ?P:     YPJJ7   !PYJJ^  ?PYJJ.   ~P!   ");                   
	
//	for(Banco i:Banco.listaBancos) {
//		System.out.println("Banco "+ i.getNombreBanco());
//	}
//	
	
//		int optionUser;
//		Usuario usuario;
//		do {
//			System.out.println("----------------------------------------------");
//			System.out.println("¿Que usuario desea realizar?");
//			System.out.println(" 1. Juan Perez");
//			System.out.println(" 2. Hernesto Perez");
//			System.out.println(" 0. Salida segura");
//			System.out.println("----------------------------------------------");
//			System.out.print("Ingrese la opcion :");
//			optionUser = (int) readLong();
//			System.out.println("----------------------------------------------");
//			
//				
//			
//			switch (optionUser) {
////			Primer usuario.
//			case 1: usuario = juanPerez; 
//					funcionalidadesEjecucion(usuario);
//					break;
//					
//				
////			Segundo usuario.
//			case 2: usuario = hernestoPerez;
//					funcionalidadesEjecucion(usuario);
//					break;
//			
//			case 3: salirDelSistema();break;
//				
//			}
//		} while(optionUser != 5);
		
	int optionUser;
	do {
		System.out.println("----------------------------------------------");
		System.out.println("	¿Que usuario desea realizar?");
		System.out.println("----------------------------------------------");
		int uC = 0;
		for(Usuario usuarioI:Usuario.getUsuario()) {
			uC++;
			System.out.println(uC + ". Usuario con CC: "+ usuarioI.getCc());
		}
		System.out.println("0. Salida segura");
		System.out.println("----------------------------------------------");
		System.out.print("	Ingrese la opcion :");
		optionUser = (int) readLong();
		System.out.println("----------------------------------------------");
		
		switch (optionUser) {
	//		Primer usuario.
			case 1: 
					System.out.println("Usted seleccionó: "+ Usuario.getUsuario().get(0).getCc());
					System.out.println("----------------------------------------------");
					funcionalidadesEjecucion(Usuario.getUsuario().get(0));
					break;
					
				
	//		Segundo usuario.
			case 2: 
					System.out.println("Usted seleccionó: "+ Usuario.getUsuario().get(1).getCc());					
					System.out.println("----------------------------------------------");
					funcionalidadesEjecucion(Usuario.getUsuario().get(1));
					break;
			
			case 3: salirDelSistema();break;
		}
	} while(optionUser != 0);
	
		
		
		
	}
	
	public static void inicializa() {
//		Creación de algunos usuarios
		if ((Banco.listaBancos.isEmpty()) && (Usuario.getUsuario().isEmpty())) {
			System.out.println("CREANDO ....");
			Usuario juanPerez = new Usuario(null,1000000,10,null);
			Usuario hernestoPerez = new Usuario(null,1000000,98,null);

			Banco Unalombia = new Banco("Unalombia",(float)1.6);
			Banco PooBanco = new Banco("PooBanco",(float)2.5);
			Banco QuitaVivienda = new Banco("QuitaVivienda",(float)36.0);
		
			Cuenta cuenta1 = new Ahorro(89,juanPerez, (float)10000.0 ,QuitaVivienda,"ahorro",(float)36.0);
		
			Cuenta cuenta3 = new Corriente(23,juanPerez,(float)50000000.0,Unalombia,"corriente",(float)2000000);
			Cuenta cuenta2 = new BajoMonto(69,hernestoPerez, (float)1000000.0,PooBanco, "bajoMonto", (float)5.0,(float)3000000.0,(float)3000000.0);
			Cuenta cuenta4 = new BajoMonto(26,hernestoPerez, (float)6000000.0,Unalombia, "bajoMonto", (float)5000.0,(float)3000.0,(float)3000.0);
		}
	}
	
	
	

	public static void funcionalidadesEjecucion(Usuario usuario) {
		int option;
		
		
		do {
			System.out.println("----------------------------------------------");
			System.out.println("	& ¿Que operacion desea realizar?");
			System.out.println("----------------------------------------------");
			System.out.println(" 1. Inscribir cuenta");
			System.out.println(" 2. Romper topes");
			System.out.println(" 3. Solicitar credito");
			System.out.println(" 4. Ver historial de transacciones");
			System.out.println(" 5. Tranferir");
			System.out.println(" 6. Volver a seleccionar usuario");
			System.out.println(" 7. Volver al menu de usuarios");
			System.out.println("----------------------------------------------");
			System.out.print("Ingrese la opcion :");
			option = (int) readLong();
			System.out.println("----------------------------------------------");
			
			switch(option) {
//			case 1: System.out.print("Metodo que ejecuta a inscribir cuentas");break;
			case 1: inscribirCuenta(usuario);break;
			case 2: romperTopes(usuario);break;
			case 3: solicitarCredito(usuario);break;
			case 4: verHistorial(usuario);break;
			case 5: transferir(usuario);break;
			case 6: salirDelSistema();break;
			case 7: break;
//			Hacen lo mismo xD
			}
			
		}while(option != 7);
	}
	
	
	
	
//	-------------------------------------- Metodos --------------------------------------	
	
	
	
	static void inscribirCuenta(Usuario usuario) {
		
		System.out.println("	#   Inscribir cuenta");
		System.out.println("----------------------------------------------");
		
		
//		SelecciÃ³n del banco - InscribirCuenta.SeleccionBanco
	
		System.out.println("	- Seleeccion del banco");
		System.out.println("----------------------------------------------");
		int c = 0;
		for(Banco i: Banco.listaBancos) {
			System.out.println((c+1) + ". " + i.getNombreBanco());
			c++;
		}
		String nombreBanco = null;
		System.out.println("----------------------------------------------");
		System.out.print("- Seleccione de que banco es la cuenta que desea inscribir: ");
		int numBanco = readInt();
		System.out.println("----------------------------------------------");
		Banco banco = null;		
		switch(numBanco) {
		case 1: banco = Banco.extraerBanco("Unalombia");break;
		case 2: banco = Banco.extraerBanco("PooBanco");break;
		case 3: banco = Banco.extraerBanco("QuitaVivienda");break;
		}
		        
		nombreBanco = banco.getNombreBanco();
		System.out.println("	R / Usted selecciono " + nombreBanco);
		System.out.println("----------------------------------------------");

		
//		Seleccione el tipo de cuenta - InscribirCuenta.SeleccionTipoCuenta
		
		System.out.println("     - Seleección tipo de cuenta");
		System.out.println("----------------------------------------------");
		System.out.println("1. Cuenta de bajo monto ");
		System.out.println("2. Cuenta de ahorros");
		System.out.println("3. Cuenta corriente ");
		System.out.println("4. Volver al menú de funcionalidades");
		System.out.print("Seleccione el tipo de cuenta: ");
		int tipCuenta = readInt(); 
		System.out.println("----------------------------------------------");
		
		String tipoCuenta = null;
		
		switch(tipCuenta) {
		case 1: tipoCuenta = "bajoMonto";break;
		case 2: tipoCuenta = "ahorro";break;
		case 3: tipoCuenta = "corriente";break;
		}
		System.out.println(" R / Usted seleccionó " + tipoCuenta);
		System.out.println("----------------------------------------------");
		
//		SelecciÃ³n del banco - InscribirCuenta.IngresoNumeroCuenta
		
		System.out.println("	- Insersión del número de cuenta");
		System.out.println("----------------------------------------------");
		System.out.print("Ingrese el número de la cuenta: ");
		int numeroCuenta = readInt();
		System.out.println("----------------------------------------------");
		
//		ComprobaciÃ³n de la existencia de la cuenta
		
		Cuenta existeCuenta = banco.extraerCuenta(numeroCuenta);
		if (existeCuenta != null) {
			
		}else {
			System.out.println("----------------------------------------------");
			System.out.println("R / Numero de cuenta "+numeroCuenta+" no existe en el banco: " + nombreBanco);
			System.out.println("----------------------------------------------");
			return ;
			
		}
		
//		SelecciÃ³n del banco - InscribirCuenta.IngresoNumeroCedula
		
		System.out.println("	- Insersión del número de cédula");
		System.out.print("Ingrese el número de cedula: ");
		int numeroCc = readInt();
		System.out.println("----------------------------------------------");

//		ComprobaciÃ³n de la existencia del usuario
		
		Usuario existeUsuario = existeCuenta.getTitular();
		
		if (existeUsuario.getCc() == numeroCc) {
			
		}else {
			System.out.println("----------------------------------------------");
			System.out.println("R / Numero de cedula "+numeroCc+" no concuerda con la cuenta");
			System.out.println("----------------------------------------------");
			return ;
		}
		
//		Llamado del mÃ©todo inscribir
		
		
		usuario.inscribir(numeroCuenta,nombreBanco);
		System.out.println("----------------------------------------------");
		System.out.println("R / " + usuario);
		System.out.println("----------------------------------------------");
//		System.out.println(usuario.getListaIncritos());

		
	
	}
	
	static void verHistorial(Usuario usuario) {
		System.out.println("----------------------------------------------");
		System.out.println("		# Ver Historial");
		System.out.println("----------------------------------------------");
		
//		VerHistorial.SeleccionCuenta
		
		System.out.println("   - Las cuentas que teiene asociadas son: ");
		System.out.println("----------------------------------------------");
		int coVh = 0;
		
		for(Cuenta cuentas : usuario.getCuentasAsociadas()) {
			coVh++;
			System.out.println(coVh + ". Cuenta " + cuentas.getNroCuenta());	
		}
		System.out.println("----------------------------------------------");
		System.out.print("Seleccione la cuenta de la que quiere ver el historial: ");
		int vhCuenta = readInt(); 
		System.out.println("----------------------------------------------");
				
        Cuenta cuentaVH = usuario.getCuentasAsociadas().get(vhCuenta-1);
        System.out.println("R / Usted eligio: "+cuentaVH.getNroCuenta());
		System.out.println("----------------------------------------------");
		
		
//		VerHistorial.Historial.SinHistorial
	
		if(cuentaVH.getHistorialTransferencia().isEmpty()) {
			
			System.out.println("R / No tiene historial de transacciones");
			System.out.println("----------------------------------------------");
			return ;
		}else {
//			VerHistorial.Historial.ConHistorial
			cuentaVH.verHistorial();
		}
			

		
		
		
	}
	
	
	static void solicitarCredito(Usuario usuario) {
		System.out.println("----------------------------------------------");
		System.out.println("	   # Solicitar credito");
		System.out.println("----------------------------------------------");
//		Verificar si tiene un crÃ©dito
		
		if(usuario.getCreditoActivo() != null) {
			System.out.println("R / El usuario " + usuario.getCc() +" ya tiene un crédito activo");
			return ;
		}
		
		
//		SolicitarCredito.SeleccionBanco
		System.out.println("	- Seleección del banco");
		System.out.println("----------------------------------------------");
		int c = 0;
		for(Banco i: Banco.listaBancos) {
			System.out.println((c+1) + ". " + i.getNombreBanco() + " tasa de interés del " + i.getTasaInteresAnual() + " anual");
			c++;
		}
		String nombreBanco = null;
		System.out.println("----------------------------------------------");
		System.out.print("Seleccione a que banco corresponde la cuenta que desea inscribir: ");
		int numBanco = readInt();
		System.out.println("----------------------------------------------");
		Banco banco = null;
		
		switch(numBanco) {
			case 1: banco = Banco.extraerBanco("Unalombia");break;
			case 2: banco = Banco.extraerBanco("PooBanco");break;
			case 3: banco = Banco.extraerBanco("QuitaVivienda");break;
		}
		        
		nombreBanco = banco.getNombreBanco();
		System.out.println("R / Usted selecciono " + nombreBanco + " que tiene una tasa de interés de " + banco.getTasaInteresAnual() + " anual");
		System.out.println("----------------------------------------------");
		
//		SolicitarCredito.SolicitarCuenta
		
		System.out.println("	- Las cuentas que tiene asociadas son: ");
		System.out.println("----------------------------------------------");
		int coSc = 0;
		
		for(Cuenta cuentas : usuario.getCuentasAsociadas()) {
			coSc++;
			System.out.println(coSc + ". Cuenta " + cuentas.getNroCuenta());	
		}
		System.out.println("----------------------------------------------");
		System.out.print("Seleccione la cuenta de la que desea guardar el crédito: ");
		int scCuenta = readInt(); 
		Cuenta CuentaSc = usuario.getCuentasAsociadas().get(scCuenta-1);	
		
		
//		SolicitarCredito.IngresoMonto
		System.out.println("----------------------------------------------");
		System.out.print("Ingrese el monto en pesos a solicitar: ");
		float monto = readLong();
		System.out.println("----------------------------------------------");
		System.out.println(" R / Usted ingresó " + monto);
		System.out.println("----------------------------------------------");
		
//		SolicitarCredito.IngresoPlazos
		System.out.print("Ingrese el plazo en meses del crédito: ");
		int plazo = readInt();
		System.out.println("----------------------------------------------");
		System.out.println("R / Usted ingresó " + plazo);
		
//		SolicitarCredito.SolicitarCuenta
		System.out.println("----------------------------------------------");
		System.out.println("R / Saldo antes del credito " + String.format("%.1f", CuentaSc.getSaldo()));
		int sCredito = usuario.solicitarCredito(banco, monto, plazo,CuentaSc);
		switch(sCredito) {
		case 1: 
			System.out.println("----------------------------------------------");
			System.out.println("R / Credito rechazado por mal comportamiento crediticio");
			System.out.println("----------------------------------------------");
			break;
		case 2: 
			System.out.println("----------------------------------------------");
			System.out.println("R / Credito rechazado por falta de capacidad de endeudamiento");
			System.out.println("----------------------------------------------");
			break;
		case 3: 
			System.out.println("----------------------------------------------");
			System.out.println("R / Tu solicitud de crédito ha sido aprobada y tu saldo actual es: "+ String.format("%.1f", CuentaSc.getSaldo()) );
			System.out.println("----------------------------------------------");
			break;
		}
	}
	
	
	
	static void romperTopes(Usuario usuario) {
		System.out.println("----------------------------------------------");
		System.out.println("	# Romper topes");
		
//		Chaqueo de las cuentas debajo monto
		int cRT = 0;
		for(Cuenta cuentaI : usuario.getCuentasAsociadas()) {
			if(cuentaI instanceof BajoMonto) {
				cRT++;
//				System.out.println(cRT + " Cuenta "+ cuentaI.getNroCuenta());
			}
		}
		
		
		
//		RomperTopes.SinCuentaBajoMonto				
		if(cRT == 0) {
			System.out.println("----------------------------------------------");
			System.out.println("R / Esta funcionalidad no está habilitada para tus cuentas.");
			System.out.println("----------------------------------------------");
			return ;
		}
		
//		RomperTopes.ConCuentaBajoMonto
		System.out.println("----------------------------------------------");
		System.out.println("¡Recuerde! El procedimiento de romper topes consiste en transformar su cuenta de tipo Bajo monto, ");
		System.out.println("a una cuenta de ahorros convencional, eliminando las limitaciones de este tipo de cuentas.");
		System.out.println("Este proceso tiene un costo de 15.000 pesos que pagará una única vez.");
		System.out.println("----------------------------------------------");
		
		System.out.println("	- Selecci�n de cuenta");
		System.out.println("----------------------------------------------");
		int cRT_1 = 0;
		for(Cuenta cuentaI : usuario.getCuentasAsociadas()) {
			if(cuentaI instanceof BajoMonto) {
				cRT_1++;
				System.out.println(cRT_1 + " Cuenta "+ cuentaI.getNroCuenta());
			}
		}
		System.out.println("----------------------------------------------");
		System.out.print(" - Para continuar seleccione la cuenta de bajo monto que desea transformar: ");
		int rtCuenta = readInt(); 
		
		Cuenta CuentaRt = usuario.getCuentasAsociadas().get(rtCuenta-1);	
		System.out.println("R / Usted seleccionó: " + CuentaRt.getNroCuenta());
		System.out.println("----------------------------------------------");
		
		Banco banco = ((BajoMonto)CuentaRt).getBanco(); 
		
//		int cRT_3 = 0;
//		for(Cuenta CuentaI : banco.getListaCuentas()) {
//			cRT_3++;
//			System.out.println(cRT_3 + " Cuenta antes de romper topes "+ CuentaI.getNroCuenta());
//		}	
		
		boolean c = ((BajoMonto)CuentaRt).romperTopes();
		int numeroCuenta = ((BajoMonto)CuentaRt).getNroCuenta();
		usuario.removerCuentaAsociada(CuentaRt);
		banco.removerCuenta(CuentaRt);

		if (c == false) {
			System.out.println("R / Tu solicitud ha sido rechazada ya que no cuentas con saldo suficiente en tu cuenta para realizar el proceso.");
			System.out.println("----------------------------------------------");
		}else {
			
//			CuentaRt = null;
//			System.gc();
			System.out.println("R / Tu solicitud ha sido aprobada, se descontarán $15.000 de tu saldo para realizar el proceso. Espera un momento...");
			System.out.println("----------------------------------------------");
			System.out.println("R / Tu cuenta ha sido actualizada y ahora no tiene topes.");
			Cuenta cANueva = banco.extraerCuenta(numeroCuenta);
//			for(Cuenta cuentaAhorro : banco.getListaCuentas()) {
////				numeroCuenta
//				if(cuentaAhorro.getNroCuenta() == numeroCuenta) {
//					cANueva = cuentaAhorro;
//				}
//			}
//			if(cANueva instanceof BajoMonto) {
//				System.out.println("AUN ES BAJO MONTO :c");
//			}else {
//				System.out.println("Si se actualizï¿½");
//			}
			
			System.out.println("R / Tu nueva cuenta de ahorros ahora tiene un saldo de: "+cANueva.getSaldo() +".");
			System.out.println("----------------------------------------------");
			
//			int cRT_2 = 0;
//			for(Cuenta cuentaI : usuario.getCuentasAsociadas()) {
//				if(cuentaI instanceof BajoMonto) {
//					cRT_2++;
//					System.out.println(cRT_2 + " Cuenta "+ cuentaI.getNroCuenta());
//				}
//			}
//			int cRT_2 = 0;
//			for(Cuenta CuentaI : banco.getListaCuentas()) {
//				cRT_2++;
//				if(CuentaI instanceof BajoMonto) {
//					System.out.println(cRT_2 + " Cuenta "+ CuentaI.getNroCuenta());				
//				}else {
//					System.out.println("Papi todo estÃ¡ melo");
//				}
//			}
			
			
		}
		
	}
	
	
	static void transferir(Usuario usuario) {
		System.out.println("----------------------------------------------");
		System.out.println("	# Transferir ");
		System.out.println("----------------------------------------------");
//		Transferir.SeleccionCuentaOrigen
		
		System.out.println("- Selecciona el producto de origen que quieres usar: ");
		System.out.println("----------------------------------------------");
		int cT = 0;
		
		for(Cuenta cuentas : usuario.getCuentasAsociadas()) {
			cT++;
			System.out.println(cT + ". Cuenta " + cuentas.getNroCuenta());	
		}
		System.out.println("----------------------------------------------");
		System.out.print("Seleccione la cuenta de la cual quiere realizar una transferencia: ");
		int tCuenta = readInt(); 
		System.out.println("----------------------------------------------");
				
        Cuenta cuentaT = usuario.getCuentasAsociadas().get(tCuenta-1);	
		System.out.println("R / Usted eligio la cuenta "+cuentaT.getNroCuenta());
		System.out.println("----------------------------------------------");
		
//		Transferir.SeleccionTipoTransferencia
		System.out.println("- Seleección tipo de transferencia");
		System.out.println("----------------------------------------------");
		System.out.println("Selecciona qué tipo de transferencia quieres hacer");
		System.out.println("1. Pagar credito");
		System.out.println("2. Transferencia a otra cuenta");
		System.out.println("----------------------------------------------");
		System.out.print("Ingrese el tipo de transferencia: ");
		int  tipoTransferencia = readInt(); 
		System.out.println("----------------------------------------------");
		
		switch(tipoTransferencia) {
			case 1: 
				System.out.println("R / Selecionaste: pagar credito");
				System.out.println("----------------------------------------------");
								
	//			Transferir.PagarCredito.SinCredito	
				if(usuario.getCreditoActivo()==null) {
					System.out.println("No tienes ningún crédito activo para pagar.");
					System.out.println("----------------------------------------------");
					return;
				}
	//			Transferir.PagarCredito.ConCredito
				Credito creditoActivo = usuario.getCreditoActivo();
				System.out.println("R / Tu crédito es de "+ creditoActivo.getDeuda() +" y pagarás una cuota de "+creditoActivo.getCuotaMensual()+".");
				System.out.println("----------------------------------------------");
				System.out.println("- Confirmar pago");
				System.out.println("----------------------------------------------");
				System.out.println("1. Si");
				System.out.println("2. Volver al menú de funcionalidades.");
				System.out.println("----------------------------------------------");
				System.out.print("Ingrese su respuesta: ");
				int  continuar1 = readInt(); 
				System.out.println("----------------------------------------------");
				
				boolean exito = false;
				switch(continuar1) {
				case 1: 
					
					exito = cuentaT.transferir(creditoActivo);
					if(exito==true) {
						System.out.println("R / Tu pago ha sido exitoso. Tu credito restante es de "+ (creditoActivo.getDeuda()-creditoActivo.getCuotaMensual()) );
						System.out.println("----------------------------------------------");
					}else {
						System.out.println("R / Tu pago ha sido rechazado ya que no cuentas con saldo suficiente o tu producto de origen no permite mover el valor indicado.");
						System.out.println("----------------------------------------------");
					}
				
					break;
				case 2: break;
				
				}
				
				
				
					
				
				
				break;
			case 2: 
				System.out.println("R / Selecionaste: tranferir a otra cuenta.");
				System.out.println("----------------------------------------------");
	//			Transferir.OtraCuenta.SeleccionStatusDeInscripcion
				System.out.println("- Seleccione a qué tipo de cuenta quieres transferir:");
				System.out.println("----------------------------------------------");
				System.out.println("1. Cuentas inscritas");
				System.out.println("2. Cuentas no inscritas");
				System.out.println("----------------------------------------------");
				System.out.print("Ingrese aca la selección: ");
				int continuar2 = readInt();
				System.out.println("----------------------------------------------");
				
				switch(continuar2) {
				case 1: 
					
					System.out.println("R / Selecionaste: cuentas inscritas.");
					System.out.println("----------------------------------------------");
		//			Transferir.OtraCuenta.Inscritas;
					
					if((usuario.getListaIncritos()).size() == 0) {
						System.out.println("R / No tiene cuentas inscritas");
						break;
					}
					
					
					System.out.println("- Seleccion cuenta destino");
					int cCIns = 0;
					for(Cuenta c : usuario.getListaIncritos()) {
						cCIns++;
						System.out.println(cCIns + ". Cuenta "+ c.getNroCuenta());	
					}
					System.out.println("----------------------------------------------");
					System.out.print("- Seleccione la cuenta de destino: ");
					int cInsc = readInt();
					System.out.println("----------------------------------------------");
					Cuenta cuentaTIns = usuario.getListaIncritos().get(cInsc-1);
					
					
					
//					Transferir.OtraCuenta.Inscritas.Error
					Banco bancoCins = cuentaTIns.getBanco();
					if(!bancoCins.getListaCuentas().contains(cuentaTIns)) {
						System.out.println("R / La cuenta inscrita que ha seleccionado ya no está disponible, por lo tanto será eliminada de su lista de cuentas inscritas.");
						usuario.removerCuentaIncrita(cuentaT);
						break;
					}
				
//					Transferir.OtraCuenta.Inscritas.IngresoValor
					System.out.print("Digite el valor que desea transferir: ");
					float valorTransferenciaCI = readLong();
					System.out.println("----------------------------------------------");
					System.out.println("R / Valor ingresado: " + valorTransferenciaCI);
					System.out.println("----------------------------------------------");
					
					boolean transferenciaOcIns = cuentaT.transferir(cuentaTIns,valorTransferenciaCI);					
					
					if(transferenciaOcIns) {
						System.out.println("R / Envío exitoso. El saldo de su cuenta es de "+ cuentaT.getSaldo()  +"." );
						System.out.println("----------------------------------------------");
//						System.out.println("CuentaOrigen" + cuentaT.getSaldo());
//						System.out.println("CuentaDestino" + cuentaTIns.getSaldo());
						
						
						break;
					}else {
						System.out.println("R / Hubo un error en la operaciÃ³n. Verifique que su cuenta de origen tenga y permita mover el saldo indicado.");
						System.out.println("----------------------------------------------");
						break;
					}
					
										
					
					
					
				case 2: 
					System.out.println("Selecionaste: cuentas no inscritas.");
					System.out.println("----------------------------------------------");
					
					
					
//					Transferir.OtraCuenta.NoInscritas.SeleccionBanco
					
					System.out.println("	- Seleección del banco");
					int c = 0;
					for(Banco i: Banco.listaBancos) {
						System.out.println((c+1) + ". " + i.getNombreBanco());
						c++;
					}
					String nombreBanco = null;
					System.out.println("----------------------------------------------");
					System.out.println("Seleccione de que banco es la cuenta que desea inscribir: ");
					int numBanco = readInt();
					System.out.println("----------------------------------------------");
					Banco banco = null;		
					System.out.println("hasta aca voy bien");
//					banco = (Banco.extraerBanco("PooBanco"));
//					System.out.println("ERORR "+ Banco.listaBancos);
					
//					Banco banco = Banco.extraerBanco("PooBanco");
//					for(Banco po:Banco.listaBancos) {
//						System.out.println("Banco "+ po.getNombreBanco());
//					}
//					
//					System.out.println("ERRORRRRRRRRRRR" + banco.getNombreBanco());
					switch(numBanco) {
					case 1: banco = Banco.extraerBanco("Unalombia");
//							System.out.println(" Usted selecciono " + banco.getNombreBanco());
							break;
					case 2: banco = Banco.extraerBanco("PooBanco");
//							System.out.println(" Usted selecciono " + banco.getNombreBanco());
							break;
					case 3: banco = Banco.extraerBanco("QuitaVivienda");
//						System.out.println(" Usted selecciono " + banco.getNombreBanco());
						break;
					}
					        
					nombreBanco = banco.getNombreBanco();
					System.out.println(" Usted selecciono " + nombreBanco);
					System.out.println("----------------------------------------------");
					
					
//					Transferir.OtraCuenta.NoInscritas.IngresoNumeroCuenta
					System.out.print("Ingrese el nÃºmero de cuenta de destino: ");
					int numCuentaDes = readInt();
					System.out.println("----------------------------------------------");
					System.out.println("El número de la cuenta ingresado es: " + numCuentaDes);
					System.out.println("----------------------------------------------");
					
					
					Cuenta cuentaDestino = banco.extraerCuenta(numCuentaDes);
					if (cuentaDestino != null) {
						
					}else {
						System.out.println("----------------------------------------------");
						System.out.println("Numero de cuenta "+numCuentaDes+" no existe en el banco: " + nombreBanco);
						System.out.println("----------------------------------------------");
						break ;
						
					}
					
					
					
					
//					Transferir.OtraCuenta.NoInscritas.IngresoValor
					System.out.print("Ingrese el valor a transferir - Cuentas no inscritas: ");
					float valorTransf = readLong();
					if(valorTransf > 3000000) {
						System.out.println("----------------------------------------------");
						System.out.println("El valor que ingresó supera el valor pertitido para cuentas no inscritas");
						System.out.println("Recuerde que valor máximo a transferir a una cuenta no inscirta es de 3'000.000");
						System.out.println("----------------------------------------------");
						break ;
					}
					
					System.out.println("----------------------------------------------");
					System.out.println("El valor a transferir ingresado: " + valorTransf);
					System.out.println("----------------------------------------------");
					
					
//					Transferir.OtraCuenta.NoInscritas.LlamadoFuncion
					boolean transferenciaOcNOIns = cuentaT.transferir(cuentaDestino,valorTransf);	
					if(transferenciaOcNOIns) {
						System.out.println("Envio exitoso. El saldo de su cuenta es de "+ cuentaT.getSaldo()  +"." );
						System.out.println("----------------------------------------------");
						System.out.println("Quedaste con un saldo de: " + cuentaT.getSaldo());
//						System.out.println("CuentaDestino" + cuentaDestino.getSaldo());
						
						
						break;
					}else {
						System.out.println("Hubo un error en la operación. Verifique que su cuenta de origen tenga y permita mover el saldo indicado.");
						System.out.println("----------------------------------------------");
						break;
					}

					
				}
				
				
				break;
			}
		

		
	}
	public static void salirDelSistema() {
		System.out.println("Vuelva pronto");
		Serializador.serializarTodo();
		System.exit(0);
	}
	
	public static void cargar() {
		Deserializador.deserializarTodo();
	}
	
	
	
	
}
