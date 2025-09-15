using System;
using System.Globalization;

namespace teste1;

public class teste1
{
    

        static void Main(string[] args){

            CultureInfo ci = CultureInfo.InvariantCulture;

            double largura, altura, perimetro, diagonal, area;

            Console.Write("Base do retângulo: ");
            largura = double.Parse(Console.ReadLine(), ci);
            Console.Write("Altura do retângulo: ");
            altura = double.Parse(Console.ReadLine(), ci);

            area = largura * altura;
            perimetro = 2 * (largura + altura);
            diagonal = Math.Sqrt(Math.Pow(largura, 2.0) + Math.Pow(altura, 2.0));


            Console.WriteLine("Area = " + area.ToString("F4", ci));
            Console.WriteLine("Perimtro = " + perimetro.ToString("F4", ci));
            Console.WriteLine("Diagonal = " + diagonal.ToString("F4", ci));



        }
    


}
