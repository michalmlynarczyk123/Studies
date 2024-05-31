import { Component, inject, OnInit } from '@angular/core';
import { BackLinkComponent } from '../../back-link/back-link.component';
import { NgIcon } from '@ng-icons/core';
import { StoreService } from '../../store.service';
import { ActivatedRoute } from '@angular/router';
import { AsyncPipe, NgForOf, NgIf } from '@angular/common';

@Component({
  selector: 'app-cards',
  standalone: true,
  imports: [
    BackLinkComponent,
    NgIcon,
    NgIf,
    AsyncPipe,
    NgForOf,
  ],
  templateUrl: './cards.component.html',
  styleUrl: './cards.component.css',
})
export class CardsComponent implements OnInit {
  private readonly storeService: StoreService = inject(StoreService);
  private readonly route: ActivatedRoute = inject(ActivatedRoute);

  cards$ = this.storeService.cards$;

  removeCard(categoryId: number, cardId: number) {
    this.storeService.deleteCard(categoryId, cardId)
  }

  ngOnInit() {
    this.route.params.subscribe(
      params => this.storeService.fetchCards(params['id']),
    );
  }
}
