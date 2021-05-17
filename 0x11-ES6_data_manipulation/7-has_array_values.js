export default function hasValuesFromArray(set, array) {
  const boolSet = new Set();
  array.forEach((item) => {
    if (set.has(item)) {
      boolSet.add(true);
    } else {
      boolSet.add(false);
    }
  });
  return !boolSet.has(false);
}
