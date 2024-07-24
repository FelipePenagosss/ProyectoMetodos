import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ajusteComponent } from './ajuste.component';

describe('ajuste', () => {
  let component: ajusteComponent;
  let fixture: ComponentFixture<ajusteComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ajusteComponent]
    });
    fixture = TestBed.createComponent(ajusteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
