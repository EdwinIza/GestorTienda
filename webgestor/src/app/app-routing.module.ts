import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PruebaApiComponent } from './prueba-api/prueba-api.component';
import { BodegaComponent } from './bodega/bodega.component';
import { AdminComponent } from './admin/admin.component';
import { PromotorComponent } from './promotor/promotor.component';


const routes: Routes = [
  { path: 'prueba-api', component: PruebaApiComponent }, // Configura una ruta para PruebaApiComponent
  // Puedes agregar más rutas aquí según sea necesario
  { path: 'bodega', component: BodegaComponent },
  { path: 'admin', component: AdminComponent },
  { path: 'promotor', component: PromotorComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
