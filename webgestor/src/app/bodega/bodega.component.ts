import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-bodega',
  templateUrl: './bodega.component.html',
  styleUrls: ['./bodega.component.css']
})
export class BodegaComponent implements OnInit {
  newStock: any = {};
  stockdata: any[] = [];
  selectedProductId: number | null = null;
  selectedStock: any = null;

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.getStock();
  }

  getStock() {
    this.apiService.getStock().subscribe(data => {
      this.stockdata = data;
    });
  }

  createStock() {
    this.apiService.createStock(this.newStock).subscribe(data => {
      console.log('Stock creado:', data);
      this.getStock();
    });
  }

  deleteStock(stockId: number) {
    this.apiService.deleteStock(stockId).subscribe(data => {
      console.log('Stock eliminado:', data);
      this.getStock();
    });
  }

  editStock(stock: any) {
    this.selectedStock = { ...stock };
  }

  saveEdit() {
    if (this.selectedStock) {
      this.apiService.updateStock(this.selectedStock.id, this.selectedStock).subscribe(data => {
        console.log('Stock actualizado:', data);
        this.selectedStock = null;
        this.getStock();
      });
    }
  }

  // Implementa la función para obtener un elemento de stock por su ID
  getStockById(stockId: number) {
    this.apiService.getStockById(stockId).subscribe(data => {
      // Aquí puedes hacer lo que necesites con el elemento de stock obtenido por su ID
      console.log('Stock obtenido por ID:', data);
    });
  }
}
