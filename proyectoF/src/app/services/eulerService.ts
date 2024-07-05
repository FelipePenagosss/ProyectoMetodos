import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Euler } from '../models/Euler';

@Injectable({
  providedIn: 'root'
})
export class EulerService{
  private url='http://localhost:5008/euler'

  constructor(private http:HttpClient) { }

  save(euler:Euler): Observable<any> {
    return this.http.post(this.url, euler);
  }

}
