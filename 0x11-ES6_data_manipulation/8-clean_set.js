export default function cleanSet(set, startString) {
  try {
    const arr = [...set];
    return arr.map((word) => {
      let wordCopy = word;
      if (wordCopy === undefined) wordCopy = '';
      if (wordCopy.startsWith(startString) && startString.length > 0) {
        return wordCopy.replace(startString, '');
      }
      return undefined;
    }).filter((word) => word !== undefined).join('-');
  } catch (error) {
    return '';
  }
}
