export default function getStudentsByLocation(getListStudents, city) {
  if (getListStudents instanceof Array && typeof city === 'string') {
    return getListStudents.filter((currentValue) => currentValue.location === city);
  }
  return [];
}
