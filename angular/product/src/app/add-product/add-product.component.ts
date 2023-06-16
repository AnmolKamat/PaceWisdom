import { Component } from '@angular/core';
import { flatMap } from 'rxjs';
import { AppComponent } from '../app.component';
import { DataService } from '../shared/data.service';
import { ProductService } from '../product.service';
import Swal from 'sweetalert2';
@Component({
  selector: 'app-add-product',
  templateUrl: './add-product.component.html',
  styleUrls: ['./add-product.component.scss']
})
export class AddProductComponent {
  constructor(public dataService: DataService,public productService:ProductService) {}
  hideAdd(){
    this.dataService.addFlag = false
  }

  submitForm(){
    event?.preventDefault()
    let productName = document.getElementById("pname") as HTMLInputElement
    let productDescription = document.getElementById("pdesc") as HTMLInputElement
    let productPrice = document.getElementById("pprice") as HTMLInputElement
    this.productService.writeProduct(productName.value,productDescription.value,+productPrice.value)
    Swal.fire({
      position: 'center',
      icon: 'success',
      title: 'Your product has been added',
      showConfirmButton: false,
      timer: 1500
    })
    this.dataService.addFlag = false
  }
}
