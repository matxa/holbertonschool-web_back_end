export default function uploadPhoto(filename) {
  return new Promise((_, reject) => reject(new Error(`${filename} cannot be processed`)));
}
