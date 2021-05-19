export default function cleanSet(set, startString) {
  if (startString === '') {
    return '';
  }
  try {
    const arr = [...set];
    return arr.filter((word) => word.startsWith(startString) && typeof word === 'string')
      .map((word) => word.split(startString)[1]).join('-');
  } catch (error) {
    return '';
  }
}
