import java.util.Locale;
import java.util.Scanner;



public class App {
    public static void main(String[] args) {
        
        Locale.setDefault(Locale.US);

        Scanner sc = new Scanner(System.in);

        int x, y, aux, soma;

        System.out.println("Digite dos numeros: ");
        x = sc.nextInt();
        y = sc.nextInt();

        if (x > y) {
            aux = x;
            x = y;
            y = aux;
                    
        }
        soma = 0;
        for (int i = x+1; i < y; i++) {
            if (i % 2 != 0) {
                soma = soma +1;
            }
            
        }
        System.out.println("Soma dos Impares: " +soma);


        sc.close();
    }
}
