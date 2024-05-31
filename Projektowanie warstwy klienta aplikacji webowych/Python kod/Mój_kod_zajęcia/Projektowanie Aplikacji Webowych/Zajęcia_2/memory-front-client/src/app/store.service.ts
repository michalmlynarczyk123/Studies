import { inject, Injectable } from '@angular/core';
import { ApiService } from './api.service';
import { BehaviorSubject } from 'rxjs';
import { Category } from './models';

@Injectable({
  providedIn: 'root',
})
export class StoreService {
  private readonly apiService: ApiService = inject(ApiService);
  private _categories = new BehaviorSubject<Category[]>([]);

  categories$ = this._categories.asObservable();

  fetchCategories() {
    this.apiService
      .getCategories()
      .subscribe((categories) => this._categories.next(categories));
  }

  addCategory(categoryName: string) {
    this.apiService.addCategory(categoryName).subscribe((category) => {
      let categories = this._categories.value;
      categories.push(category);
      this._categories.next(categories);
    });
  }

  deleteCategory(categoryId: number) {
    this.apiService.deleteCategory(categoryId).subscribe(() => {
      let categories = this._categories.value;
      let filterCategories = categories.filter(
        (category) => category.id !== categoryId
      );
      this._categories.next(filterCategories);
    });
  }
}
