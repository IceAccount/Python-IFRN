class Calculadora {
  somar(a: number, b: number): number {
    return a + b;
  }

  subtrair(a: number, b: number): number {
    return a - b;
  }

  multiplicar(a: number, b: number): number {
    return a * b;
  }

  dividir(a: number, b: number): number {
    if (b === 0) {
      throw new Error("Não é possível dividir por zero.");
    }
    return a / b;
  }
}

// Exemplo de uso
const calc = new Calculadora();

console.log("Soma:", calc.somar(10, 5));
console.log("Subtração:", calc.subtrair(10, 5));
console.log("Multiplicação:", calc.multiplicar(10, 5));
console.log("Divisão:", calc.dividir(10, 5));