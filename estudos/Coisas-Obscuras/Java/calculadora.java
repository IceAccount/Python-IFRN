import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.println("=== CALCULADORA ===");
            System.out.println("1 - Soma");
            System.out.println("2 - Subtração");
            System.out.println("3 - Multiplicação");
            System.out.println("4 - Divisão");

            System.out.print("Escolha: ");
            int opcao = scanner.nextInt();

            System.out.print("Primeiro número: ");
            double num1 = scanner.nextDouble();

            System.out.print("Segundo número: ");
            double num2 = scanner.nextDouble();

            double resultado = 0;

            switch (opcao) {
                case 1:
                    resultado = num1 + num2;
                    break;
                case 2:
                    resultado = num1 - num2;
                    break;
                case 3:
                    resultado = num1 * num2;
                    break;
                case 4:
                    if (num2 == 0) {
                        System.out.println("Não pode dividir por zero!");
                        return;
                    }
                    resultado = num1 / num2;
                    break;
                default:
                    System.out.println("Opção inválida!");
                    return;
            }

            System.out.println("Resultado: " + resultado);

        } catch (Exception e) {
            System.out.println("Erro: digite apenas números!");
        }

        scanner.close();
    }
}