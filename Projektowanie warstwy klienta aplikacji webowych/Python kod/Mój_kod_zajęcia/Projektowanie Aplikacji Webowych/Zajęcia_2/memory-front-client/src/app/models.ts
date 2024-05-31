export interface Category {
  id: number;
  name: string;
}

export interface Card {
  id: number,
  term: string,
  definition: string,
  category_id: number
}
