export default function cleanSet(set, startString) {
  if (set instanceof Set && typeof startString === 'string') {
    let string = '';
    set.forEach((setString) => {
      if (setString.startsWith(startString) && startString.length > 0) {
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
  throw new Error('< set > should be a Set && < startString > should be a string');
}
