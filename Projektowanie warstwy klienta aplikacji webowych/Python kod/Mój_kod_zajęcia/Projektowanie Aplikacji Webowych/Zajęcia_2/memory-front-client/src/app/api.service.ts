import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Category } from './models';
import { Observable } from 'rxjs';
import { observableToBeFn } from 'rxjs/internal/testing/TestScheduler';

const BASE_URL = 'http://localhost:5000';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private readonly httpClient: HttpClient = inject(HttpClient);

  getCategories(): Observable<Category[]> {
    return this.httpClient.get<Category[]>(`${BASE_URL}/categories`);
  }

  addCategory(categoryName: string): Observable<Category> {
    return this.httpClient.post<Category>(`${BASE_URL}/categories`, {
      name: categoryName,
    });
  }

  deleteCategory(categoryId: number): Observable<any> {
    return this.httpClient.delete(`${BASE_URL}/categories/${categoryId}`);
  }
}
