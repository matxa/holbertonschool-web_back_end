export default function cleanSet(set, startString) {
  if (startString === '') {
    return '';
  }
  try {
    return [...set]
      .filter((word) => word.startsWith(startString) && typeof word === 'string')
      .map((word) => word.replace(startString, ''))
      .join('-');
  } catch (error) {
    return '';
  }
}
