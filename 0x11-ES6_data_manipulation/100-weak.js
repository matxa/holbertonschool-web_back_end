export const weakMap = new WeakMap();

export function queryAPI(endPoint) {
  if (weakMap.has(endPoint) === false) {
    weakMap.set(endPoint, 1);
  } else if (weakMap.get(endPoint) + 1 >= 5) {
    throw new Error('Endpoint load is high');
  } else {
    weakMap.set(endPoint, weakMap.get(endPoint) + 1);
  }
}
