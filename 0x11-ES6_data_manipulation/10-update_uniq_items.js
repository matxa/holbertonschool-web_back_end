export default function updateUniqueItems(map) {
  if (map instanceof Map) {
    for (const item of map) {
      if (item[1] === 1) {
        map.set(item[0], 100);
      }
    }
  } else {
    throw new Error('Cannot process');
  }
  return map;
}
