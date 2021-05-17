export default function getListStudentIds(getListStudents) {
  if (getListStudents instanceof Array) {
    const idArray = getListStudents.map((currentValue) => currentValue.id);
    return idArray;
  }
  return [];
}
