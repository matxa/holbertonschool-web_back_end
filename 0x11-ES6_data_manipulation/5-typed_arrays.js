export default function createInt8TypedArray(length, position, value) {
  const arrayBuffer = new ArrayBuffer(length);
  const view = new DataView(arrayBuffer);

  try {
    view.setInt8(position, value);
  } catch (error) {
    throw new Error('Position outside range');
  }
  return view;
}
