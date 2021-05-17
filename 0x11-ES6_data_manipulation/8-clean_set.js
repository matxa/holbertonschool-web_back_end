export default function cleanSet(set, startString) {
  let string = '';
  set.forEach((setString) => {
    if (setString.startsWith(startString) && startString !== '') {
      const [, newString] = setString.split(startString);
      if (string.length < 1) {
        string = newString;
      } else {
        string = `${string}-${newString}`;
      }
    }
  });
  return string;
}
