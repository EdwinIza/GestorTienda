import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PruebaApiComponent } from './prueba-api/prueba-api.component';

const routes: Routes = [
  { path: 'prueba-api', component: PruebaApiComponent }, // Configura una ruta para PruebaApiComponent
  // Puedes agregar más rutas aquí según sea necesario
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
