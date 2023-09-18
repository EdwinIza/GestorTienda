import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';


@Component({
  selector: 'app-prueba-api',
  templateUrl: './prueba-api.component.html',
  styleUrls: ['./prueba-api.component.css']
})
export class PruebaApiComponent implements OnInit {
  responseData: any;
  newUser: any = {}; // Objeto para almacenar los datos del nuevo usuario
  userUpdate: any = {}; // Objeto para almacenar los datos del usuario a actualizar
  userDetails: any; // Propiedad para almacenar los detalles del usuario por ID
  userId: number = 0; // Agrega esta propiedad para almacenar el ID de usuario
  stockdata: any; //Objeto para alamacenar los datos de todo el stock
  newStock: any = {};
  newCliente: any = {};
  clienteData: any;

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.getStock();
    this.getClientes();
  }

//USUARIOS
  testApiConnection() {
    // Llama al método `getUsers` de tu servicio ApiService para obtener datos de la API
    this.apiService.getUsers().subscribe(data => {
      this.responseData = data;
      console.log('Respuesta de la API:', this.responseData);
    });
  }

  createUser() {
    // Llama al método `createUser` para crear un nuevo usuario en la API
    this.apiService.createUser(this.newUser).subscribe(data => {
      console.log('Usuario creado:', data);
      // Puedes realizar otras acciones aquí, como limpiar el formulario o actualizar la lista de usuarios
    });
  }

  getUserById() {
    this.apiService.getUserById(this.userId).subscribe(data => {
      console.log('Usuario obtenido por ID:', data);
      // Puedes asignar los datos del usuario a una propiedad y mostrarlos en tu vista
      this.userDetails = data;
    });
  }
  
  updateUser() {
    // Llama al método `updateUser` para actualizar un usuario en la API
    this.apiService.updateUser(this.userUpdate).subscribe(data => {
      console.log('Usuario actualizado:', data);
      // Puedes realizar otras acciones aquí, como limpiar el formulario o actualizar la lista de usuarios
    });
  }

//STOCK
  getStock(){
       // Llama al método `updateUser` para actualizar un usuario en la API
       this.apiService.getStock().subscribe(data => {
        this.stockdata= data;
        console.log('Datos de Stock:', data);
        // Puedes realizar otras acciones aquí, como limpiar el formulario o actualizar la lista de usuarios
      });
  }

  createStock(){
    this.apiService.createStock(this.newStock).subscribe(data =>{
      console.log('Stock creado:', data);
    });
  }

//CLIENTES
  getClientes(){
    this.apiService.getClientes().subscribe(data =>{
      this.clienteData = data;
      console.log('Datos Clientes:', data)
    })
  }

  createClientes(){
    this.apiService.createClientes(this.newCliente).subscribe(data =>{
      console.log('Cliente Creado:', data)
    })
  }


}
