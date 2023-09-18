import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PruebaApiComponent } from './prueba-api/prueba-api.component';
import { BodegaComponent } from './bodega/bodega.component';
import { AdminComponent } from './admin/admin.component';
import { PromotorComponent } from './promotor/promotor.component';

@NgModule({
  declarations: [
    AppComponent,
    PruebaApiComponent,
    BodegaComponent,
    AdminComponent,
    PromotorComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
