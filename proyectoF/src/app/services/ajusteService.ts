import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ajusteService {
  private apiUrl = 'http://localhost:5010/ajuste_lineal_de_curvas';

  constructor(private http: HttpClient) {}

  save(ajuste: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, ajuste);
  }
}
