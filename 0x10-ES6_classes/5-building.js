export default class Building {
  constructor(sqft) {
    this._sqft = sqft
  }

  get sqft() { return this._sqft; }

  set sqft(sqft) { this._sqft = sqft }
}

// stop 9:18pm May 12, 2021
