import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ajusteService } from 'src/app/services/ajusteService';
import { ajuste } from 'src/app/models/ajuste';

@Component({
  selector: 'app-ajuste-lineal-de-curvas',
  templateUrl: './ajuste.component.html',
  styleUrls: ['./ajuste.component.css']
})
export class ajusteComponent implements OnInit {
  eventForm: FormGroup;
  titulo = 'Método ajuste lineal de curvas';
  lista: any[] = [];
  raiz: number = 0;
  imagen: string = '';

  constructor(
    private fb: FormBuilder,
    private ajusteService: ajusteService
  ) {
    this.eventForm = this.fb.group({
      PuntosX: ['', Validators.required],
      PuntosY: ['', Validators.required],
    });
  }

  ngOnInit(): void { }

  consulta() {
    const puntosX = this.eventForm.get('PuntosX')?.value.split(',').map(Number);
  const puntosY = this.eventForm.get('PuntosY')?.value.split(',').map(Number);

    // Crear el objeto ajuste con las propiedades esperadas
    const ajusteData = { PuntosX: puntosX, PuntosY: puntosY };

    this.ajusteService.save(ajusteData).subscribe(
      response => {
        console.log(response);
        const data = response.Iteraciones;
        this.raiz = response.Raiz;
        this.imagen = 'data:image/png;base64,' + response.Imagen;
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
}
