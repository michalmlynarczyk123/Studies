import { Component, inject, OnInit } from '@angular/core';
import { NgIcon } from '@ng-icons/core';
import { RouterLink } from '@angular/router';
import { AsyncPipe, NgForOf, NgIf } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { StoreService } from '../../store.service';
import { BackLinkComponent } from '../../back-link/back-link.component';

@Component({
  selector: 'app-categories',
  standalone: true,
  imports: [
    NgIcon,
    RouterLink,
    NgForOf,
    NgIf,
    FormsModule,
    AsyncPipe,
    BackLinkComponent,
  ],
  templateUrl: './categories.component.html',
  styleUrl: './categories.component.css',
})
export class CategoriesComponent implements OnInit {
  private readonly storeService: StoreService = inject(StoreService);
  categories$ = this.storeService.categories$;

  // categories = ['Kategoria 1'];
  showNewCategoryInput = false;
  newCategoryName = '';

  addCategory() {
    this.storeService.addCategory(this.newCategoryName);
    this.newCategoryName = '';
    this.showNewCategoryInput = false;
  }

  removeCategory(categoryId: number) {
    this.storeService.deleteCategory(categoryId);
  }
  ngOnInit(): void {
    this.storeService.fetchCategories();
  }
}
