import { Component, OnInit} from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { EulerService }from 'src/app/services/eulerService';
import { Euler } from 'src/app/models/Euler';

@Component({
  selector: 'app-euler',
  templateUrl: './euler.component.html',
  styleUrls: ['./euler.component.css']
})
export class EulerComponent  implements OnInit{
  eventForm: FormGroup;
  titulo = 'Método Euler';
  lista: any[] = [];
  raiz: number = 0;
  selectedField: string = ''; // Campo seleccionado para actualizar


  constructor(
    private fb: FormBuilder,
    private eulerService: EulerService
  ) {
    this.eventForm = this.fb.group({
      funcion: ['', Validators.required],
      x_inicial: ['', Validators.required],
      y_inicial: ['', Validators.required],
      x_secundaria: ['', Validators.required],
      numero_iteraciones: ['', Validators.required],
    });


  }



  ngOnInit(): void { }

  consulta(){
    let euler: Euler = {

      funcion: this.eventForm.get('funcion')?.value,
      x0: this.eventForm.get('x_inicial')?.value,
      x1: this.eventForm.get('x_secundaria')?.value,
      y: this.eventForm.get('y_inicial')?.value,
      n: this.eventForm.get('numero_iteraciones')?.value,
    };

    this.eulerService.save(euler).subscribe(
      response => {
        console.log(response);
        const data = response.iteraciones;
        this.raiz = response.resultado;

        if (Array.isArray(data)) {
          this.lista = data;
          for (const iterator of this.lista) {
            console.log(iterator.iteracion);
          }
        } else {
          console.error('Los datos recibidos no son un array:', data);
        }

      },
      error => {
        console.log(error);
        this.eventForm.reset();
      }

    );

  }


  openCalculator(field: string) {
    this.selectedField = field; // Guarda el campo seleccionado
    const calculatorModal = document.getElementById('calculatorModal');
    if (calculatorModal) {
      calculatorModal.style.display = 'block';
    }
  }

  closeCalculator() {
    const calculatorModal = document.getElementById('calculatorModal');
    if (calculatorModal) {
      calculatorModal.style.display = 'none';
    }
  }

  saveFunction(func: string) {
    if (this.selectedField) {
      this.eventForm.get(this.selectedField)?.setValue(func);
      this.closeCalculator();
    }
  }

}
