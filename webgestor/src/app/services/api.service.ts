import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private baseUrl = 'http://localhost:8000'; // Reemplaza esto con la URL de tu API

  constructor(private http: HttpClient) {}


//USUARIOS
  getUsers(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/usuarios`);
  }

  getUserById(userId: number): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/usuarios/${userId}`);
  }

  createUser(user: any): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/usuarios/`, user);
  }

  updateUser(user: any): Observable<any> {
    const userId = user.id; // Asume que tienes un campo 'id' en tu objeto de usuario
    return this.http.put<any>(`${this.baseUrl}/usuarios/${userId}`, user);
  }

//STOCK
  // Métodos para stock de productos
  getStock(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/stock`);
  }

  createStock(stock: any): Observable<any>{
    return this.http.post<any>(`${this.baseUrl}/stock/`, stock);
  }

//CLIENTES
  getClientes():Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/clientes`);
  }

  createClientes(cliente: any):Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/clientes`, cliente);
  }

  // Otros métodos para obtener tiendas, crear registros, etc.
}
