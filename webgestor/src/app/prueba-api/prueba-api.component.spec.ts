import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PruebaApiComponent } from './prueba-api.component';

describe('PruebaApiComponent', () => {
  let component: PruebaApiComponent;
  let fixture: ComponentFixture<PruebaApiComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PruebaApiComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PruebaApiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
