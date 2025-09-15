import java.util.Locale;
import java.util.Scanner;



public class App {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int a, b, c, menor;

        System.out.println("Primeiro valor: ");
        a = sc.nextInt();
        System.out.println("Segundo valor: ");
        b = sc.nextInt();
        System.out.println("Terceiro valor: ");
        c = sc.nextInt();

        if (a < b && a < c) {
            menor = a;
            
        } else if (b < c) {
            menor = b;
            
        }else{
            menor = c;
        }

        System.out.println("Menor = " + menor);



        sc.close();
    }
}
