export class Euler {
  funcion: string;
  x0: number;
  x1: number;
  y: number;
  n: number;

  constructor(funcion: string, x0: number, x1: number, y: number, n: number) {
    this.funcion = funcion;
    this.x0 = x0;
    this.x1 = x1;
    this.y = y;
    this.n = n;
  }
}
