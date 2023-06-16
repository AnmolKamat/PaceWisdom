import { Injectable ,ChangeDetectorRef} from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  localFile = localStorage.getItem("products")
  db  = this.localFile ? JSON.parse(this.localFile) : [];
  ids = this.db.map((product: { id: number, name: string, description: string, price: number }) =>product.id)
  newId:number = 0
  getId():number{
    this.newId = Math.floor(Math.random()*1000)
    if (this.newId in this.ids){
      return this.getId()
    }
    else{
      return this.newId
    }

  }
  readProduct(){
    return this.db
  }

  writeProduct(name:string,desc:string,price:number){

    this.db.push({"id":this.getId(),"name":name,"desc":desc,"price":price})
    this.localFile = JSON.stringify(this.db)
    localStorage.setItem("products",this.localFile)
  }
  deleteProduct(id:number){
    this.db = this.db.filter((p:{ id: number, name: string, description: string, price: number }) => p.id !== id)
    this.localFile = JSON.stringify(this.db)
    localStorage.setItem("products",this.localFile)
  }

}
