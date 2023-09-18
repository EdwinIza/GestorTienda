import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent implements OnInit {
  newUser: any = {}; // Objeto para almacenar los datos del nuevo usuario
  dataUser: any;

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }

  createUser() {
    // Llama al método `createUser` para crear un nuevo usuario en la API
    this.apiService.createUser(this.newUser).subscribe(data => {
      console.log('Usuario creado:', data);
      // Puedes realizar otras acciones aquí, como limpiar el formulario o actualizar la lista de usuarios
    });
  }

  getUsers() {
    // Llama al método `getUsers` de tu servicio ApiService para obtener datos de la API
    this.apiService.getUsers().subscribe(data => {
      this.dataUser = data;
      console.log('Respuesta de la API:', this.dataUser);
    });
  }



}
