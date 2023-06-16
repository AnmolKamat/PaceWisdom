import { Component } from '@angular/core';
import { DataService } from './shared/data.service';
import { ProductService } from './product.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'product';
  constructor(public dataService:DataService,public productService:ProductService){}

  showAdd(){
    this.dataService.addFlag = true
  }
}
