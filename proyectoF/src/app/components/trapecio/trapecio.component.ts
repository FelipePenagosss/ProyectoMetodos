
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { trapecio } from 'src/app/models/trapecio';
import { trapecioService } from 'src/app/services/trapecioService';

@Component({
  selector: 'app-Trapecio',
  templateUrl: './trapecio.component.html',
  styleUrls: ['./trapecio.component.css']
})
export class TrapecioComponent implements OnInit {
  eventForm: FormGroup;
  titulo = 'Metodo Taprecio';
  lista: any[] = [];
  area: number = 0;
  imagen: string = '';

  constructor(
    private fb: FormBuilder,
    private trapeService: trapecioService
  ) {
    this.eventForm = this.fb.group({
      funcion: ['', Validators.required],
      a: ['', Validators.required],
      b:['',Validators.required],
      n: ['', Validators.required],
    });
  }

  ngOnInit(): void { }

  consulta() {
    console.log("Llegue al metodo del back");
    const trape: trapecio = {
      funcion: this.eventForm.get('funcion')?.value,
      a: this.eventForm.get('a')?.value,
      b:this.eventForm.get('b')?.value,
      n: this.eventForm.get('n')?.value
    };
    console.log("cree la constante");

    this.trapeService.save(trape).subscribe(
      response => {
        console.log("resolvi lo interno");
        console.log(response);
       
        this.area = response.Area;
        this.imagen = 'data:image/png;base64,' + response.Imagen;
        
      },
      error => {
        console.log(error);
        this.eventForm.reset();
      }
    );
  }
}

