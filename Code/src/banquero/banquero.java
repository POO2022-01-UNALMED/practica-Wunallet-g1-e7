package banquero;

import java.util.Scanner;

public class banquero {
	static Scanner sc = new Scanner(System.in);
	static long readLong() {
		return sc.nextLong();
	}
	static String readln() {
		sc.nextLine();
		return sc.nextLine();
	}
	
	
	public static void main (String args[]) {
		int optionUser;
		
		do {
			System.out.println("¿Qué usuario desea selecionar?");
			System.out.println(" 1. Juan Perez");
			System.out.println(" 2. Hernesto Perez");
			System.out.println(" 0. Salida segura");
			System.out.print("Ingrese la opción :");
			optionUser = (int) readLong();
			
			switch (optionUser) {
//			Primer usuario.
			case 1: 
				int option;
					
				do {
					System.out.println("¿Qué operación desea realizar?");
					System.out.println(" 1. Inscribir cuenta");
					System.out.println(" 2. Romper topes");
					System.out.println(" 3. Solicitar credito");
					System.out.println(" 4. Ver historial de transacciones");
					System.out.println(" 5. Tranferir");
					System.out.println(" 6. Salida segura");
					System.out.println(" 7. Volver al menú de usuarios");
					System.out.print("Ingrese la opción :");
					
					option = (int) readLong();
					
					switch(option) {
					case 1: System.out.print("Método que ejecuta a inscribir cuentas");break;
					case 2: System.out.print("Método que ejecuta a romper topes");break;
					case 3: System.out.print("Método que ejecuta a solicitar credito");break;
					case 4: System.out.print("Método que ejecuta a ver historial de transacciones");break;
					case 5: System.out.print("Método que ejecuta a tranferir");break;
					case 6: break;
//					Hacen lo mismo xD
					case 7: break;
					}
					
					
				}while(option != 0);break;
				
				
				
//			Segundo usuario.
			case 2: 
				int option2;
					
				do {
					System.out.println("¿Qué operación desea realizar?");
					System.out.println(" 1. Inscribir cuenta");
					System.out.println(" 2. Romper topes");
					System.out.println(" 3. Solicitar credito");
					System.out.println(" 4. Ver historial de transacciones");
					System.out.println(" 5. Tranferir");
					System.out.println(" 6. Salida segura");
					System.out.println(" 7. Volver al menú de usuarios");
					System.out.print("Ingrese la opción :");
					
					option2 = (int) readLong();
					
					switch(option2) {
					case 1: System.out.print("Método que ejecuta a inscribir cuentas");break;
					case 2: System.out.print("Método que ejecuta a romper topes");break;
					case 3: System.out.print("Método que ejecuta a solicitar credito");break;
					case 4: System.out.print("Método que ejecuta a ver historial de transacciones");break;
					case 5: System.out.print("Método que ejecuta a tranferir");break;
					case 6: break;
//					Hacen lo mismo xD
					case 7: break;
					}
					
					
				}while(option2 != 0);break;
			}
		} while(optionUser != 0);
			
		
	}
}
