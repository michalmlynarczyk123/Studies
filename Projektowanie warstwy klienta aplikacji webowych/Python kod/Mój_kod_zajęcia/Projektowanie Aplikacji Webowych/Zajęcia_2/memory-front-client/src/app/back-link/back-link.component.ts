import { Component, input } from '@angular/core';
import { NgIcon } from '@ng-icons/core';
import { RouterLink } from '@angular/router';
import { Input } from 'postcss';

@Component({
  selector: 'app-back-link',
  standalone: true,
  imports: [NgIcon, RouterLink],
  templateUrl: './back-link.component.html',
  styleUrl: './back-link.component.css',
})
export class BackLinkComponent {
  @Input() path = '../';
}
