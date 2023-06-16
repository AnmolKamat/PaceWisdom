import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  addFlag :boolean;
  constructor() {
    this.addFlag = false
  }
}
