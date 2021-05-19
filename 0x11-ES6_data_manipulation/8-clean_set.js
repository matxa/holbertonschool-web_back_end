export default function cleanSet(set, startString) {
  if (startString === '') return '';
  try {
    const arr = [...set];
    return arr.map((word) => {
      if (word.startsWith(startString) && startString.length > 0) {
        return word.split(startString)[1];
      }
      return undefined;
    }).filter((word) => word !== undefined).join('-');
  } catch (error) {
    return '';
  }
}
